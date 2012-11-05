Name:           enchant
Version:        1.6.0
Release:        6
License:        LGPL-2.1+
Summary:        Generic Spell Checking Library
Url:            http://www.abisource.com/
Group:          Productivity/Text/Spell
Source:         %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  aspell-devel
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)

%description
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

%package tools
License:        LGPL-2.1+
Summary:        Generic Spell Checking Library - Command Line Tools
Group:          Productivity/Text/Spell

%description tools
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

This package provides command-line tools to interact with enchant.

%package zemberek
License:        LGPL-2.1+
Summary:        Generic Spell Checking Library - Zemberek Plugin
Group:          Productivity/Text/Spell
# Only zemberek-server over D-Bus is supported. Server must be installed locally:
Recommends:     zemberek-server
Supplements:    packageand(libenchant:zemberek-server)
Provides:       locale(%{name}:az)
Provides:       locale(%{name}:tk)
Provides:       locale(%{name}:tr)
Provides:       locale(%{name}:tt)

%description zemberek
Zemberek plugin (Azeri, Turkmen, Turkish, Tatar) for enchant, a library
providing an efficient extensible abstraction for dealing with
different spell checking libraries.

%package -n libenchant
License:        LGPL-2.1+
Summary:        Generic Spell Checking Library
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libenchant
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

%package devel
License:        LGPL-2.1+
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libstdc++-devel
Requires:       pkgconfig(glib-2.0)

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q

%build
%configure --with-pic \
    --disable-static \
    --enable-zemberek \
    --with-myspell-dir=%{_datadir}/myspell \
    --disable-voikko

make %{?_smp_mflags}

%install
%make_install

%post -n libenchant -p /sbin/ldconfig

%postun -n libenchant -p /sbin/ldconfig

%files tools
%defattr(-,root,root)
%{_bindir}/enchant
%{_bindir}/enchant-lsmod
%doc %{_mandir}/man1/enchant.1*

%files zemberek
%defattr(-,root,root)
%{_libdir}/enchant/libenchant_zemberek.so

%files -n libenchant
%defattr(-,root,root)
%doc COPYING.LIB
%{_libdir}/*.so.*
# The directories are not versioned, unfortunately. Not good for the SLPP.
%{_datadir}/enchant
%dir %{_libdir}/enchant
%{_libdir}/enchant/libenchant_aspell.so
%{_libdir}/enchant/libenchant_ispell.so
%{_libdir}/enchant/libenchant_myspell.so

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
