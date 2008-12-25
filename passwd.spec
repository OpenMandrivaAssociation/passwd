Summary:	The passwd utility for setting/changing passwords using PAM
Name:		passwd
Version:	0.74
Release:	%mkrel 7
License:	BSD
Group:		System/Base
Source0:	passwd-%{version}.tar.bz2
# (fc) add support for notifying gnome-keyring pam module of password change
Patch0:		passwd-0.74-gnomekeyring.patch
# This url is stupid, someone come up with a better one _please_!
URL:		http://www.freebsd.org
Requires:	pam >= 0.59
Requires:	pwdb >= 0.58
Requires(pre):	setup >= 2.7.12-2mdv 
#needed for file-deps /etc/libuser.conf
Requires:	libuser
BuildRequires:	glib2-devel
BuildRequires:	libuser-devel
BuildRequires:	pam-devel
BuildRequires:	popt-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The passwd package contains a system utility (passwd) which sets
and/or changes passwords, using PAM (Pluggable Authentication
Modules).

%prep

%setup -q
%patch0 -p1 -b .gnome-keyring

%build
%configure2_5x --without-selinux
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


