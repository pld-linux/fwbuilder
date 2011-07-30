#
%define		_majver		4
%define		_minver		2
Summary:	Firewall Builder
Summary(pl.UTF-8):	Narzędzie do tworzenia firewalli
Name:		fwbuilder
Version:	%{_majver}.%{_minver}.2.3541
Release:	3
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/fwbuilder/%{name}-%{version}.tar.gz
# Source0-md5:	56ddc67c79adaf5d5730945ad1a26666
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-configure.patch
Patch1:		%{name}-c++.patch
Patch2:		%{name}-dont-mess-with-compiler-names-and-ccache.patch
URL:		http://www.fwbuilder.org/
BuildRequires:	QtCore-devel >= 4.3
BuildRequires:	QtDBus-devel >= 4.3
BuildRequires:	QtGui-devel >= 4.3
BuildRequires:	QtNetwork-devel >= 4.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
Obsoletes:	fwbuilder-devel
Obsoletes:	fwbuilder-doc
Obsoletes:	libfwbuilder
Obsoletes:	libfwbuilder-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firewall administration toolkit.

%description -l pl.UTF-8
Narzędzie do tworzenia i administracji firewallami.

%package compiler-ipfilter
Summary:	ipfilter compiler for Firewall Builder
Summary(pl.UTF-8):	Kompilator ipfilter dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-ipfilter
ipfilter compiler for Firewall Builder.

%description compiler-ipfilter -l pl.UTF-8
Kompilator ipfilter dla Firewall Buildera.

%package compiler-iptables
Summary:	iptables compiler for Firewall Builder
Summary(pl.UTF-8):	Kompilator iptables dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-iptables
iptables compiler for Firewall Builder.

%description compiler-iptables -l pl.UTF-8
Kompilator iptables dla Firewall Buildera.

%package compiler-openbsd-pf
Summary:	OpenBSD pf compiler for Firewall Builder
Summary(pl.UTF-8):	Kompilator OpenBSD pf dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-openbsd-pf
OpenBSD pf compiler for Firewall Builder.

%description compiler-openbsd-pf -l pl.UTF-8
Kompilator OpenBSD pf dla Firewall Buildera.

%package compiler-cisco-fwsm
Summary:	Cisco FWSM compiler for Firewall Builder
Summary(pl.UTF-8):	Kompilator Cisco FWSM dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-cisco-fwsm
Cisco FWSM compiler for Firewall Builder.

%description compiler-cisco-fwsm -l pl.UTF-8
Kompilator Cisco FWSM dla Firewall Buildera.

%package compiler-cisco-iosacl
Summary:	Cisco IOSACL compiler for Firewall Builder
Summary(pl.UTF-8):	Kompilator Cisco IOSACL dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-cisco-iosacl
Cisco FWSM compiler for Firewall Builder.

%description compiler-cisco-iosacl -l pl.UTF-8
Kompilator Cisco IOSACL dla Firewall Buildera.

%package compiler-cisco-pix
Summary:	Cisco PIX compiler for Firewall Builder
Summary(pl.UTF-8):	Kompilator Cisco PIX dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-cisco-pix
Cisco PIX compiler for Firewall Builder.

%description compiler-cisco-pix -l pl.UTF-8
Kompilator Cisco PIX dla Firewall Buildera.

%package compiler-freebsd-ipfw
Summary:	FreeBSD ipfw compiler for Firewall Builder
Summary(pl.UTF-8):	Kompilator FreeBSD ipfw dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-freebsd-ipfw
FreeBSD ipfw compiler for Firewall Builder.

%description compiler-freebsd-ipfw -l pl.UTF-8
Kompilator FreeBSD ipfw dla Firewall Buildera.

%package compiler-procurve
Summary:	HP Procurve compiler for Firewall Builder
Summary(pl.UTF-8):	Kompilator HP Procurve dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-procurve
HP Procurve compiler for Firewall Builder.

%description compiler-procurve -l pl.UTF-8
Kompilator HP Procurve dla Firewall Buildera.

%package platform-linux24
Summary:	Linux 2.4 specific files
Summary(pl.UTF-8):	Pliki specyficzne dla Linuksa 2.4
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-linux24
Linux 2.4 specific files.

%description platform-linux24 -l pl.UTF-8
Pliki specyficzne dla Linuksa 2.4.

%package platform-bsd
Summary:	Variuos BSD specific files
Summary(pl.UTF-8):	Pliki specyficzne dla różnych BSD
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-bsd
Variuos BSD specific files.

%description platform-bsd -l pl.UTF-8
Pliki specyficzne dla róznych BSD.

%package platform-cisco
Summary:	Cisco specific files
Summary(pl.UTF-8):	Pliki specyficzne dla Cisco
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-cisco
Cisco specific files.

%description platform-cisco -l pl.UTF-8
Pliki specyficzne dla Cisco.

%package platform-procurve
Summary:	HP Procurve specific files
Summary(pl.UTF-8):	Pliki specyficzne dla HP Procurve
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-procurve
HP Procurve specific files.

%description platform-procurve -l pl.UTF-8
Pliki specyficzne dla HP Procurve.

%package platform-solaris
Summary:	Solaris specific files
Summary(pl.UTF-8):	Pliki specyficzne dla Solarisa
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-solaris
Solaris specific files.

%description platform-solaris -l pl.UTF-8
Pliki specyficzne dla Solarisa.

%package platform-macosx
Summary:	MacOS X specific files
Summary(pl.UTF-8):	Pliki specyficzne dla MacOS X
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-macosx
MacOS X specific files.

%description platform-macosx -l pl.UTF-8
Pliki specyficzne dla MacOS X.

%prep
%setup -q
#%patch0 -p1
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
%attr(755,root,root) %{_bindir}/fwbedit
%attr(755,root,root) %{_bindir}/fwbuilder
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/fwbuilder.dtd
%{_datadir}/%{name}/*.xml
%dir %{_datadir}/%{name}/configlets
%dir %{_datadir}/%{name}/locale
%{_datadir}/%{name}/migration
%dir %{_datadir}/%{name}/os
%{_datadir}/%{name}/os/unknown_os.xml
%{_datadir}/%{name}/os/endian.xml
%{_datadir}/%{name}/os/oneshield.xml
%dir %{_datadir}/%{name}/platform
%{_datadir}/%{name}/platform/unknown.xml
%{_desktopdir}/fwbuilder.desktop
%{_mandir}/man1/fwbuilder*
%{_mandir}/man1/fwbedit*
%{_pixmapsdir}/fwbuilder.png
%{_iconsdir}/hicolor/*/apps/fwbuilder.png

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

%files compiler-procurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_procurve_acl
%{_datadir}/%{name}/platform/procurve_acl.xml

%files platform-linux24
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/transfer_secuwall
%{_datadir}/%{name}/configlets/dd-wrt-jffs
%{_datadir}/%{name}/configlets/dd-wrt-nvram
%{_datadir}/%{name}/configlets/ipcop
%{_datadir}/%{name}/configlets/openwrt
%{_datadir}/%{name}/configlets/ipf
%{_datadir}/%{name}/configlets/linux24
%{_datadir}/%{name}/configlets/secuwall
%{_datadir}/%{name}/configlets/sveasoft
%{_datadir}/%{name}/os/linux24.xml
%{_datadir}/%{name}/os/dd-wrt-jffs.xml
%{_datadir}/%{name}/os/dd-wrt-nvram.xml
%{_datadir}/%{name}/os/ipcop.xml
%{_datadir}/%{name}/os/openwrt.xml
%{_datadir}/%{name}/os/secuwall.xml
%{_datadir}/%{name}/os/sveasoft.xml

%files platform-bsd
%defattr(644,root,root,755)
%{_datadir}/%{name}/configlets/bsd
%{_datadir}/%{name}/configlets/freebsd
%{_datadir}/%{name}/configlets/ipfw
%{_datadir}/%{name}/configlets/openbsd
%{_datadir}/%{name}/configlets/pf
%{_datadir}/%{name}/os/freebsd.xml
%{_datadir}/%{name}/os/openbsd.xml

%files platform-cisco
%defattr(644,root,root,755)
%{_datadir}/%{name}/configlets/fwsm_os
%{_datadir}/%{name}/configlets/ios
%{_datadir}/%{name}/configlets/pix_os
%{_datadir}/%{name}/os/ios.xml
%{_datadir}/%{name}/os/pix_os.xml
%{_datadir}/%{name}/os/fwsm_os.xml

%files platform-procurve
%defattr(644,root,root,755)
%{_datadir}/%{name}/configlets/procurve
%{_datadir}/%{name}/os/procurve.xml

%files platform-solaris
%defattr(644,root,root,755)
%{_datadir}/%{name}/configlets/solaris
%{_datadir}/%{name}/os/solaris.xml

%files platform-macosx
%defattr(644,root,root,755)
%{_datadir}/%{name}/configlets/macosx
%{_datadir}/%{name}/os/macosx.xml
