Name:		fwbuilder
Summary:	Firewall Builder
Summary(pl):	Narzêdzie do tworzenia firewalli
URL:		http://www.fwbuilder.org/
Version:	1.0.8
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://belnet.dl.sourceforge.net/sourceforge/fwbuilder/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtkmm-devel >= 1.2.3
BuildRequires:	imlib-devel
BuildRequires:	libfwbuilder-devel >= 0.10.12
BuildRequires:	libsigc++-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
Requires:	libfwbuilder >= 0.10.12
Obsoletes:	fwbuilder-doc fwbuilder-devel


%description
Firewall administration toolkit.

%description -l pl
Narzêdzie do tworzenia i administracji firewallami.


%package install
Summary:	Install script for Firewall Builder rules.
Summary(pl):	Skrypt instalujacy regulki tworzone przez Firewall Buildera.
Group:		Applications/System
Requires:	%{name} = %{version}

%description install
Install script for Firewall Builder rules.

%description install -l pl
Skrypt instalujacy regulki tworzone przez Firewall Buildera.


%package devel
Summary:	Firewall Builder development files.
Group:		Applications/System
Requires:	%{name} = %{version}

%description devel
Firewall Builder development files.


%package static
Summary:	Firewall Builder static libraries.
Group:		Applications/System
Requires:	%{name} = %{version}

%description static
Firewall Builder static libraries.


%package compiler-ipfilter
Summary:	ipfilter compiler for Firewall Builder
Summary(pl):	Kompilator ipfilter dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}

%description compiler-ipfilter
ipfilter compiler for Firewall Builder.

%description compiler-ipfilter -l pl
Kompilator ipfilter dla Firewall Buildera.


%package compiler-iptables
Summary:	iptables compiler for Firewall Builder
Summary(pl):	Kompilator iptables dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}

%description compiler-iptables
iptables compiler for Firewall Builder.

%description compiler-iptables -l pl
Kompilator iptables dla Firewall Buildera.


%package compiler-openbsd-pf
Summary:	OpenBSD pf compiler for Firewall Builder
Summary(pl):	Kompilator OpenBSD pf dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}

%description compiler-openbsd-pf
OpenBSD pf compiler for Firewall Builder.

%description compiler-openbsd-pf -l pl
Kompilator OpenBSD pf dla Firewall Buildera.


%package compiler-cisco-pix
Summary:	Cisco PIX compiler for Firewall Builder
Summary(pl):	Kompilator Cisco PIX dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}

%description compiler-cisco-pix
Cisco PIX compiler for Firewall Builder.

%description compiler-cisco-pix -l pl
Kompilator Cisco PIX dla Firewall Buildera.


%package platform-linux24
Summary:	Linux 2.4 specific files.
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-linux24
Linux 2.4 specific files.


%package platform-freebsd
Summary:	FreeBSD specific files.
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-freebsd
FreeBSD specific files.


%package platform-openbsd
Summary:	OpenBSD specific files.
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-openbsd
OpenBSD specific files.


%package platform-cisco-pix
Summary:	Cisco PIX specific files.
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-cisco-pix
Cisco PIX specific files.


%package platform-solaris
Summary:	Solaris specific files.
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-solaris
Solaris specific files.


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
%attr(755,root,root) %{_bindir}/fwbuilder
%attr(755,root,root) %{_bindir}/fwblookup
%{_datadir}/fwbuilder/*.*
%{_datadir}/fwbuilder/gtkrc
%{_datadir}/fwbuilder/migration
%{_datadir}/fwbuilder/filters
%{_datadir}/fwbuilder/os/unknown_os.xml
%{_datadir}/fwbuilder/platform/unknown.xml
%{_datadir}/bug-buddy/bugzilla/*
%{_datadir}/bug-buddy/xml/*
%{_datadir}/bug-buddy/fwbuilder*
%{_pixmapsdir}/fwbuilder
%{_mandir}/man1/fwbuilder*
%{_mandir}/man1/fwblookup*

%files devel
%defattr(644,root,root,755)
%{_datadir}/fwbuilder/modules/gui/*.la

%files static
%defattr(644,root,root,755)
%{_datadir}/fwbuilder/modules/gui/*.a

%files install
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_install

%files compiler-iptables
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_ipt
%attr(755,root,root) %{_datadir}/fwbuilder/modules/gui/lib_iptables_dlg.so
%{_datadir}/fwbuilder/platform/iptables.xml
%{_mandir}/man1/fwb_ipt*

%files compiler-ipfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_ipf
%attr(755,root,root) %{_datadir}/fwbuilder/modules/gui/lib_ipf_dlg.so
%{_datadir}/fwbuilder/platform/ipf.xml
%{_mandir}/man1/fwb_ipf*

%files compiler-openbsd-pf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_pf
%attr(755,root,root) %{_datadir}/fwbuilder/modules/gui/lib_pf_dlg.so
%{_datadir}/fwbuilder/platform/pf.xml
%{_mandir}/man1/fwb_pf*

%files compiler-cisco-pix
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/fwb_pix
%attr(755,root,root) %{_datadir}/fwbuilder/modules/gui/lib_pix_dlg.so
%{_datadir}/fwbuilder/platform/pix.xml
#%%{_mandir}/man1/fwb_pix*

%files platform-linux24
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/fwbuilder/modules/gui/lib_linux24_dlg.so
%{_datadir}/fwbuilder/os/linux24.xml

%files platform-freebsd
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/fwbuilder/modules/gui/lib_freebsd_dlg.so
%{_datadir}/fwbuilder/os/freebsd.xml

%files platform-openbsd
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/fwbuilder/modules/gui/lib_openbsd_dlg.so
%{_datadir}/fwbuilder/os/openbsd.xml

%files platform-cisco-pix
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/fwbuilder/modules/gui/lib_pix_os_dlg.so
%{_datadir}/fwbuilder/os/pix_os.xml

%files platform-solaris
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/fwbuilder/modules/gui/lib_solaris_dlg.so
%{_datadir}/fwbuilder/os/solaris.xml
