# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-ldap3
Epoch: 100
Version: 2.9.1
Release: 1%{?dist}
BuildArch: noarch
Summary: A strictly RFC 4510 conforming LDAP V3 pure Python client library
License: LGPL-3.0-only
URL: https://github.com/cannatag/ldap3/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
ldap3 is a strictly RFC 4510 conforming LDAP V3 pure Python client
library. The same codebase runs in Python 2, Python 3, PyPy and PyPy3.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-ldap3
Summary: A strictly RFC 4510 conforming LDAP V3 pure Python client library
Requires: python3
Requires: python3-pyasn1 >= 0.4.6
Provides: python3-ldap3 = %{epoch}:%{version}-%{release}
Provides: python3dist(ldap3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ldap3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ldap3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ldap3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ldap3) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-ldap3
ldap3 is a strictly RFC 4510 conforming LDAP V3 pure Python client
library. The same codebase runs in Python 2, Python 3, PyPy and PyPy3.

%files -n python%{python3_version_nodots}-ldap3
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-ldap3
Summary: A strictly RFC 4510 conforming LDAP V3 pure Python client library
Requires: python3
Requires: python3-pyasn1 >= 0.4.6
Provides: python3-ldap3 = %{epoch}:%{version}-%{release}
Provides: python3dist(ldap3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ldap3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ldap3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ldap3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ldap3) = %{epoch}:%{version}-%{release}

%description -n python3-ldap3
ldap3 is a strictly RFC 4510 conforming LDAP V3 pure Python client
library. The same codebase runs in Python 2, Python 3, PyPy and PyPy3.

%files -n python3-ldap3
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-ldap3
Summary: A strictly RFC 4510 conforming LDAP V3 pure Python client library
Requires: python3
Requires: python3-pyasn1 >= 0.4.6
Provides: python3-ldap3 = %{epoch}:%{version}-%{release}
Provides: python3dist(ldap3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ldap3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ldap3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ldap3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ldap3) = %{epoch}:%{version}-%{release}

%description -n python3-ldap3
ldap3 is a strictly RFC 4510 conforming LDAP V3 pure Python client
library. The same codebase runs in Python 2, Python 3, PyPy and PyPy3.

%files -n python3-ldap3
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
