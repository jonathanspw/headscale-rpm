%bcond_without vendor
%if %{without vendor}
%bcond_without check
%endif

# needed for the way some dependencies work
%global gomodulesmode GO111MODULE=on

# https://github.com/juanfont/headscale
%global goipath         github.com/juanfont/headscale
Version:                0.23.0

%if 0%{?rhel}
%gometa
%else
%gometa -f
%endif

%global common_description %{expand:
An open source, self-hosted implementation of the Tailscale control server.}

%global golicenses      LICENSE

Name:           headscale
Release:        1%{?dist}
Summary:        An open source, self-hosted implementation of the Tailscale control server

License:        BSD-3-Clause
URL:            %{gourl}
%if %{with vendor}
# see create-vendor-tarball.sh in this distgit repo
Source0:        headscale-%{version}-vendored.tar.xz
%else
Source0:        %{gosource}
%endif
Source1:        headscale.service
Source2:        headscale.tmpfiles
Source3:        headscale.sysusers
Source4:        config.yaml


BuildRequires:  git-core
BuildRequires:  systemd-rpm-macros
BuildRequires:  tar

Requires: systemd

%description %{common_description}


%if %{without vendor}
%gopkg
%endif


%prep
%goprep %{?with_vendor:-k}
#%%autopatch -p1


%build
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/%{name}


%install
%if %{without vendor}
%gopkginstall
%endif

install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m 0755 %{buildroot}/run/%{name}/
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/headscale.sysusers
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -d -m 0755 %{buildroot}%{_sharedstatedir}/headscale/
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/headscale/config.yaml


%if %{with check}
%check
%gocheck
%endif


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

%if %{without vendor}
%gopkgfiles
%endif


%changelog
* Thu Dec 19 2024 jonathanspw <8390543+jonathanspw@users.noreply.github.com> - 0.23.0-1
- update to 0.23.0

* Mon Jan 22 2024 Jonathan Wright <jonathan@almalinux.org> - 0.22.3-3
- Update systemd unit to After=network-online.target

* Fri Jun 07 2023 Dusty Mabe <dusty@dustymabe.com> - 0.22.3-2
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
