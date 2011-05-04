Summary:	The passwd utility for setting/changing passwords using PAM
Name:		passwd
Version:	0.78
Release:	%mkrel 2
License:	BSD
Group:		System/Base
URL:		https://fedorahosted.org/passwd/
Source0:	https://fedorahosted.org/releases/p/a/passwd/%{name}-%{version}.tar.bz2
Patch0:		passwd-0.78-enable-gnome-keyring.patch
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
%patch0 -p1 -b .gnome~

%build
%configure2_5x \
	--without-selinux \
	--without-pwdb \
	--with-audit \
	--with-libuser \
	--disable-rpath

%make

%install
rm -rf %{buildroot}

%makeinstall_std

install -m644 passwd.pamd -D %{buildroot}%{_sysconfdir}/pam.d/passwd

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/pam.d/passwd
%attr(4511,root,shadow) %{_bindir}/passwd
%{_mandir}/man1/passwd.1*
%lang(ja) %{_mandir}/ja/man1/passwd.1*
