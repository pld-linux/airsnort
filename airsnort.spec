Summary:	802.11 WEP Encryption Cracking Tool
Summary(pl):	Program do ³amania szyfrowania WEP dla protoko³u 802.11
Name:		airsnort
Version:	0.2.4a
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://dl.sourceforge.net/airsnort/%{name}-%{version}.tar.gz
# Source0-md5:	e07e3bd7f2a95b54140e8109a5bd512d
URL:		http://airsnort.shmoo.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libpcap-devel
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
