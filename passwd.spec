%define _disable_ld_no_undefined 1

Summary:	The passwd utility for setting/changing passwords using PAM
Name:		passwd
Version:	0.80
Release:	1
License:	BSD
Group:		System/Base
Url:		https://pagure.io/passwd
Source0:	https://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2
Patch0:		passwd-0.79-enable-gnome-keyring.patch
BuildRequires:	audit-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libuser)
Requires:	pam >= 0.59
Requires(pre):	setup >= 2.7.12-2mdv 
#needed for file-deps /etc/libuser.conf
Requires:	libuser

%description
The passwd package contains a system utility (passwd) which sets
and/or changes passwords, using PAM (Pluggable Authentication
Modules).

%prep
%setup -q
%apply_patches

%build
%configure \
	--without-selinux \
	--without-pwdb \
	--with-audit \
	--with-libuser

%make

%install
%makeinstall_std

install -m644 passwd.pamd -D %{buildroot}%{_sysconfdir}/pam.d/passwd

%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/pam.d/passwd
%attr(4511,root,shadow) %{_bindir}/passwd
%{_mandir}/man1/passwd.1*
