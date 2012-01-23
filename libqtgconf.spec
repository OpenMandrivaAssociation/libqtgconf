%define major 1
%define libname %mklibname qtgconf %{major}
%define develname %mklibname qtgconf -d

Summary:	Qt binding and QML plugin for GConf
Name:		libqtgconf
Version:	0.1
Release:	1
License:	LGPLv2
Url:		http://launchpad.net/gconf-qt
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE - libqtgconf-cmake-libdir-fix.patch nmarques@opensuse.org -- not again...
Patch0:		%{name}-cmake-libdir-fix.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtDeclarative)

%description
Simple Qt binding and QML plugin for GConf, written as a thin wrapper on top
of libgq-gconf (see http://maemo.org/packages/view/libgq-gconf0/).

%package -n %{libname}
Summary:	Qt binding and QML plugin for GConf - shared libraries
Group:		System/Libraries

%description -n %{libname}
Simple Qt binding and QML plugin for GConf, written as a thin wrapper on top
of libgq-gconf (see http://maemo.org/packages/view/libgq-gconf0/).

%package -n %{develname}
Summary:	Qt binding and QML plugin for GConf - development files
Group:		Development/C++
Requires:	%{libname} = %{version}

%description -n %{develname}
Simple Qt binding and QML plugin for GConf, written as a thin wrapper on top
of libgq-gconf (see http://maemo.org/packages/view/libgq-gconf0/).

%prep
%setup -q
%apply_patches

%build
export BUILD_GLOBAL=true
%cmake \
	-Dlibdir=%{_libdir} \

%make

%install
pushd build
# .pc file hack
sed -i 's/libdir=\${exec_prefix}\/lib/libdir=\${exec_prefix}\/%{_lib}/g' ../libqtgconf.pc
%make_install
popd build

%files -n %{libname}
%doc COPYING README
%{_libdir}/*.so.%{major}*
%{_libdir}/qt4/plugins/imports/

%files -n %{develname}
%{_includedir}/QtGConf/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libqtgconf.pc

