Name:		fwbuilder
Summary:	Firewall Builder
Summary(pl):	Narzêdzie do tworzenia firewalli
Url:		http://www.fwbuilder.org/
Version:	1.0.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://belnet.dl.sourceforge.net/sourceforge/fwbuilder/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtkmm-devel >= 1.2.3
BuildRequires:	imlib-devel
BuildRequires:	libfwbuilder-devel >= 0.10.4
BuildRequires:	libsigc++1-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
Obsoletes:	fwbuilder-doc fwbuilder-devel

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
Firewall administration toolkit.

%description -l pl
Narzêdzie do tworzenia i administracji firewallami.

%package compiler
Summary:	compiler libraries for Firewall Builder
Summary(pl):	Biblioteki dla Firewall Buildera.
Group:		Applications/System
Requires:	%{name} = %{version}

%description compiler
Compiler libraries for Firewall Builder.

%description compiler -l pl
Biblioteki dla Firewall Buildera.

%package iptables
Summary:	iptables compiler for Firewall Builder
Summary(pl):	Kompilator iptables dla Firewall Buildera.
Group:		Applications/System
Requires:	%{name} = %{version}

%description iptables
iptables compiler for Firewall Builder.

%description iptables -l pl
Kompilator iptables dla Firewall Buildera.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/fwbuilder
%{_datadir}/bug-buddy/bugzilla/*
%{_datadir}/bug-buddy/xml/*
%{_datadir}/bug-buddy/*.*
%{_pixmapsdir}/fwbuilder

%files compiler
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_includedir}/*.h

%files iptables
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_iptables
