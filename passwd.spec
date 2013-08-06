Summary:	The passwd utility for setting/changing passwords using PAM
Name:		passwd
Version:	0.78
Release:	3
License:	BSD
Group:		System/Base
URL:		https://fedorahosted.org/passwd/
Source0:	https://fedorahosted.org/releases/p/a/passwd/%{name}-%{version}.tar.bz2
Patch0:		passwd-0.78-enable-gnome-keyring.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	libuser-devel
BuildRequires:	pam-devel
BuildRequires:	popt-devel
BuildRequires:	audit-devel
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
%makeinstall_std

install -m644 passwd.pamd -D %{buildroot}%{_sysconfdir}/pam.d/passwd

%find_lang %{name}

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/pam.d/passwd
%attr(4511,root,shadow) %{_bindir}/passwd
%{_mandir}/man1/passwd.1*
%lang(ja) %{_mandir}/ja/man1/passwd.1*


%changelog
* Mon Feb 20 2012 abf
- The release updated by ABF

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.78-2mdv2011.0
+ Revision: 666990
- mass rebuild

* Tue Sep 28 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.78-1mdv2011.0
+ Revision: 581560
- new release: 0.79

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.77-3mdv2010.1
+ Revision: 519981
- rebuilt against audit-2 libs

* Sat Jan 30 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.77-2mdv2010.1
+ Revision: 498535
- Patch0: enable gnome keyring

* Tue Sep 15 2009 Frederik Himpe <fhimpe@mandriva.org> 0.77-1mdv2010.0
+ Revision: 443189
- update to new version 0.77

* Sun Jun 28 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.76-1mdv2010.0
+ Revision: 390231
- update to new version 0.76
- provide good URLs
- do not require pwdb since we rely on libuser
- enable audit support

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.74-7mdv2009.1
+ Revision: 319036
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.74-6mdv2009.0
+ Revision: 265326
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Thierry Vignaud <tv@mandriva.org> 0.74-5mdv2009.0
+ Revision: 218045
- rebuild

* Tue May 20 2008 Vincent Danen <vdanen@mandriva.com> 0.74-4mdv2009.0
+ Revision: 209290
- revert the sgid shadow stuff, seems this particular passwd implementation requires being suid root

* Mon May 19 2008 Vincent Danen <vdanen@mandriva.com> 0.74-3mdv2009.0
+ Revision: 209161
- requires shadow group-aware setup
- passwd is sgid shadow now, not suid root

  + Thierry Vignaud <tv@mandriva.org>
    - remove PAM req from description has it's automatically required anyway

* Wed Jan 23 2008 Frederic Crozat <fcrozat@mandriva.com> 0.74-2mdv2008.1
+ Revision: 157046
- Patch0 : notify gnome-keyring pam module of password change
- Clean specfile
- Replace file dep with package dep

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Dec 28 2006 Stew Benedict <sbenedict@mandriva.com> 0.74-1mdv2007.0
+ Revision: 102348
- 0.74: minor fixes in error reporting, localize messages

* Tue Dec 12 2006 Stew Benedict <sbenedict@mandriva.com> 0.73-1mdv2007.1
+ Revision: 95303
- Import passwd

* Thu Nov 16 2006 Stew Benedict <sbenedict@mandriva.com> 0.73-1mdv2007.1
- 0.73

* Tue May 09 2006 Stew Benedict <sbenedict@mandriva.com> 0.71-1mdk
- 0.71, drop P0-2

* Tue Jan 31 2006 Olivier Blin <oblin@mandriva.com> 0.68-5mdk
- use "include" directive instead of deprecated pam_stack module (Patch2)

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.68-4mdk
- Rebuild

* Mon Jun 21 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.68-3mdk
- security fix (Vincent Danen)
- misc spec file fixes

