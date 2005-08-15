# $Rev: 3424 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xsm application
Summary(pl):	Aplikacja xsm
Name:		xorg-app-xsm
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xsm-%{version}.tar.bz2
# Source0-md5:	05ba978407eca36bb2e304c5dc56a4c9
Patch0:		xsm-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	heimdal-rsh
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRequires:	xorg-data-xbitmaps
BuildRoot:	%{tmpdir}/xsm-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xsm application.

%description -l pl
Aplikacja xsm.


%prep
%setup -q -n xsm-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_sysconfdir}/X11/app-defaults/*
%attr(755,root,wheel) %{_bindir}/*
%{_libdir}/X11/xsm/system.xsm
%{_mandir}/man1/*.1*
