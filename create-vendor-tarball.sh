#!/usr/bin/bash

version=$1

if [[ -z ${version} ]]; then
    echo "This script requires the version as an argument."
    exit 1
fi

git clone --branch v${version} --depth 1 https://github.com/juanfont/headscale.git headscale-${version}
pushd headscale-${version}
go mod vendor
popd
XZ_OPT='-9' tar --exclude .git -cJf headscale-${version}-vendored.tar.xz headscale-${version}
rm -rf headscale-${version}

