Summary:	The passwd utility for setting/changing passwords using PAM
Name:		passwd
Version:	0.76
Release:	%mkrel 1
License:	BSD
Group:		System/Base
URL:		https://fedorahosted.org/passwd/
Source0:	https://fedorahosted.org/releases/p/a/passwd/%{name}-%{version}.tar.bz2
BuildRequires:	glib2-devel
BuildRequires:	libuser-devel
BuildRequires:	pam-devel
BuildRequires:	popt-devel
BuildRequires:	audit-devel
Requires:	pam >= 0.59
Requires(pre):	setup >= 2.7.12-2mdv 
#needed for file-deps /etc/libuser.conf
Requires:	libuser
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The passwd package contains a system utility (passwd) which sets
and/or changes passwords, using PAM (Pluggable Authentication
Modules).

%prep
%setup -q

%build
%configure2_5x \
	--without-selinux \
	--without-pwdb \
	--with-audit \
	--with-libuser \
	--disable-rpath

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/pam.d

%makeinstall_std

install -m0644 passwd.pamd %{buildroot}%{_sysconfdir}/pam.d/passwd

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/pam.d/passwd
%attr(4511,root,shadow) %{_bindir}/passwd
%{_mandir}/man1/passwd.1*
