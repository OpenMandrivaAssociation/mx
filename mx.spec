Name: mx
Summary: User interface toolkit for the MeeGo
Version: 1.1.0
Release: %mkrel 1
Group: Development/Library
License: LGPLv2.1
URL: http://www.meego.com
Source0: %{name}-%{version}.tar.gz
Patch0: %{name}-1.1.0-enable-deprecated.patch
BuildRequires: libclutter1.0-devel
BuildRequires: libgtk+2-devel
BuildRequires: libstartup-notification-1-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libgladeui-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gir-repository

%description
'MX' is a currently experiemental toolkit for the meego-netbook
implementation.


%package doc
Summary: MX documentation
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for MX

%package devel
Summary: MX development libraries and headers
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
MX development libraries and header files

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .enable-deprecated

%build
autoreconf --install
%configure2_5x \
  --disable-static \
  --enable-gtk-doc \
  --without-clutter-gesture \
  --with-glade

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang mx-1.0

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f mx-1.0.lang
%defattr(-,root,root,-)
%doc COPYING.LIB
%{_libdir}/libmx*.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_datadir}/mx
%{_bindir}


%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/mx

%files devel
%defattr(-,root,root,-)
%{_includedir}/mx-1.0/*
%{_libdir}/libmx*.so
%{_libdir}/libmx*.la
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/glade3/catalogs/*.xml

