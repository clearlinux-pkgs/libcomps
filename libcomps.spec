#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcomps
Version  : 0.1.17
Release  : 32
URL      : https://github.com/rpm-software-management/libcomps/archive/0.1.17/libcomps-0.1.17.tar.gz
Source0  : https://github.com/rpm-software-management/libcomps/archive/0.1.17/libcomps-0.1.17.tar.gz
Summary  : Comps XML file manipulation library
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: libcomps-lib = %{version}-%{release}
Requires: libcomps-license = %{version}-%{release}
Requires: libcomps-python = %{version}-%{release}
Requires: libcomps-python3 = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : check-dev
BuildRequires : doxygen
BuildRequires : expat-dev
BuildRequires : libxml2-dev
BuildRequires : pkgconfig(expat)
BuildRequires : python3-dev
BuildRequires : zlib-dev

%description
Libcomps is library for structure-like manipulation with content of
comps XML files. Supports read/write XML file, structure(s) modification.

%package dev
Summary: dev components for the libcomps package.
Group: Development
Requires: libcomps-lib = %{version}-%{release}
Provides: libcomps-devel = %{version}-%{release}
Requires: libcomps = %{version}-%{release}

%description dev
dev components for the libcomps package.


%package lib
Summary: lib components for the libcomps package.
Group: Libraries
Requires: libcomps-license = %{version}-%{release}

%description lib
lib components for the libcomps package.


%package license
Summary: license components for the libcomps package.
Group: Default

%description license
license components for the libcomps package.


%package python
Summary: python components for the libcomps package.
Group: Default
Requires: libcomps-python3 = %{version}-%{release}

%description python
python components for the libcomps package.


%package python3
Summary: python3 components for the libcomps package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libcomps package.


%prep
%setup -q -n libcomps-0.1.17
cd %{_builddir}/libcomps-0.1.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629915744
pushd libcomps
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%cmake .. -Wno-dev
make  %{?_smp_mflags}
popd
popd

%install
export SOURCE_DATE_EPOCH=1629915744
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcomps
cp %{_builddir}/libcomps-0.1.17/COPYING %{buildroot}/usr/share/package-licenses/libcomps/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd libcomps
pushd clr-build
%make_install
popd
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libcomps/comps_bradix.h
/usr/include/libcomps/comps_default.h
/usr/include/libcomps/comps_dict.h
/usr/include/libcomps/comps_doc.h
/usr/include/libcomps/comps_doccategory.h
/usr/include/libcomps/comps_docenv.h
/usr/include/libcomps/comps_docgroup.h
/usr/include/libcomps/comps_docgroupid.h
/usr/include/libcomps/comps_docpackage.h
/usr/include/libcomps/comps_elem.h
/usr/include/libcomps/comps_hslist.h
/usr/include/libcomps/comps_log.h
/usr/include/libcomps/comps_log_codes.h
/usr/include/libcomps/comps_mm.h
/usr/include/libcomps/comps_mradix.h
/usr/include/libcomps/comps_obj.h
/usr/include/libcomps/comps_objdict.h
/usr/include/libcomps/comps_objlist.h
/usr/include/libcomps/comps_objmradix.h
/usr/include/libcomps/comps_objradix.h
/usr/include/libcomps/comps_parse.h
/usr/include/libcomps/comps_radix.h
/usr/include/libcomps/comps_set.h
/usr/include/libcomps/comps_utils.h
/usr/include/libcomps/comps_validate.h
/usr/lib64/libcomps.so
/usr/lib64/pkgconfig/libcomps.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcomps.so.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcomps/4cc77b90af91e615a64ae04893fdffa7939db84c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
