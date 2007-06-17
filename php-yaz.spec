%define modname yaz
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 64_%{modname}.ini

Summary:	A Z39.50 client for PHP
Name:		php-%{modname}
Version:	1.0.12
Release:	%mkrel 1
License:	PHP License
Group:		Development/PHP
URL:		http://pecl.php.net/package/yaz
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tar.bz2
Source1:	%{modname}.ini
# http://indexdata.dk/phpyaz/demo/mult.phps
Source2:	mult.php
Patch0:		yaz-antibork.diff
BuildRequires:	php-devel >= 3:5.2.2
BuildRequires:	yaz-devel >= 3.0.0
BuildRequires:	tcp_wrappers-devel 
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
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export FFLAGS="%{optflags}"

%if %mdkversion >= 200710
export CFLAGS="$CFLAGS -fstack-protector"
export CXXFLAGS="$CXXFLAGS -fstack-protector"
export FFLAGS="$FFLAGS -fstack-protector"
%endif

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
