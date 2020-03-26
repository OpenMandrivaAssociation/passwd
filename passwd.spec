%define _disable_ld_no_undefined 1

Summary:	The passwd utility for setting/changing passwords using PAM
Name:		passwd
Version:	0.80
Release:	4
License:	BSD
Group:		System/Base
Url:		https://pagure.io/passwd
Source0:	https://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2
Patch0:		https://src.fedoraproject.org/rpms/passwd/raw/master/f/passwd-0.80-manpage.patch
Patch1:		https://src.fedoraproject.org/rpms/passwd/raw/master/f/passwd-0.80-S-output.patch
BuildRequires:	m4
BuildRequires:	audit-devel >= 2.8.2
BuildRequires:	pam-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libuser)
%ifarch riscv64
BuildRequires:	atomic-devel
%endif
Requires:	pam >= 1:1.3.0
Requires:	setup >= 2.8.9
#needed for file-deps /etc/libuser.conf
Requires:	libuser

%description
The passwd package contains a system utility (passwd) which sets
and/or changes passwords, using PAM (Pluggable Authentication
Modules).

%prep
%autosetup -p1

autoreconf -fis -Wall
./autogen.sh

%build
%configure \
	--without-selinux \
	--without-pwdb \
	--with-audit \
	--with-libuser

%make_build

%install
%make_install

install -m644 passwd.pamd -D %{buildroot}%{_sysconfdir}/pam.d/passwd

%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/pam.d/passwd
%attr(4511,root,shadow) %{_bindir}/passwd
%{_mandir}/man1/passwd.1*
