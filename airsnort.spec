Summary:	802.11 WEP Encryption Cracking Tool
Summary(pl):	Program do ³amania szyfrowania WEP dla protoko³u 802.11
Name:		Airsnort
Version:	0.2.1b
Release:	0
License:	GPL
Group:		Networking
Source0:	%{name}-%{version}.tar.gz
URL:		http://airsnort.shmoo.com/
BuildRequires:	gtk+-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
AirSnort is a wireless LAN (WLAN) tool that recovers encryption keys.
It operates by passively monitoring transmissions, computing the
encryption key when enough packets have been gathered.

%description -l pl
AirSnort jest narzêdziem dla sieci bezprzewodowych (WLAN) do
uzyskiwania kluczy szyfrowania. Dzia³a pasywnie monitoruj±c transmisjê
i obliczaj±c klucz po przechwyceniu wystarczaj±cej ilo¶ci pakietów.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.decrypt TODO
%attr(755,root,root) %{_bindir}/*
