Summary:	Firewall Builder
Summary(pl):	Narzêdzie do tworzenia firewalli
Name:		fwbuilder
Version:	1.0.11
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	03f013f0f02472c91845e3d6fd50720a
Patch0:		%{name}-modulesdir.patch
URL:		http://www.fwbuilder.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtkmm1-devel >= 1.2.3
BuildRequires:	imlib-devel
BuildRequires:	libfwbuilder-devel >= 1.0.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
Requires:	libfwbuilder >= 1.0.1
Obsoletes:	fwbuilder-doc
Obsoletes:	fwbuilder-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firewall administration toolkit.

%description -l pl
Narzêdzie do tworzenia i administracji firewallami.

%package install
Summary:	Install script for Firewall Builder rules
Summary(pl):	Skrypt instaluj±cy regu³ki tworzone przez Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}

%description install
Install script for Firewall Builder rules.

%description install -l pl
Skrypt instaluj±cy regu³ki tworzone przez Firewall Buildera.

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

%package compiler-freebsd-ipfw
Summary:	FreeBSD ipfw compiler for Firewall Builder
Summary(pl):	Kompilator FreeBSD ipfw dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}

%description compiler-freebsd-ipfw
FreeBSD ipfw compiler for Firewall Builder.

%description compiler-freebsd-ipfw -l pl
Kompilator FreeBSD ipfw dla Firewall Buildera.

%package platform-linux24
Summary:	Linux 2.4 specific files
Summary(pl):	Pliki specyficzne dla Linuksa 2.4
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-linux24
Linux 2.4 specific files.

%description platform-linux24 -l pl
Pliki specyficzne dla Linuksa 2.4.

%package platform-freebsd
Summary:	FreeBSD specific files
Summary(pl):	Pliki specyficzne dla FreeBSD
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-freebsd
FreeBSD specific files.

%description platform-freebsd -l pl
Pliki specyficzne dla FreeBSD.

%package platform-openbsd
Summary:	OpenBSD specific files
Summary(pl):	Pliki specyficzne dla OpenBSD
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-openbsd
OpenBSD specific files.

%description platform-openbsd -l pl
Pliki specyficzne dla OpenBSD.

%package platform-cisco-pix
Summary:	Cisco PIX specific files
Summary(pl):	Pliki specyficzne dla Cisco PIX
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-cisco-pix
Cisco PIX specific files.

%description platform-cisco-pix -l pl
Pliki specyficzne dla Cisci PIX.

%package platform-solaris
Summary:	Solaris specific files
Summary(pl):	Pliki specyficzne dla Solarisa
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-solaris
Solaris specific files.

%description platform-solaris -l pl
Pliki specyficzne dla Solarisa.

%package platform-macosx
Summary:	MacOS X specific files
Summary(pl):	Pliki specyficzne dla MacOS X
Group:		Applications/System
Requires:	%{name} = %{version}

%description platform-macosx
MacOS X specific files.

%description platform-macosx -l pl
Pliki specyficzne dla MacOS X.

%prep
%setup -q
%patch -p1

# don't call autoheader, it would destroy important parts of config.h
echo '#undef MODULES_DIR' >> config.h.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-auto-docdir \
	--disable-static \
	--with-templatedir=%{_datadir}/fwbuilder \
	--with-iconsdir=%{_pixmapsdir}/fwbuilder

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
%doc doc/AUTHORS doc/ChangeLog doc/Credits doc/NEWS doc/README* doc/TODO
%doc doc/examples doc/testing_new_compiler
%doc doc/*.html
%attr(755,root,root) %{_bindir}/fwbuilder
%attr(755,root,root) %{_bindir}/fwblookup
%attr(755,root,root) %{_bindir}/fwb_compile_all
%attr(755,root,root) %{_bindir}/fwbedit
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/gui
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/platform
%dir %{_datadir}/%{name}/os
%{_datadir}/%{name}/*.*
%{_datadir}/%{name}/gtkrc
%{_datadir}/%{name}/migration
%{_datadir}/%{name}/filters
%{_datadir}/%{name}/os/unknown_os.xml
%{_datadir}/%{name}/platform/unknown.xml
%{_datadir}/bug-buddy/bugzilla/*
%{_datadir}/bug-buddy/xml/*
%{_datadir}/bug-buddy/fwbuilder*
%{_pixmapsdir}/%{name}
%{_mandir}/man1/fwbuilder*
%{_mandir}/man1/fwblookup*
%{_mandir}/man1/fwb_compile_all*
%{_mandir}/man1/fwbedit*

%files install
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_install
%{_mandir}/man1/fwb_install*

%files compiler-iptables
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_ipt
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_iptables_dlg.so
%{_datadir}/%{name}/platform/iptables.xml
%{_mandir}/man1/fwb_ipt*

%files compiler-ipfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_ipf
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_ipf_dlg.so
%{_datadir}/%{name}/platform/ipf.xml
%{_mandir}/man1/fwb_ipf*

%files compiler-openbsd-pf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_pf
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_pf_dlg.so
%{_datadir}/%{name}/platform/pf.xml
%{_mandir}/man1/fwb_pf*

%files compiler-cisco-pix
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/fwb_pix
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_pix_dlg.so
%{_datadir}/%{name}/platform/pix.xml
#%%{_mandir}/man1/fwb_pix*

%files compiler-freebsd-ipfw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_ipfw
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_ipfw_dlg.so
%{_datadir}/%{name}/platform/ipfw.xml

%files platform-linux24
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_linux24_dlg.so
%{_datadir}/%{name}/os/linux24.xml

%files platform-freebsd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_freebsd_dlg.so
%{_datadir}/%{name}/os/freebsd.xml

%files platform-openbsd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_openbsd_dlg.so
%{_datadir}/%{name}/os/openbsd.xml

%files platform-cisco-pix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_pix_os_dlg.so
%{_datadir}/%{name}/os/pix_os.xml

%files platform-solaris
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_solaris_dlg.so
%{_datadir}/%{name}/os/solaris.xml

%files platform-macosx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/modules/gui/lib_macosx_dlg.so
%{_datadir}/%{name}/os/macosx.xml
