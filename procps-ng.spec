#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v2
# autospec commit: 250a666
#
Name     : procps-ng
Version  : 4.0.4
Release  : 50
URL      : https://gitlab.com/procps-ng/procps/-/archive/v4.0.4/procps-v4.0.4.tar.gz
Source0  : https://gitlab.com/procps-ng/procps/-/archive/v4.0.4/procps-v4.0.4.tar.gz
Summary  : Library to control and query process state
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0+ LGPL-2.0 LGPL-2.0+
Requires: procps-ng-bin = %{version}-%{release}
Requires: procps-ng-lib = %{version}-%{release}
Requires: procps-ng-license = %{version}-%{release}
Requires: procps-ng-locales = %{version}-%{release}
Requires: procps-ng-man = %{version}-%{release}
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : systemd-dev
BuildRequires : tcl
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Correct-ncurses.h-path.patch

%description
[![build status](https://gitlab.com/ci/projects/2142/status.png?ref=master)](https://gitlab.com/ci/projects/2142?ref=master)
procps
======

%package bin
Summary: bin components for the procps-ng package.
Group: Binaries
Requires: procps-ng-license = %{version}-%{release}

%description bin
bin components for the procps-ng package.


%package dev
Summary: dev components for the procps-ng package.
Group: Development
Requires: procps-ng-lib = %{version}-%{release}
Requires: procps-ng-bin = %{version}-%{release}
Provides: procps-ng-devel = %{version}-%{release}
Requires: procps-ng = %{version}-%{release}

%description dev
dev components for the procps-ng package.


%package doc
Summary: doc components for the procps-ng package.
Group: Documentation
Requires: procps-ng-man = %{version}-%{release}

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
Requires: procps-ng-license = %{version}-%{release}

%description lib
lib components for the procps-ng package.


%package license
Summary: license components for the procps-ng package.
Group: Default

%description license
license components for the procps-ng package.


%package locales
Summary: locales components for the procps-ng package.
Group: Default

%description locales
locales components for the procps-ng package.


%package man
Summary: man components for the procps-ng package.
Group: Default

%description man
man components for the procps-ng package.


%prep
%setup -q -n procps-v4.0.4
cd %{_builddir}/procps-v4.0.4
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698776389
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%autogen --disable-static --exec-prefix=/ \
--enable-watch8bit \
--with-systemd
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check ||:

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffunction-sections -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1698776389
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/procps-ng
cp %{_builddir}/procps-v%{version}/COPYING %{buildroot}/usr/share/package-licenses/procps-ng/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/procps-v%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/procps-ng/3cc956929ff9e4c1c89a2c826cdc7fec5e0b21ab || :
cp %{_builddir}/procps-v%{version}/library/COPYING %{buildroot}/usr/share/package-licenses/procps-ng/3cc956929ff9e4c1c89a2c826cdc7fec5e0b21ab || :
cp %{_builddir}/procps-v%{version}/src/ps/COPYING %{buildroot}/usr/share/package-licenses/procps-ng/3cc956929ff9e4c1c89a2c826cdc7fec5e0b21ab || :
%make_install
%find_lang procps-ng
## Remove excluded files
rm -f %{buildroot}*/usr/bin/uptime
rm -f %{buildroot}*/usr/share/man/man1/uptime.1
## install_append content
mv %{buildroot}/usr/bin/top %{buildroot}/usr/bin/top2
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/free
/usr/bin/kill
/usr/bin/pgrep
/usr/bin/pidof
/usr/bin/pidwait
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
/usr/include/libproc2/diskstats.h
/usr/include/libproc2/meminfo.h
/usr/include/libproc2/misc.h
/usr/include/libproc2/pids.h
/usr/include/libproc2/slabinfo.h
/usr/include/libproc2/stat.h
/usr/include/libproc2/vmstat.h
/usr/include/libproc2/xtra-procps-debug.h
/usr/lib64/libproc2.so
/usr/lib64/pkgconfig/libproc2.pc
/usr/share/man/man3/procps.3
/usr/share/man/man3/procps_misc.3
/usr/share/man/man3/procps_pids.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/procps\-ng/*

%files extras
%defattr(-,root,root,-)
/usr/bin/slabtop

%files lib
%defattr(-,root,root,-)
/usr/lib64/libproc2.so.0
/usr/lib64/libproc2.so.0.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/procps-ng/3cc956929ff9e4c1c89a2c826cdc7fec5e0b21ab
/usr/share/package-licenses/procps-ng/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/free.1
/usr/share/man/man1/kill.1
/usr/share/man/man1/pgrep.1
/usr/share/man/man1/pidof.1
/usr/share/man/man1/pidwait.1
/usr/share/man/man1/pkill.1
/usr/share/man/man1/pmap.1
/usr/share/man/man1/ps.1
/usr/share/man/man1/pwdx.1
/usr/share/man/man1/slabtop.1
/usr/share/man/man1/tload.1
/usr/share/man/man1/top.1
/usr/share/man/man1/w.1
/usr/share/man/man1/watch.1
/usr/share/man/man5/sysctl.conf.5
/usr/share/man/man8/sysctl.8
/usr/share/man/man8/vmstat.8

%files locales -f procps-ng.lang
%defattr(-,root,root,-)

