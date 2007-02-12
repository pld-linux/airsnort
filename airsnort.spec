Summary:	802.11 WEP Encryption Cracking Tool
Summary(pl.UTF-8):	Program do łamania szyfrowania WEP dla protokołu 802.11
Name:		airsnort
Version:	0.2.7e
Release:	0.1
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/airsnort/%{name}-%{version}.tar.gz
# Source0-md5:	8f852bd872fa7d352c14781010c25ef4
URL:		http://airsnort.shmoo.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libpcap-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AirSnort is a wireless LAN (WLAN) tool that recovers encryption keys.
It operates by passively monitoring transmissions, computing the
encryption key when enough packets have been gathered.

%description -l pl.UTF-8
AirSnort jest narzędziem dla sieci bezprzewodowych (WLAN) pozwalającym
na uzyskiwanie kluczy szyfrowania. Działa pasywnie monitorując
transmisję i obliczając klucz po przechwyceniu wystarczającej ilości
pakietów.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.decrypt TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
