%define modname yaz
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 64_%{modname}.ini

Summary:	A Z39.50 client for PHP
Name:		php-%{modname}
Version:	1.1.3
Release:	2
License:	PHP License
Group:		Development/PHP
URL:		http://pecl.php.net/package/yaz
Source0:	http://ftp.indexdata.dk/pub/phpyaz/yaz-%{version}.tgz
Source1:	%{modname}.ini
# http://indexdata.dk/phpyaz/demo/mult.phps
Source2:	mult.php
Patch0:		yaz-antibork.diff
BuildRequires:	php-devel >= 3:5.2.2
BuildRequires:	yaz-devel >= 3.0.0
BuildRequires:	libicu-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	libpth-devel
BuildRequires:	tcp_wrappers-devel 
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This extension implements a Z39.50 client for PHP using the YAZ toolkit.

%prep

%setup -q -n %{modname}-%{version}
[ "../package.xml" != "/" ] && mv ../package.xml .

%patch0 -p0

cp %{SOURCE1} %{inifile}
cp %{SOURCE2} mult.php

%build
%serverbuild

phpize
%configure2_5x --with-libdir=%{_lib} \
    --enable-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m0755 %{soname} %{buildroot}%{_libdir}/php/extensions/
install -m0644 %{inifile} %{buildroot}%{_sysconfdir}/php.d/%{inifile}

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS README mult.php package.xml
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Wed Jun 27 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.3-1mdv2012.0
+ Revision: 807198
- 1.1.3

* Thu Jun 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.2-1
+ Revision: 806587
- 1.1.2

* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.1-5
+ Revision: 796961
- fix build
- rebuild for php-5.4.x
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.1-3
+ Revision: 696492
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.1-2
+ Revision: 695493
- rebuilt for php-5.3.7

* Wed Jun 01 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.1-1
+ Revision: 682270
- 1.1.1

* Sun May 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-1
+ Revision: 681633
- 1.1.0 (no changes though...)

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-19
+ Revision: 646707
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-18mdv2011.0
+ Revision: 629902
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-17mdv2011.0
+ Revision: 628218
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-16mdv2011.0
+ Revision: 600551
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-15mdv2011.0
+ Revision: 588888
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-14mdv2010.1
+ Revision: 514721
- rebuilt for php-5.3.2

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 1:1.0.14-13mdv2010.1
+ Revision: 508647
- rebuild

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-12mdv2010.1
+ Revision: 485504
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-11mdv2010.1
+ Revision: 468275
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-10mdv2010.0
+ Revision: 451379
- rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 1:1.0.14-9mdv2010.0
+ Revision: 397288
- Rebuild

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-8mdv2010.0
+ Revision: 377045
- rebuilt for php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-7mdv2009.1
+ Revision: 346709
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-6mdv2009.1
+ Revision: 341850
- rebuilt against php-5.2.9RC2

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-5mdv2009.1
+ Revision: 323145
- rebuild

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-4mdv2009.1
+ Revision: 310322
- rebuilt against php-5.2.7

* Fri Jul 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-3mdv2009.0
+ Revision: 238475
- rebuild

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-2mdv2009.0
+ Revision: 200311
- rebuilt for php-5.2.6

* Thu Feb 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-1mdv2008.1
+ Revision: 173480
- 1.0.14
- bump release
- add more build requires

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.13-4mdv2008.1
+ Revision: 162314
- fix deps (libicu-devel)
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.13-3mdv2008.1
+ Revision: 107743
- restart apache if needed

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.13-2mdv2008.0
+ Revision: 77589
- rebuilt against php-5.2.4

* Fri Jul 06 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.13-1mdv2008.0
+ Revision: 49056
- 1.0.13

* Sun Jun 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.12-1mdv2008.0
+ Revision: 40490
- 1.0.12

* Thu Jun 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.11-2mdv2008.0
+ Revision: 39533
- use distro conditional -fstack-protector

* Thu Jun 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.11-1mdv2008.0
+ Revision: 36523
- 1.0.11

* Sun Jun 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.10-2mdv2008.0
+ Revision: 34811
- rediffed P0
- rebuilt against new upstream version (5.2.3)
- 1.0.10

* Tue May 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.9-1mdv2008.0
+ Revision: 25053
- 1.0.9
- rediffed P0
- fix deps

* Thu May 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.8-4mdv2008.0
+ Revision: 21367
- rebuilt against new upstream version (5.2.2)

