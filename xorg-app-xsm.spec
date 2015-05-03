Summary:	xsm application - X Session Manager
Summary(pl.UTF-8):	Aplikacja xsm - zarządca sesji X
Name:		xorg-app-xsm
Version:	1.0.3
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xsm-%{version}.tar.bz2
# Source0-md5:	2a9818eba05556e6e99be87d9b3974c4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.99
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXt >= 1.0.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xsm application is a session manager. A session is a group of
applications, each of which has a particular state. xsm allows you to
create arbitrary sessions - for example, you might have a "light"
session, a "development" session, or an "xterminal" session. Each
session can have its own set of applications. Within a session, you
can perform a "checkpoint" to save application state, or a "shutdown"
to save state and exit the session. When you log back in to the
system, you can load a specific session, and you can delete sessions
you no longer want to keep.

%description -l pl.UTF-8
Aplikacja xsm to zarządca sesji. Sesja to grupa aplikacji, z których
każda jest w jakimś stanie. xsm pozwala tworzyć dowolne sesje - np.
można mieć sesję "light", "development" i "xterminal". Każda sesja
może mieć własny zbiór aplikacji. W ramach sesji można wykonać
operację "checkpoint" w celu zapisania stanu aplikacji lub "shutdown",
aby zapisać stan i zakończyć sesję. Po ponownym zalogowaniu do systemu
można wczytać określoną sesję; można także usunąć sesje już
niepotrzebne.

%prep
%setup -q -n xsm-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-rsh=/usr/bin/ssh

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xsm
%{_datadir}/X11/app-defaults/XSm
%dir /etc/X11/xsm
%config(noreplace) %verify(not md5 mtime size) /etc/X11/xsm/system.xsm
%{_mandir}/man1/xsm.1*
