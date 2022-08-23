#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-idna_ssl
Version  : 1.1.0
Release  : 32
URL      : https://files.pythonhosted.org/packages/46/03/07c4894aae38b0de52b52586b24bf189bb83e4ddabfe2e2c8f2419eec6f4/idna-ssl-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/46/03/07c4894aae38b0de52b52586b24bf189bb83e4ddabfe2e2c8f2419eec6f4/idna-ssl-1.1.0.tar.gz
Summary  : Patch ssl.match_hostname for Unicode(idna) domains support
Group    : Development/Tools
License  : MIT
Requires: pypi-idna_ssl-license = %{version}-%{release}
Requires: pypi-idna_ssl-python = %{version}-%{release}
Requires: pypi-idna_ssl-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(idna)
BuildRequires : pypi(pytest_runner)

%description
========

%package license
Summary: license components for the pypi-idna_ssl package.
Group: Default

%description license
license components for the pypi-idna_ssl package.


%package python
Summary: python components for the pypi-idna_ssl package.
Group: Default
Requires: pypi-idna_ssl-python3 = %{version}-%{release}

%description python
python components for the pypi-idna_ssl package.


%package python3
Summary: python3 components for the pypi-idna_ssl package.
Group: Default
Requires: python3-core
Provides: pypi(idna_ssl)
Requires: pypi(idna)

%description python3
python3 components for the pypi-idna_ssl package.


%prep
%setup -q -n idna-ssl-1.1.0
cd %{_builddir}/idna-ssl-1.1.0
pushd ..
cp -a idna-ssl-1.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656400628
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-idna_ssl
cp %{_builddir}/idna-ssl-1.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-idna_ssl/6b8689c0fd8786e0c546e954329ce66432f51dc1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-idna_ssl/6b8689c0fd8786e0c546e954329ce66432f51dc1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
