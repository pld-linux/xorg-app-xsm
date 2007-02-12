Summary:	xsm application
Summary(pl.UTF-8):   Aplikacja xsm
Name:		xorg-app-xsm
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xsm-%{version}.tar.bz2
# Source0-md5:	cce867ff7d0df9c0b9e682591779952c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xsm application.

%description -l pl.UTF-8
Aplikacja xsm.

%prep
%setup -q -n xsm-%{version}

sed -i -e '/^RSH=$/d' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	RSH=/usr/bin/rsh

%{__make} \
	SYSTEM_INIT_DIR=/etc/X11/xsm

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SYSTEM_INIT_DIR=/etc/X11/xsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xsm
%{_datadir}/X11/app-defaults/XSm
%dir /etc/X11/xsm
%config(noreplace) %verify(not md5 mtime size) /etc/X11/xsm/system.xsm
%{_mandir}/man1/xsm.1x*
