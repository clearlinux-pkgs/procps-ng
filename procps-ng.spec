#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : procps-ng
Version  : 3.3.12
Release  : 38
URL      : http://downloads.sourceforge.net/procps-ng/procps-ng-3.3.12.tar.xz
Source0  : http://downloads.sourceforge.net/procps-ng/procps-ng-3.3.12.tar.xz
Summary  : Library to control and query process state
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0+ LGPL-2.0 LGPL-2.0+
Requires: procps-ng-bin
Requires: procps-ng-lib
Requires: procps-ng-doc
Requires: procps-ng-locales
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : ncurses-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : systemd-dev
BuildRequires : tcl
Patch1: 0001-watch-Use-real-ncurses-header.patch
Patch2: tinfow.patch
Patch3: break.patch

%description
How to use check suite
----------------------
You need DejaGNU package.  Assuming you have it all you need to do is

%package bin
Summary: bin components for the procps-ng package.
Group: Binaries

%description bin
bin components for the procps-ng package.


%package dev
Summary: dev components for the procps-ng package.
Group: Development
Requires: procps-ng-lib
Requires: procps-ng-bin
Provides: procps-ng-devel

%description dev
dev components for the procps-ng package.


%package doc
Summary: doc components for the procps-ng package.
Group: Documentation

%description doc
doc components for the procps-ng package.


%package extras
Summary: extras components for the procps-ng package.
Group: Default

%description extras
extras components for the procps-ng package.


%package lib
Summary: lib components for the procps-ng package.
Group: Libraries

%description lib
lib components for the procps-ng package.


%package locales
Summary: locales components for the procps-ng package.
Group: Default

%description locales
locales components for the procps-ng package.


%prep
%setup -q -n procps-ng-3.3.12
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506458533
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%reconfigure --disable-static --exec-prefix=/ --enable-watch8bit --with-systemd
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check ||:

%install
export SOURCE_DATE_EPOCH=1506458533
rm -rf %{buildroot}
%make_install
%find_lang procps-ng
## make_install_append content
mv %{buildroot}/usr/bin/top %{buildroot}/usr/bin/top2
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/slabtop
%exclude /usr/bin/uptime
/usr/bin/free
/usr/bin/kill
/usr/bin/pgrep
/usr/bin/pidof
/usr/bin/pkill
/usr/bin/pmap
/usr/bin/ps
/usr/bin/pwdx
/usr/bin/sysctl
/usr/bin/tload
/usr/bin/top2
/usr/bin/vmstat
/usr/bin/w
/usr/bin/watch

%files dev
%defattr(-,root,root,-)
/usr/include/proc/alloc.h
/usr/include/proc/devname.h
/usr/include/proc/escape.h
/usr/include/proc/procps.h
/usr/include/proc/pwcache.h
/usr/include/proc/readproc.h
/usr/include/proc/sig.h
/usr/include/proc/slab.h
/usr/include/proc/sysinfo.h
/usr/include/proc/version.h
/usr/include/proc/wchan.h
/usr/include/proc/whattime.h
/usr/lib64/libprocps.so
/usr/lib64/pkgconfig/libprocps.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/procps\-ng/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
%exclude /usr/share/man/man1/uptime.1

%files extras
%defattr(-,root,root,-)
/usr/bin/slabtop

%files lib
%defattr(-,root,root,-)
/usr/lib64/libprocps.so.6
/usr/lib64/libprocps.so.6.0.0

%files locales -f procps-ng.lang
%defattr(-,root,root,-)

