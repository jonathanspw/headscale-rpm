#!/usr/bin/bash
# because fedora diverges from golang upstream
# this fixes some commits that otherwise wouldn't
# resolve when fetching dependencies
export GOPROXY=https://proxy.golang.org,direct

usage() {
  echo "Usage: $0 [-d value]... [-v version] [-l]"
  echo "  -d    delete entries from go.sum.  May be repeated.  Ex: fybrik.io/crdoc"
  echo "  -v    version of package to be bundled"
  echo "  -l    generate license text for spec file"
  exit 1
}

if [ $# == 0 ]; then
  usage
fi

declare -a d_values
do_license=false

while (( "$#" )); do
  case "$1" in
    -d)
      d_values+=("$2")
      shift 2
      ;;
    -v)
      version="$2"
      shift 2
      ;;
    -l)
      do_license=true
      shift
      ;;
    --)
      shift
      break
      ;;
    *)
      usage
      ;;
  esac
done

# Check if version is set
if [ -z "$version" ]; then
  echo "Error: -v is a required argument"
  usage
fi

git clone --branch v${version} --depth 1 https://github.com/juanfont/headscale.git headscale-${version}
pushd headscale-${version}

# clean up go.sum based on inputs
for value in "${d_values[@]}"; do
  sed -i "/^${value}/d" go.sum
done

# go vendoring
go mod tidy
go mod vendor

# let's parse bundled deps and licenses
if $do_license; then
	declare -A LICENSE_ASSOC_ARR
	for dep in $(go mod edit -json | jq -r '.Require.[] | "\(.Path);\(.Version)"'); do
	        GO_MOD_PATH=$(echo -n $dep | awk -F ';' '{ printf "%s", $1 }')
	        GO_MOD_PATH_URLENCODE=$(echo -n $GO_MOD_PATH | jq -sRr @uri)
	        VERSION=$(echo -n $dep | awk -F ';' '{ printf "%s", $2 }')
	        VERSION_SPEC=$(echo $VERSION | sed 's/-/~/g')
	        CURL_OUT=$(curl -s https://api.deps.dev/v3/systems/go/packages/$GO_MOD_PATH_URLENCODE/versions/$VERSION)
	        LICENSES=$(echo -n $CURL_OUT | jq -r '.licenses | join(" OR ")' 2> /dev/null)
	        if [ ! -z "$LICENSES" ]; then
	                if echo "$LICENSES" | grep -q " OR "; then
	                        LICENSE_ASSOC_ARR["($LICENSES)"]=1
	                else
	                        LICENSE_ASSOC_ARR["$LICENSES"]=1
	                fi
	        else
		# if we couldn't match a license on the exact version, try the default version
			CURL_OUT=$(curl -s https://api.deps.dev/v3/systems/go/packages/$GO_MOD_PATH_URLENCODE)
			DEFAULT_VERSION=$(echo -n $CURL_OUT | jq -r '.versions.[] | select(.isDefault==true) | .versionKey.version' 2> /dev/null)
			CURL_OUT=$(curl -s https://api.deps.dev/v3/systems/go/packages/$GO_MOD_PATH_URLENCODE/versions/$DEFAULT_VERSION)
		        LICENSES_2ND=$(echo -n $CURL_OUT | jq -r '.licenses | join(" OR ")' 2> /dev/null)
		        if [ ! -z "$LICENSES_2ND" ]; then
		                if echo "$LICENSES_2ND" | grep -q " OR "; then
	        	                LICENSE_ASSOC_ARR["($LICENSES_2ND)"]=1
	               		else
	                        	LICENSE_ASSOC_ARR["$LICENSES_2ND"]=1
	                	fi
	        	fi
		fi
	        if [ ! -z "$LICENSES" ]; then
			echo "# $LICENSES"
		else
			echo "# $LICENSES_2ND"
		fi
	        echo "Provides:       bundled(golang($GO_MOD_PATH)) = $VERSION_SPEC"
	done

	echo ""

	# flip back to an indexed array so we can use the values
	LICENSE_ARR=("${!LICENSE_ASSOC_ARR[@]}")
	# merge array values into an SPDX string
	LICENSE_STRING=$(printf "%s AND "  "${LICENSE_ARR[@]}")
	# remove extra "AND".  there's probably a better way to do this
	LICENSE_STRING=${LICENSE_STRING::-4}
	echo "License string for spec.  Don't forget to include the base software's license if not included."
	echo $LICENSE_STRING
	echo ""
fi

popd
#XZ_OPT='-e -9 -T0' tar --exclude .git -cJf headscale-${version}-vendored.tar.xz headscale-${version}
tar -I "zstd -T0 --ultra -22" --exclude .git -cf headscale-${version}-vendored.tar.zst headscale-${version}
rm -rf headscale-${version}
