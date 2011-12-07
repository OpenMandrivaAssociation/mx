%define api			1.0
%define major		2
%define gtk_major	0
%define gir_major	1.0

%define libname		%mklibname %{name} %{major}
%define libgtk		%mklibname %{name}-gtk %{gtk_major}
%define develname	%mklibname %{name} -d
%define develgtk	%mklibname %{name}-gtk -d
%define girname		%mklibname %{name}-gir %{gir_major}
%define girgtk		%mklibname %{name}-gtk-gir %{gir_major}

Name: mx
Summary: User interface toolkit for the MeeGo
Version: 1.4.1
Release: 1
Group: System/Libraries
License: LGPLv2.1
URL: http://www.clutter-project.org/
Source0: http://source.clutter-project.org/sources/mx/1.4/%{name}-%{version}.tar.xz
#Patch0: %{name}-1.1.0-enable-deprecated.patch
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: pkgconfig(clutter-gesture)
BuildRequires: pkgconfig(clutter-imcontext-0.1)
BuildRequires: pkgconfig(clutter-x11-1.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)

%description
'MX' is a currently experiemental toolkit for the meego-netbook
implementation.

%package -n %{libname}
Group: System/Libraries
Summary: Shared library for %{name}
Conflicts: %{name} < %{version}-%{release}

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{libgtk}
Group: System/Libraries
Summary: Shared library for %{name}-gtk
Conflicts: %{name} < %{version}-%{release}

%description -n %{libgtk}
This package contains the shared library for %{name}-gtk.

%package -n %{girname}
Summary: GObject Introspection interface description for %{name}
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{girgtk}
Summary: GObject Introspection interface description for %{name}-gtk
Group: System/Libraries
Requires: %{libgtk} = %{version}-%{release}

%description -n %{girgtk}
GObject Introspection interface description for %{name}-gtk.

%package -n %{develname}
Summary: MX development libraries and headers
Group: Development/C
Requires: %{libname} = %{version}-%{release}
%rename %{name}-doc
Obsoletes: %{name}-devel

%description -n %{develname}
MX development libraries and header files

%package -n %{develgtk}
Summary: MX - Gtk development libraries and headers
Group: Development/C
Requires: %{libgtk} = %{version}-%{release}

%description -n %{develgtk}
MX - Gtk development libraries and header files

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-introspection

%make LIBS='-lm'

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang mx-1.0

%files -f mx-1.0.lang
%doc COPYING.LIB
%{_bindir}
%{_datadir}/mx

%files -n %{libname}
%{_libdir}/libmx-%{api}.so.%{major}*

%files -n %{libgtk}
%{_libdir}/libmx-gtk-%{api}.so.%{gtk_major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Mx-%{api}.typelib

%files -n %{girgtk}
%{_libdir}/girepository-1.0/MxGtk-%{gir_major}.typelib

%files -n %{develname}
%{_includedir}/mx-1.0/mx/*
%{_libdir}/libmx-%{api}.so
%{_libdir}/pkgconfig/mx-%{api}.pc
%{_datadir}/gtk-doc/html/mx
%{_datadir}/gir-1.0/Mx-%{gir_major}.gir

%files -n %{develgtk}
%{_includedir}/mx-1.0/mx-gtk*
%{_libdir}/libmx-gtk-%{api}*.so
%{_libdir}/pkgconfig/mx-gtk-%{api}.pc
%{_datadir}/gtk-doc/html/mx-gtk
%{_datadir}/gir-1.0/MxGtk-%{gir_major}.gir

