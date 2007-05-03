%define modname yaz
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 64_%{modname}.ini

Summary:	A Z39.50 client for PHP
Name:		php-%{modname}
Version:	1.0.8
Release:	%mkrel 4
License:	PHP License
Group:		Development/PHP
URL:		http://pecl.php.net/package/yaz
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tar.bz2
Source1:	%{modname}.ini
# http://indexdata.dk/phpyaz/demo/mult.phps
Source2:	mult.php
Patch0:		yaz-1.0.2-antibork.diff
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	yaz-devel tcp_wrappers-devel 
Provides:	php5-yaz
Obsoletes:	php5-yaz
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This extension implements a Z39.50 client for PHP using the YAZ toolkit.

%prep

%setup -q -n %{modname}-%{version}
[ "../package.xml" != "/" ] && mv ../package.xml .

%patch0 -p0

cp %{SOURCE1} %{inifile}
cp %{SOURCE2} mult.php

%build

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


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS README mult.php package.xml
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


