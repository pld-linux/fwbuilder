Name:		fwbuilder
Summary:	Firewall Builder
Summary(pl):	Narzêdzie do tworzenia firewalli
URL:		http://www.fwbuilder.org/
Version:	1.0.7
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://belnet.dl.sourceforge.net/sourceforge/fwbuilder/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtkmm1-devel >= 1.2.3
BuildRequires:	imlib-devel
BuildRequires:	libfwbuilder-devel >= 0.10.11
BuildRequires:	libsigc++1-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
Requires:	libfwbuilder >= 0.10.11
Obsoletes:	fwbuilder-doc fwbuilder-devel

%define         _prefix         /usr/X11R6
%define         _mandir         %{_datadir}/man

%description
Firewall administration toolkit.

%description -l pl
Narzêdzie do tworzenia i administracji firewallami.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure2_13 \
	--enable-auto-docdir \
	--with-templatedir=%{_datadir}/fwbuilder \
	--with-iconsdir=%{_pixmapsdir}/fwbuilder/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}/fwbuilder
install src/icons/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/fwbuilder
install src/icons/host*.png $RPM_BUILD_ROOT%{_pixmapsdir}/fwbuilder

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/fwbuilder
%{_datadir}/bug-buddy/bugzilla/*
%{_datadir}/bug-buddy/xml/*
%{_datadir}/bug-buddy/*.*
%{_pixmapsdir}/fwbuilder
%{_mandir}/man1/*
