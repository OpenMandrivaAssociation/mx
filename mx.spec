%define api	1.0
%define major	2
%define gtkmaj	0
%define libname	%mklibname %{name} %{api} %{major}
%define libgtk	%mklibname %{name}-gtk %{api} %{gtkmaj}
%define devname	%mklibname %{name} -d
%define devgtk	%mklibname %{name}-gtk -d
%define girname	%mklibname %{name}-gir %{api}
%define girgtk	%mklibname %{name}-gtk-gir %{api}

Summary:	User interface toolkit for the MeeGo
Name:		mx
Version:	1.4.7
Release:	3
Group:		System/Libraries
License:	LGPLv2.1
Url:		http://www.clutter-project.org/
Source0:	https://github.com/downloads/clutter-project/mx/%{name}-%{version}.tar.xz
Patch0:		mx-nogl.patch
BuildRequires:	intltool
BuildRequires:	gettext
BuildRequires:	pkgconfig(clutter-gesture)
BuildRequires:	pkgconfig(clutter-imcontext-0.1)
BuildRequires:	pkgconfig(clutter-x11-1.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)

%description
'MX' is a currently experiemental toolkit for the meego-netbook
implementation.

%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library for %{name}
Conflicts:	%{name} < %{version}-%{release}

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{libgtk}
Group:		System/Libraries
Summary:	Shared library for %{name}-gtk
Conflicts:	%{name} < %{version}-%{release}

%description -n %{libgtk}
This package contains the shared library for %{name}-gtk.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{girgtk}
Summary:	GObject Introspection interface description for %{name}-gtk
Group:		System/Libraries

%description -n %{girgtk}
GObject Introspection interface description for %{name}-gtk.

%package -n %{devname}
Summary:	MX development libraries and headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
MX development libraries and header files

%package -n %{devgtk}
Summary:	MX - Gtk development libraries and headers
Group:		Development/C
Requires:	%{libgtk} = %{version}-%{release}
Requires:	%{girgtk} = %{version}-%{release}

%description -n %{devgtk}
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
%makeinstall_std
%find_lang %{name}-%{api}

%files -f %{name}-%{api}.lang
%{_bindir}/*
%{_datadir}/mx

%files -n %{libname}
%{_libdir}/libmx-%{api}.so.%{major}*

%files -n %{libgtk}
%{_libdir}/libmx-gtk-%{api}.so.%{gtkmaj}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Mx-%{api}.typelib

%files -n %{girgtk}
%{_libdir}/girepository-1.0/MxGtk-%{api}.typelib

%files -n %{devname}
%doc COPYING.LIB
%{_includedir}/mx-%{api}/mx/*
%{_libdir}/libmx-%{api}.so
%{_libdir}/pkgconfig/mx-%{api}.pc
%{_datadir}/gtk-doc/html/mx
%{_datadir}/gir-1.0/Mx-%{api}.gir

%files -n %{devgtk}
%{_includedir}/mx-%{api}/mx-gtk*
%{_libdir}/libmx-gtk-%{api}*.so
%{_libdir}/pkgconfig/mx-gtk-%{api}.pc
%{_datadir}/gtk-doc/html/mx-gtk
%{_datadir}/gir-1.0/MxGtk-%{api}.gir

