Summary:	Firewall Builder
Summary(pl):	Narzêdzie do tworzenia firewalli
Name:		fwbuilder
Version:	2.0.0
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fwbuilder/%{name}-%{version}.tar.gz
# Source0-md5:	167ba3ce4b2cacf3018f799b9cee5743
Patch0:		%{name}-configure.patch
URL:		http://www.fwbuilder.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfwbuilder-devel >= 2.0.0
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.0
Requires:	libfwbuilder >= 2.0.0
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
Requires:	%{name} = %{version}-%{release}

%description install
Install script for Firewall Builder rules.

%description install -l pl
Skrypt instaluj±cy regu³ki tworzone przez Firewall Buildera.

%package compiler-ipfilter
Summary:	ipfilter compiler for Firewall Builder
Summary(pl):	Kompilator ipfilter dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-ipfilter
ipfilter compiler for Firewall Builder.

%description compiler-ipfilter -l pl
Kompilator ipfilter dla Firewall Buildera.

%package compiler-iptables
Summary:	iptables compiler for Firewall Builder
Summary(pl):	Kompilator iptables dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-iptables
iptables compiler for Firewall Builder.

%description compiler-iptables -l pl
Kompilator iptables dla Firewall Buildera.

%package compiler-openbsd-pf
Summary:	OpenBSD pf compiler for Firewall Builder
Summary(pl):	Kompilator OpenBSD pf dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-openbsd-pf
OpenBSD pf compiler for Firewall Builder.

%description compiler-openbsd-pf -l pl
Kompilator OpenBSD pf dla Firewall Buildera.

%package compiler-cisco-pix
Summary:	Cisco PIX compiler for Firewall Builder
Summary(pl):	Kompilator Cisco PIX dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-cisco-pix
Cisco PIX compiler for Firewall Builder.

%description compiler-cisco-pix -l pl
Kompilator Cisco PIX dla Firewall Buildera.

%package compiler-freebsd-ipfw
Summary:	FreeBSD ipfw compiler for Firewall Builder
Summary(pl):	Kompilator FreeBSD ipfw dla Firewall Buildera
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description compiler-freebsd-ipfw
FreeBSD ipfw compiler for Firewall Builder.

%description compiler-freebsd-ipfw -l pl
Kompilator FreeBSD ipfw dla Firewall Buildera.

%package platform-linux24
Summary:	Linux 2.4 specific files
Summary(pl):	Pliki specyficzne dla Linuksa 2.4
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-linux24
Linux 2.4 specific files.

%description platform-linux24 -l pl
Pliki specyficzne dla Linuksa 2.4.

%package platform-freebsd
Summary:	FreeBSD specific files
Summary(pl):	Pliki specyficzne dla FreeBSD
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-freebsd
FreeBSD specific files.

%description platform-freebsd -l pl
Pliki specyficzne dla FreeBSD.

%package platform-openbsd
Summary:	OpenBSD specific files
Summary(pl):	Pliki specyficzne dla OpenBSD
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-openbsd
OpenBSD specific files.

%description platform-openbsd -l pl
Pliki specyficzne dla OpenBSD.

%package platform-cisco-pix
Summary:	Cisco PIX specific files
Summary(pl):	Pliki specyficzne dla Cisco PIX
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-cisco-pix
Cisco PIX specific files.

%description platform-cisco-pix -l pl
Pliki specyficzne dla Cisci PIX.

%package platform-solaris
Summary:	Solaris specific files
Summary(pl):	Pliki specyficzne dla Solarisa
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-solaris
Solaris specific files.

%description platform-solaris -l pl
Pliki specyficzne dla Solarisa.

%package platform-macosx
Summary:	MacOS X specific files
Summary(pl):	Pliki specyficzne dla MacOS X
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description platform-macosx
MacOS X specific files.

%description platform-macosx -l pl
Pliki specyficzne dla MacOS X.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
	--with-templatedir=%{_datadir}/fwbuilder

%{__make} \
	QTDIR=/usr

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	QTDIR=/usr \
	DDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,ChangeLog,Credits,README*,*.html}
%attr(755,root,root) %{_bindir}/fwbuilder
%attr(755,root,root) %{_bindir}/fwblookup
%attr(755,root,root) %{_bindir}/fwb_compile_all
%attr(755,root,root) %{_bindir}/fwbedit
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.xml
%dir %{_datadir}/%{name}/locale
%lang(fr) %{_datadir}/%{name}/locale/fwbuilder_fr.qm
%lang(ru) %{_datadir}/%{name}/locale/fwbuilder_ru.qm
%lang(vi) %{_datadir}/%{name}/locale/fwbuilder_vi.qm
%dir %{_datadir}/%{name}/os
%{_datadir}/%{name}/os/linksys.xml
%{_datadir}/%{name}/os/unknown_os.xml
%dir %{_datadir}/%{name}/platform
%{_datadir}/%{name}/platform/unknown.xml
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
%{_datadir}/%{name}/platform/iptables.xml
%{_mandir}/man1/fwb_ipt*

%files compiler-ipfilter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_ipf
%{_datadir}/%{name}/platform/ipf.xml
%{_mandir}/man1/fwb_ipf*

%files compiler-openbsd-pf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_pf
%{_datadir}/%{name}/platform/pf.xml
%{_mandir}/man1/fwb_pf*

%files compiler-cisco-pix
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/fwb_pix
%{_datadir}/%{name}/platform/pix.xml
#%%{_mandir}/man1/fwb_pix*

%files compiler-freebsd-ipfw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fwb_ipfw
%{_datadir}/%{name}/platform/ipfw.xml

%files platform-linux24
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/linux24.xml

%files platform-freebsd
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/freebsd.xml

%files platform-openbsd
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/openbsd.xml

%files platform-cisco-pix
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/pix_os.xml

%files platform-solaris
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/solaris.xml

%files platform-macosx
%defattr(644,root,root,755)
%{_datadir}/%{name}/os/macosx.xml
