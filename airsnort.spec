Summary:	802.11 WEP Encryption Cracking Tool
Summary(pl):	Program do ³amania szyfrowania WEP dla protoko³u 802.11
Name:		airsnort
Version:	0.2.6
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://dl.sourceforge.net/airsnort/%{name}-%{version}.tar.gz
# Source0-md5:	5a3081e1d07b5052b9a6092e03bf753d
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

%description -l pl
AirSnort jest narzêdziem dla sieci bezprzewodowych (WLAN) pozwalaj±cym
na uzyskiwanie kluczy szyfrowania. Dzia³a pasywnie monitoruj±c
transmisjê i obliczaj±c klucz po przechwyceniu wystarczaj±cej ilo¶ci
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
