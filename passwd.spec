Summary:	The passwd utility for setting/changing passwords using PAM
Name:		passwd
Version:	0.74
Release:	%mkrel 1
License:	BSD
Group:		System/Base
Source0:	passwd-%{version}.tar.bz2
# This url is stupid, someone come up with a better one _please_!
URL:		http://www.freebsd.org
Requires:	pam >= 0.59, pwdb >= 0.58, /etc/libuser.conf
BuildRequires:	glib2-devel
BuildRequires:	libuser-devel
BuildRequires:	pam-devel
BuildRequires:	popt-devel

%description
The passwd package contains a system utility (passwd) which sets
and/or changes passwords, using PAM (Pluggable Authentication
Modules).

To use passwd, you should have PAM installed on your system.

%prep

%setup -q

%build
%configure --without-selinux
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/pam.d
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

%makeinstall_std

install -m0644 passwd.pamd %{buildroot}%{_sysconfdir}/pam.d/passwd
perl -p -i -e 's|use_authtok nullok|use_authtok nullok md5|' %{buildroot}%{_sysconfdir}/pam.d/passwd
%find_lang %{name}

# cleanup
rm -f %{buildroot}%{_bindir}/{chfn,chsh}
rm -f %{buildroot}%{_mandir}/man1/{chfn.1,chsh.1}

# strip is borked...
chmod 755 %{buildroot}%{_bindir}/passwd

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/pam.d/passwd
%attr(4511,root,root) %{_bindir}/passwd
%{_mandir}/man1/passwd.1*


