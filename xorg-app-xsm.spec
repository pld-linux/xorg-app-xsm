Summary:	xsm application
Summary(pl):	Aplikacja xsm
Name:		xorg-app-xsm
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/xsm-%{version}.tar.bz2
# Source0-md5:	8c5b2229fa8e270e5c5bcfe09d477877
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xsm application.

%description -l pl
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

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appmandir=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/*
%{_libdir}/X11/xsm
%{_mandir}/man1/*.1x*
