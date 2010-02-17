#
%define		_majver		3
%define		_minver		0
Summary:	Firewall Builder
Summary(pl.UTF-8):   Narzędzie do tworzenia firewalli
Name:		fwbuilder
Version:	%{_majver}.%{_minver}.5
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fwbuilder/%{name}-%{version}.tar.gz
# Source0-md5:	d4d914882a215e6d651dc7094ea88a36
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-configure.patch
Patch1:		%{name}-c++.patch
Patch2:		%{name}-dont-mess-with-compiler-names-and-ccache.patch
URL:		http://www.fwbuilder.org/
BuildRequires:	antlr = 2.7.7
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libfwbuilder-devel = %{version}
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	QtCore-devel >= 4.3
BuildRequires:	QtGui-devel >= 4.3
BuildRequires:	QtNetwork-devel >= 4.3
Requires:	libfwbuilder = %{version}
Obsoletes:	fwbuilder-doc
Obsoletes:	fwbuilder-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firewall administration toolkit.

%description -l pl.UTF-8
Narzędzie do tworzenia i administracji firewallami.

#%package install
#Summary:	Install script for Firewall Builder rules
#Summary(pl.UTF-8):   Skrypt instalujący regułki tworzone przez Firewall Buildera
#Group:		Applications/System
#Requires:	%{name} = %{version}-%{release}

#%description install
#Install script for Firewall Builder rules.

#%description install -l pl.UTF-8
#Skrypt instalujący regułki tworzone przez Firewall Buildera.

%package compiler-ipfilter
Summary:	ipfilter compiler for Firewall Builder
Summary(pl.UTF-8):   Kompilator ipfilter dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-ipfilter
ipfilter compiler for Firewall Builder.

%description compiler-ipfilter -l pl.UTF-8
Kompilator ipfilter dla Firewall Buildera.

%package compiler-iptables
Summary:	iptables compiler for Firewall Builder
Summary(pl.UTF-8):   Kompilator iptables dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-iptables
iptables compiler for Firewall Builder.

%description compiler-iptables -l pl.UTF-8
Kompilator iptables dla Firewall Buildera.

%package compiler-openbsd-pf
Summary:	OpenBSD pf compiler for Firewall Builder
Summary(pl.UTF-8):   Kompilator OpenBSD pf dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-openbsd-pf
OpenBSD pf compiler for Firewall Builder.

%description compiler-openbsd-pf -l pl.UTF-8
Kompilator OpenBSD pf dla Firewall Buildera.

%package compiler-cisco-fwsm
Summary:	Cisco FWSM compiler for Firewall Builder
Summary(pl.UTF-8):   Kompilator Cisco FWSM dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-cisco-fwsm
Cisco FWSM compiler for Firewall Builder.

%description compiler-cisco-fwsm -l pl.UTF-8
Kompilator Cisco FWSM dla Firewall Buildera.

%package compiler-cisco-iosacl
Summary:	Cisco IOSACL compiler for Firewall Builder
Summary(pl.UTF-8):   Kompilator Cisco IOSACL dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-cisco-iosacl
Cisco FWSM compiler for Firewall Builder.

%description compiler-cisco-iosacl -l pl.UTF-8
Kompilator Cisco IOSACL dla Firewall Buildera.

%package compiler-cisco-pix
Summary:	Cisco PIX compiler for Firewall Builder
Summary(pl.UTF-8):   Kompilator Cisco PIX dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-cisco-pix
Cisco PIX compiler for Firewall Builder.

%description compiler-cisco-pix -l pl.UTF-8
Kompilator Cisco PIX dla Firewall Buildera.

%package compiler-freebsd-ipfw
Summary:	FreeBSD ipfw compiler for Firewall Builder
Summary(pl.UTF-8):   Kompilator FreeBSD ipfw dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-freebsd-ipfw
FreeBSD ipfw compiler for Firewall Builder.

%description compiler-freebsd-ipfw -l pl.UTF-8
Kompilator FreeBSD ipfw dla Firewall Buildera.

%package platform-linux24
Summary:	Linux 2.4 specific files
Summary(pl.UTF-8):   Pliki specyficzne dla Linuksa 2.4
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-linux24
Linux 2.4 specific files.

%description platform-linux24 -l pl.UTF-8
Pliki specyficzne dla Linuksa 2.4.

%package platform-freebsd
Summary:	FreeBSD specific files
Summary(pl.UTF-8):   Pliki specyficzne dla FreeBSD
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-freebsd
FreeBSD specific files.

%description platform-freebsd -l pl.UTF-8
Pliki specyficzne dla FreeBSD.

%package platform-openbsd
Summary:	OpenBSD specific files
Summary(pl.UTF-8):   Pliki specyficzne dla OpenBSD
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-openbsd
OpenBSD specific files.

%description platform-openbsd -l pl.UTF-8
Pliki specyficzne dla OpenBSD.

%package platform-cisco-fwsm
Summary:	Cisco PIX specific files
Summary(pl.UTF-8):   Pliki specyficzne dla Cisco FWSM
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-cisco-fwsm
Cisco FWSM specific files.

%description platform-cisco-fwsm -l pl.UTF-8
Pliki specyficzne dla Cisci FWSM.

%package platform-cisco-pix
Summary:	Cisco PIX specific files
Summary(pl.UTF-8):   Pliki specyficzne dla Cisco PIX
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-cisco-pix
Cisco PIX specific files.

%description platform-cisco-pix -l pl.UTF-8
Pliki specyficzne dla Cisci PIX.

%package platform-solaris
Summary:	Solaris specific files
Summary(pl.UTF-8):   Pliki specyficzne dla Solarisa
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-solaris
Solaris specific files.

%description platform-solaris -l pl.UTF-8
Pliki specyficzne dla Solarisa.

%package platform-macosx
Summary:	MacOS X specific files
Summary(pl.UTF-8):   Pliki specyficzne dla MacOS X
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-macosx
MacOS X specific files.

%description platform-macosx -l pl.UTF-8
Pliki specyficzne dla MacOS X.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1

%build
export QTDIR="%{_usr}"
export QMAKESPEC="%{_datadir}/qt4/mkspecs/linux-g++"

cp -f /usr/share/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure \
	--with-templatedir=%{_datadir}/fwbuilder \
	--with-qmake=qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

export QTDIR="%{_usr}"
export QMAKESPEC="%{_datadir}/qt/mkspecs/linux-g++"

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

# drop 512x512 icon
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/hicolor/512x512

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,ChangeLog,Credits,README*,*.html}
%attr(755,root,root) %{_bindir}/fwb_compile_all
%attr(755,root,root) %{_bindir}/fwbedit
#%attr(755,root,root) %{_bindir}/fwblookup
%attr(755,root,root) %{_bindir}/fwbuilder
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.xml
%dir %{_datadir}/%{name}/locale
#%lang(de) %{_datadir}/%{name}/locale/fwbuilder_de.qm
#%lang(es) %{_datadir}/%{name}/locale/fwbuilder_es.qm
#%lang(fr) %{_datadir}/%{name}/locale/fwbuilder_fr.qm
%lang(ja) %{_datadir}/%{name}/locale/fwbuilder_ja.qm
#%lang(pt_BR) %{_datadir}/%{name}/locale/fwbuilder_pt_BR.qm
%lang(ru) %{_datadir}/%{name}/locale/fwbuilder_ru.qm
#%lang(sv) %{_datadir}/%{name}/locale/fwbuilder_sv.qm
%dir %{_datadir}/%{name}/os
%{_datadir}/%{name}/os/linksys.xml
%{_datadir}/%{name}/os/unknown_os.xml
%dir %{_datadir}/%{name}/platform
%{_datadir}/%{name}/platform/unknown.xml
%{_datadir}/%{name}/os/ios.xml
%{_datadir}/%{name}/platform/iosacl.xml
%{_desktopdir}/fwbuilder.desktop
%{_mandir}/man1/fwbuilder*
#%{_mandir}/man1/fwblookup*
%{_mandir}/man1/fwb_compile_all*
%{_mandir}/man1/fwbedit*
%{_pixmapsdir}/fwbuilder.png
%{_iconsdir}/hicolor/*/apps/fwbuilder.png

#%files install
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/fwb_install
#%{_mandir}/man1/fwb_install*

%files compiler-iptables
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_ipt
%{_datadir}/%{name}/platform/iptables.xml
%{_mandir}/man1/fwb_ipt.1*

%files compiler-ipfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_ipf
%{_datadir}/%{name}/platform/ipf.xml
%{_mandir}/man1/fwb_ipf.1*

%files compiler-openbsd-pf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_pf
%{_datadir}/%{name}/platform/pf.xml
%{_mandir}/man1/fwb_pf.1*

%files compiler-cisco-fwsm
%defattr(644,root,root,755)
%{_datadir}/%{name}/platform/fwsm.xml

%files compiler-cisco-iosacl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_iosacl
%{_datadir}/%{name}/platform/iosacl.xml
%{_mandir}/man1/fwb_iosacl.1*

%files compiler-cisco-pix
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_pix
%{_datadir}/%{name}/platform/pix.xml
%{_mandir}/man1/fwb_pix.1*

%files compiler-freebsd-ipfw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_ipfw
%{_datadir}/%{name}/platform/ipfw.xml
%{_mandir}/man1/fwb_ipfw.1*

%files platform-linux24
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/linux24.xml

%files platform-freebsd
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/freebsd.xml

%files platform-openbsd
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/openbsd.xml

%files platform-cisco-fwsm
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/fwsm_os.xml

%files platform-cisco-pix
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/pix_os.xml

%files platform-solaris
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/solaris.xml

%files platform-macosx
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/macosx.xml
