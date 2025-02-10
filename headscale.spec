# https://github.com/juanfont/headscale
%global goipath github.com/juanfont/headscale

# needed for the way some dependencies work
%global gomodulesmode GO111MODULE=on

%global common_description %{expand:
An open source, self-hosted implementation of the Tailscale control server.}

Name:           headscale
Version:        0.24.3
Release:        1%{?dist}
Summary:        An open source, self-hosted implementation of the Tailscale control server

License:        BSD-2-Clause AND MIT AND Apache-2.0 AND MPL-2.0 AND BSD-2-Clause-Views AND ISC AND BSD-3-Clause AND ISC
URL:            https://github.com/juanfont/headscale
# see create-vendor-tarball.sh in this distgit repo
Source0:        headscale-%{version}-vendored.tar.xz
Source1:        headscale.service
Source2:        headscale.tmpfiles
Source3:        headscale.sysusers
Source4:        config.yaml

%if %{defined el8}
ExclusiveArch:  %{golang_arches}
%else
ExclusiveArch:  %{golang_arches_future}
BuildRequires:  go-rpm-macros
%endif

BuildRequires:  git-core
BuildRequires:  systemd-rpm-macros
BuildRequires:  tar

Requires: systemd


# MIT
Provides:       bundled(golang(github.com/AlecAivazis/survey/v2)) = v2.3.7
# MIT
Provides:       bundled(golang(github.com/cenkalti/backoff/v4)) = v4.3.0
# MIT
Provides:       bundled(golang(github.com/chasefleming/elem-go)) = v0.30.0
# ISC
Provides:       bundled(golang(github.com/coder/websocket)) = v1.8.12
# Apache-2.0
Provides:       bundled(golang(github.com/coreos/go-oidc/v3)) = v3.11.0
# ISC
Provides:       bundled(golang(github.com/davecgh/go-spew)) = v1.1.2~0.20180830191138~d8f796af33cc
# BSD-3-Clause
Provides:       bundled(golang(github.com/fsnotify/fsnotify)) = v1.8.0
# MIT
Provides:       bundled(golang(github.com/glebarez/sqlite)) = v1.11.0
# MIT
Provides:       bundled(golang(github.com/go-gormigrate/gormigrate/v2)) = v2.1.3
# MIT
Provides:       bundled(golang(github.com/gofrs/uuid/v5)) = v5.3.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/google/go-cmp)) = v0.6.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/gorilla/mux)) = v1.8.1
# Apache-2.0
Provides:       bundled(golang(github.com/grpc-ecosystem/go-grpc-middleware)) = v1.4.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/grpc-ecosystem/grpc-gateway/v2)) = v2.24.0
# MIT
Provides:       bundled(golang(github.com/jagottsicher/termcolor)) = v1.0.2
# BSD-3-Clause OR Apache-2.0 OR MIT
Provides:       bundled(golang(github.com/klauspost/compress)) = v1.17.11
# MIT
Provides:       bundled(golang(github.com/oauth2-proxy/mockoidc)) = v0.0.0~20240214162133~caebfff84d25
# Apache-2.0
Provides:       bundled(golang(github.com/ory/dockertest/v3)) = v3.11.0
# MIT
Provides:       bundled(golang(github.com/philip-bui/grpc-zerolog)) = v1.0.1
# BSD-2-Clause
Provides:       bundled(golang(github.com/pkg/profile)) = v1.7.0
# Apache-2.0
Provides:       bundled(golang(github.com/prometheus/client_golang)) = v1.20.5
# Apache-2.0
Provides:       bundled(golang(github.com/prometheus/common)) = v0.61.0
# MIT
Provides:       bundled(golang(github.com/pterm/pterm)) = v0.12.80
# Apache-2.0
Provides:       bundled(golang(github.com/puzpuzpuz/xsync/v3)) = v3.4.0
# MIT
Provides:       bundled(golang(github.com/rs/zerolog)) = v1.33.0
# MIT
Provides:       bundled(golang(github.com/samber/lo)) = v1.47.0
# Apache-2.0
Provides:       bundled(golang(github.com/sasha-s/go-deadlock)) = v0.3.5
# Apache-2.0
Provides:       bundled(golang(github.com/spf13/cobra)) = v1.8.1
# Apache-2.0
Provides:       bundled(golang(github.com/spf13/viper)) = v1.20.0~alpha.6
# MIT
Provides:       bundled(golang(github.com/stretchr/testify)) = v1.10.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/tailscale/hujson)) = v0.0.0~20241010212012~29efb4a0184b
# BSD-3-Clause
Provides:       bundled(golang(github.com/tailscale/tailsql)) = v0.0.0~20241211062219~bf96884c6a49
# MIT
Provides:       bundled(golang(github.com/tcnksm/go-latest)) = v0.0.0~20170313132115~e3007ae9052e
# BSD-3-Clause
Provides:       bundled(golang(go4.org/netipx)) = v0.0.0~20231129151722~fdeea329fbba
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/crypto)) = v0.31.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/exp)) = v0.0.0~20241215155358~4a5509556b9e
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/net)) = v0.32.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/oauth2)) = v0.24.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/sync)) = v0.10.0
# Apache-2.0
Provides:       bundled(golang(google.golang.org/genproto/googleapis/api)) = v0.0.0~20241216192217~9240e9c98484
# Apache-2.0
Provides:       bundled(golang(google.golang.org/grpc)) = v1.69.0
# BSD-3-Clause
Provides:       bundled(golang(google.golang.org/protobuf)) = v1.36.0
# BSD-2-Clause
Provides:       bundled(golang(gopkg.in/check.v1)) = v1.0.0~20201130134442~10cb98267c6c
# MIT OR Apache-2.0
Provides:       bundled(golang(gopkg.in/yaml.v3)) = v3.0.1
# MIT
Provides:       bundled(golang(gorm.io/driver/postgres)) = v1.5.11
# MIT
Provides:       bundled(golang(gorm.io/gorm)) = v1.25.12
# BSD-3-Clause
Provides:       bundled(golang(tailscale.com)) = v1.79.0~pre
# MIT
Provides:       bundled(golang(zgo.at/zcache/v2)) = v2.1.0
# Apache-2.0
Provides:       bundled(golang(zombiezen.com/go/postgrestest)) = v1.0.1
# BSD-3-Clause
Provides:       bundled(golang(modernc.org/libc)) = v1.55.3
# BSD-3-Clause
Provides:       bundled(golang(modernc.org/mathutil)) = v1.6.0
# BSD-3-Clause
Provides:       bundled(golang(modernc.org/memory)) = v1.8.0
# BSD-3-Clause
Provides:       bundled(golang(modernc.org/sqlite)) = v1.33.1
# MIT
Provides:       bundled(golang(atomicgo.dev/cursor)) = v0.2.0
# MIT
Provides:       bundled(golang(atomicgo.dev/keyboard)) = v0.2.9
# MIT
Provides:       bundled(golang(atomicgo.dev/schedule)) = v0.1.0
# BSD-3-Clause
Provides:       bundled(golang(dario.cat/mergo)) = v1.0.1
# BSD-3-Clause
Provides:       bundled(golang(filippo.io/edwards25519)) = v1.1.0
# MIT
Provides:       bundled(golang(github.com/Azure/go-ansiterm)) = v0.0.0~20230124172434~306776ec8161
# MIT
Provides:       bundled(golang(github.com/Microsoft/go-winio)) = v0.6.2
# BSD-2-Clause-Views
Provides:       bundled(golang(github.com/Nvveen/Gotty)) = v0.0.0~20120604004816~cd527374f1e5
# Apache-2.0
Provides:       bundled(golang(github.com/akutz/memconn)) = v0.1.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/alexbrainman/sspi)) = v0.0.0~20231016080023~1a75b4708caa
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2)) = v1.26.1
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/config)) = v1.27.11
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/credentials)) = v1.17.11
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)) = v1.16.1
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/internal/configsources)) = v1.3.5
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)) = v2.6.5
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/internal/ini)) = v1.8.0
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)) = v1.11.2
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)) = v1.11.7
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/ssm)) = v1.45.0
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/sso)) = v1.20.5
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/ssooidc)) = v1.23.4
# Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/sts)) = v1.28.6
# Apache-2.0
Provides:       bundled(golang(github.com/aws/smithy-go)) = v1.20.2
# MIT
Provides:       bundled(golang(github.com/beorn7/perks)) = v1.0.1
# BSD-3-Clause
Provides:       bundled(golang(github.com/bits-and-blooms/bitset)) = v1.13.0
# MIT
Provides:       bundled(golang(github.com/cespare/xxhash/v2)) = v2.3.0
# Apache-2.0
Provides:       bundled(golang(github.com/containerd/console)) = v1.0.4
# Apache-2.0
Provides:       bundled(golang(github.com/containerd/continuity)) = v0.4.5
# Apache-2.0
Provides:       bundled(golang(github.com/coreos/go-iptables)) = v0.7.1~0.20240112124308~65c67c9f46e6
# BSD-3-Clause
Provides:       bundled(golang(github.com/creachadair/mds)) = v0.20.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/dblohm7/wingoes)) = v0.0.0~20240123200102~b75a8a7d7eb0
# Apache-2.0
Provides:       bundled(golang(github.com/digitalocean/go-smbios)) = v0.0.0~20180907143718~390a4f403a8e
# Apache-2.0
Provides:       bundled(golang(github.com/docker/cli)) = v27.4.0+incompatible
# Apache-2.0
Provides:       bundled(golang(github.com/docker/docker)) = v27.4.0+incompatible
# Apache-2.0
Provides:       bundled(golang(github.com/docker/go-connections)) = v0.5.0
# Apache-2.0
Provides:       bundled(golang(github.com/docker/go-units)) = v0.5.0
# MIT
Provides:       bundled(golang(github.com/dustin/go-humanize)) = v1.0.1
# MIT
Provides:       bundled(golang(github.com/felixge/fgprof)) = v0.9.5
# MIT
Provides:       bundled(golang(github.com/fxamacker/cbor/v2)) = v2.6.0
# MIT
Provides:       bundled(golang(github.com/gaissmai/bart)) = v0.11.1
# BSD-3-Clause
Provides:       bundled(golang(github.com/glebarez/go-sqlite)) = v1.22.0
# Apache-2.0
Provides:       bundled(golang(github.com/go-jose/go-jose/v3)) = v3.0.3
# Apache-2.0
Provides:       bundled(golang(github.com/go-jose/go-jose/v4)) = v4.0.2
# BSD-3-Clause
Provides:       bundled(golang(github.com/go-json-experiment/json)) = v0.0.0~20231102232822~2e55bd4e08b0
# MIT
Provides:       bundled(golang(github.com/go-ole/go-ole)) = v1.3.0
# MIT
Provides:       bundled(golang(github.com/go-viper/mapstructure/v2)) = v2.2.1
# BSD-2-Clause
Provides:       bundled(golang(github.com/godbus/dbus/v5)) = v5.1.1~0.20230522191255~76236955d466
# BSD-3-Clause
Provides:       bundled(golang(github.com/gogo/protobuf)) = v1.3.2
# MIT
Provides:       bundled(golang(github.com/golang-jwt/jwt/v5)) = v5.2.1
# Apache-2.0
Provides:       bundled(golang(github.com/golang/groupcache)) = v0.0.0~20210331224755~41bb18bfe9da
# BSD-3-Clause
Provides:       bundled(golang(github.com/golang/protobuf)) = v1.5.4
# Apache-2.0
Provides:       bundled(golang(github.com/google/btree)) = v1.1.2
# BSD-3-Clause
Provides:       bundled(golang(github.com/google/go-github)) = v17.0.0+incompatible
# BSD-3-Clause
Provides:       bundled(golang(github.com/google/go-querystring)) = v1.1.0
# Apache-2.0
Provides:       bundled(golang(github.com/google/nftables)) = v0.2.1~0.20240414091927~5e242ec57806
# Apache-2.0
Provides:       bundled(golang(github.com/google/pprof)) = v0.0.0~20241210010833~40e02aabc2ad
# Apache-2.0
Provides:       bundled(golang(github.com/google/shlex)) = v0.0.0~20191202100458~e7afc7fbc510
# BSD-3-Clause
Provides:       bundled(golang(github.com/google/uuid)) = v1.6.0
# MIT
Provides:       bundled(golang(github.com/gookit/color)) = v1.5.4
# BSD-3-Clause
Provides:       bundled(golang(github.com/gorilla/csrf)) = v1.7.2
# BSD-3-Clause
Provides:       bundled(golang(github.com/gorilla/securecookie)) = v1.1.2
# MPL-2.0
Provides:       bundled(golang(github.com/hashicorp/go-version)) = v1.7.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/hdevalence/ed25519consensus)) = v0.2.0
# MIT
Provides:       bundled(golang(github.com/illarion/gonotify/v2)) = v2.0.3
# Apache-2.0
Provides:       bundled(golang(github.com/inconshreveable/mousetrap)) = v1.1.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/insomniacslk/dhcp)) = v0.0.0~20240129002554~15c9b8791914
# MIT
Provides:       bundled(golang(github.com/jackc/pgpassfile)) = v1.0.0
# MIT
Provides:       bundled(golang(github.com/jackc/pgservicefile)) = v0.0.0~20240606120523~5a60cdf6a761
# MIT
Provides:       bundled(golang(github.com/jackc/pgx/v5)) = v5.7.1
# MIT
Provides:       bundled(golang(github.com/jackc/puddle/v2)) = v2.2.2
# MIT
Provides:       bundled(golang(github.com/jinzhu/inflection)) = v1.0.0
# MIT
Provides:       bundled(golang(github.com/jinzhu/now)) = v1.1.5
# Apache-2.0
Provides:       bundled(golang(github.com/jmespath/go-jmespath)) = v0.4.0
# MIT
Provides:       bundled(golang(github.com/josharian/native)) = v1.1.1~0.20230202152459~5c7d0dd6ab86
# MIT
Provides:       bundled(golang(github.com/jsimonetti/rtnetlink)) = v1.4.1
# MIT
Provides:       bundled(golang(github.com/kballard/go-shellquote)) = v0.0.0~20180428030007~95032a82bc51
# BSD-3-Clause
Provides:       bundled(golang(github.com/kortschak/wol)) = v0.0.0~20200729010619~da482cc4850a
# MIT
Provides:       bundled(golang(github.com/kr/pretty)) = v0.3.1
# MIT
Provides:       bundled(golang(github.com/kr/text)) = v0.2.0
# MIT
Provides:       bundled(golang(github.com/lib/pq)) = v1.10.9
# MIT
Provides:       bundled(golang(github.com/lithammer/fuzzysearch)) = v1.1.8
# MIT
Provides:       bundled(golang(github.com/mattn/go-colorable)) = v0.1.13
# MIT
Provides:       bundled(golang(github.com/mattn/go-isatty)) = v0.0.20
# MIT
Provides:       bundled(golang(github.com/mattn/go-runewidth)) = v0.0.16
# MIT
Provides:       bundled(golang(github.com/mdlayher/genetlink)) = v1.3.2
# MIT
Provides:       bundled(golang(github.com/mdlayher/netlink)) = v1.7.2
# MIT
Provides:       bundled(golang(github.com/mdlayher/sdnotify)) = v1.0.0
# MIT
Provides:       bundled(golang(github.com/mdlayher/socket)) = v0.5.0
# MIT
Provides:       bundled(golang(github.com/mgutz/ansi)) = v0.0.0~20200706080929~d51e80ef957d
# BSD-3-Clause
Provides:       bundled(golang(github.com/miekg/dns)) = v1.1.58
# MIT
Provides:       bundled(golang(github.com/mitchellh/go-ps)) = v1.0.0
# Apache-2.0
Provides:       bundled(golang(github.com/moby/docker-image-spec)) = v1.3.1
# Apache-2.0
Provides:       bundled(golang(github.com/moby/sys/user)) = v0.3.0
# Apache-2.0
Provides:       bundled(golang(github.com/moby/term)) = v0.5.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/munnerz/goautoneg)) = v0.0.0~20191010083416~a7dc8b61c822
# MIT
Provides:       bundled(golang(github.com/ncruces/go-strftime)) = v0.1.9
# Apache-2.0
Provides:       bundled(golang(github.com/opencontainers/go-digest)) = v1.0.0
# Apache-2.0
Provides:       bundled(golang(github.com/opencontainers/image-spec)) = v1.1.0
# Apache-2.0
Provides:       bundled(golang(github.com/opencontainers/runc)) = v1.2.3
# MIT
Provides:       bundled(golang(github.com/pelletier/go-toml/v2)) = v2.2.3
# Apache-2.0
Provides:       bundled(golang(github.com/petermattis/goid)) = v0.0.0~20241211131331~93ee7e083c43
# BSD-3-Clause
Provides:       bundled(golang(github.com/pierrec/lz4/v4)) = v4.1.21
# BSD-2-Clause
Provides:       bundled(golang(github.com/pkg/errors)) = v0.9.1
# BSD-3-Clause
Provides:       bundled(golang(github.com/pmezard/go-difflib)) = v1.0.1~0.20181226105442~5d4384ee4fb2
# MIT
Provides:       bundled(golang(github.com/prometheus-community/pro-bing)) = v0.4.0
# Apache-2.0
Provides:       bundled(golang(github.com/prometheus/client_model)) = v0.6.1
# Apache-2.0
Provides:       bundled(golang(github.com/prometheus/procfs)) = v0.15.1
# BSD-3-Clause
Provides:       bundled(golang(github.com/remyoudompheng/bigfft)) = v0.0.0~20230129092748~24d4a6f8daec
# MIT
Provides:       bundled(golang(github.com/rivo/uniseg)) = v0.4.7
# BSD-3-Clause
Provides:       bundled(golang(github.com/rogpeppe/go-internal)) = v1.13.1
# Apache-2.0
Provides:       bundled(golang(github.com/safchain/ethtool)) = v0.3.0
# MIT
Provides:       bundled(golang(github.com/sagikazarmark/locafero)) = v0.6.0
# MIT
Provides:       bundled(golang(github.com/sirupsen/logrus)) = v1.9.3
# MIT
Provides:       bundled(golang(github.com/sourcegraph/conc)) = v0.3.0
# Apache-2.0
Provides:       bundled(golang(github.com/spf13/afero)) = v1.11.0
# MIT
Provides:       bundled(golang(github.com/spf13/cast)) = v1.7.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/spf13/pflag)) = v1.0.5
# MIT
Provides:       bundled(golang(github.com/subosito/gotenv)) = v1.6.0
# MIT
Provides:       bundled(golang(github.com/tailscale/certstore)) = v0.1.1~0.20231202035212~d3fa0460f47e
# MIT
Provides:       bundled(golang(github.com/tailscale/go-winio)) = v0.0.0~20231025203758~c4f33415bf55
# BSD-3-Clause
Provides:       bundled(golang(github.com/tailscale/golang-x-crypto)) = v0.0.0~20240604161659~3fde5e568aa4
# BSD-2-Clause
Provides:       bundled(golang(github.com/tailscale/goupnp)) = v1.0.1~0.20210804011211~c64d0f06ea05
# Apache-2.0
Provides:       bundled(golang(github.com/tailscale/netlink)) = v1.1.1~0.20240822203006~4d49adab4de7
# BSD-3-Clause
Provides:       bundled(golang(github.com/tailscale/peercred)) = v0.0.0~20240214030740~b535050b2aa4
# BSD-3-Clause
Provides:       bundled(golang(github.com/tailscale/setec)) = v0.0.0~20240930150730~e6eb93658ed3
# BSD-3-Clause
Provides:       bundled(golang(github.com/tailscale/squibble)) = v0.0.0~20240909231413~32a80b9743f7
# BSD-3-Clause
Provides:       bundled(golang(github.com/tailscale/web-client-prebuilt)) = v0.0.0~20240226180453~5db17b287bf1
# MIT
Provides:       bundled(golang(github.com/tailscale/wireguard-go)) = v0.0.0~20241113014420~4e883d38c8d3
# MIT
Provides:       bundled(golang(github.com/tcnksm/go-httpstat)) = v0.2.0
# BSD-3-Clause
Provides:       bundled(golang(github.com/u-root/uio)) = v0.0.0~20240118234441~a3c409a6018e
# Apache-2.0
Provides:       bundled(golang(github.com/vishvananda/netns)) = v0.0.4
# MIT
Provides:       bundled(golang(github.com/x448/float16)) = v0.8.4
# Apache-2.0
Provides:       bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0~20190905194746~02993c407bfb
# Apache-2.0
Provides:       bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0~20180127040603~bd5ef7bd5415
# Apache-2.0
Provides:       bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0
# MIT
Provides:       bundled(golang(github.com/xo/terminfo)) = v0.0.0~20220910002029~abceb7e1c41e
# MIT
Provides:       bundled(golang(go.uber.org/multierr)) = v1.11.0
# Apache-2.0
Provides:       bundled(golang(go4.org/mem)) = v0.0.0~20220726221520~4f986261bf13
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/mod)) = v0.22.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/sys)) = v0.28.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/term)) = v0.27.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/text)) = v0.21.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/time)) = v0.5.0
# BSD-3-Clause
Provides:       bundled(golang(golang.org/x/tools)) = v0.28.0
# MIT
Provides:       bundled(golang(golang.zx2c4.com/wintun)) = v0.0.0~20230126152724~0fa3db229ce2
# MIT
Provides:       bundled(golang(golang.zx2c4.com/wireguard/windows)) = v0.5.3
# Apache-2.0
Provides:       bundled(golang(google.golang.org/genproto/googleapis/rpc)) = v0.0.0~20241216192217~9240e9c98484
# Apache-2.0 OR MIT
Provides:       bundled(golang(gopkg.in/yaml.v2)) = v2.4.0
# Apache-2.0 OR MIT
Provides:       bundled(golang(gvisor.dev/gvisor)) = v0.0.0~20240722211153~64c016c92987

%description %{common_description}


%prep
%autosetup -p1 -n %{name}-0.24.3
# this is the same as %%goprep
mkdir -p src/$(dirname %{goipath})
ln -s $PWD src/%{goipath}


%build
%gobuild -o bin/%{name} %{goipath}/cmd/%{name}


%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp bin/* %{buildroot}%{_bindir}/
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m 0755 %{buildroot}/run/%{name}/
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/headscale.sysusers
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -d -m 0755 %{buildroot}%{_sharedstatedir}/headscale/
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/headscale/config.yaml


%pre
%sysusers_create_compat %{SOURCE3}


%post
%systemd_post headscale.service


%preun
%systemd_preun headscale.service


%postun
%systemd_postun_with_restart headscale.service


%files
%license LICENSE
%doc docs/ README.md CHANGELOG.md
%{_bindir}/headscale
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.sysusers
%{_unitdir}/%{name}.service
%dir %attr(0755,headscale,headscale) %{_sharedstatedir}/%{name}/
%attr(0755,headscale,headscale) %{_sysconfdir}/%{name}/
%attr(0644,headscale,headscale) %config(noreplace) %{_sysconfdir}/%{name}/config.yaml


%changelog
* Mon Feb 10 2025 Jonathan Wright <jonathan@almalinux.org> - 0.24.3-1
- update to 0.24.3

* Thu Dec 19 2024 Jonathan Wright <jonathan@almalinux.org> - 0.24.0~BETA2-1
- update to 0.24.0-beta.2
- update spec: remove almost all golang macros

* Thu Dec 19 2024 Jonathan Wright <jonathan@almalinux.org> - 0.23.0-3
- update spec: add complete license information
  add complete provides for vendored rpm
  remove non-vendored conditionals

* Thu Dec 19 2024 Jonathan Wright <jonathan@almalinux.org> - 0.23.0-2
- fix default config for 0.23.0

* Thu Dec 19 2024 Jonathan Wright <jonathan@almalinux.org> - 0.23.0-1
- update to 0.23.0

* Mon Jan 22 2024 Jonathan Wright <jonathan@almalinux.org> - 0.22.3-3
- Update systemd unit to After=network-online.target

* Fri Jul 07 2023 Dusty Mabe <dusty@dustymabe.com> - 0.22.3-2
- Add Requires on systemd

* Fri May 12 2023 Jonathan Wright <jonathan@almalinux.org> - 0.22.3-1
- Update to 0.22.3

* Tue Apr 25 2023 Jonathan Wright <jonathan@almalinux.org> - 0.22.1-2
- Add patch to fix high CPU usage from ACLs

* Thu Apr 20 2023 Jonathan Wright <jonathan@almalinux.org> - 0.22.1-1
- Update to 0.22.1

* Thu Apr 20 2023 Jonathan Wright <jonathan@almalinux.org> - 0.22.0-1
- Update to 0.22.0
- Use vendored source tarball

* Wed Apr 19 2023 Jonathan Wright <jonathan@almalinux.org> - 0.21.0-3
- allow binding of privileged ports

* Wed Apr 19 2023 Jonathan Wright <jonathan@almalinux.org> - 0.21.0-2
- add preferred_username field patch

* Wed Apr 19 2023 Jonathan Wright <jonathan@almalinux.org> - 0.21.0-1
- Initial package build
