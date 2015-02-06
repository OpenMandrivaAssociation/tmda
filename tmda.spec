%define name	tmda
%define version 1.1.12
%define release 2


Summary:	Tagged Message Delivery Agent
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tgz
License:	BSD
Group:		Networking/Mail
URL:		http://tmda.net
BuildArch:	noarch
Requires:	python-cdb
BuildRequires:	python 
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
TMDA is an OSI certified software application designed to
significantly reduce the amount of SPAM/UCE (junk-mail) you
receive. TMDA combines a  "whitelist" (for known/trusted senders),
a "blacklist" (for undesired senders), and a cryptographically
enhanced confirmation system (for unknown, but legitimate
senders).

%package	emacs
Summary:	Tagged Message Deliver Agent - Emacs Support Files
Group:		Editors
Requires:	tmda >= %{version}, emacs

%description	emacs
This module contains useful helper routines for using TMDA from
Gnus (and perhaps other Emacs based mail/news readers). 

%prep
%setup -q

%build
mv doc/README README2

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}


install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/tmda
install -d %{buildroot}%{_datadir}/emacs/site-lisp
install -d %{buildroot}%{py_puresitedir}/TMDA/pythonlib/email

install -m0755 bin/tmda-* %{buildroot}%{_bindir}/
install -m0644 templates/*.txt %{buildroot}%{_datadir}/tmda/
install -m0644 TMDA/*.py %{buildroot}%{py_puresitedir}/TMDA/
install -m0644 TMDA/pythonlib/email/*.py %{buildroot}%{py_puresitedir}/TMDA/pythonlib/email/
install -m0755 contrib/{collectaddys,printcdb,printdbm} %{buildroot}%{_bindir}
install -m0644 contrib/tmda.el %{buildroot}%{_datadir}/emacs/site-lisp

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog CODENAMES COPYING CRYPTO INSTALL README* THANKS UPGRADE contrib doc/html/{*.html,attachments/} doc/pdf/*
%attr(0755,root,root) %{_bindir}/*
%{py_puresitedir}/TMDA/
%{_datadir}/tmda/*

%files emacs
%defattr(0644,root,root)
%{_datadir}/emacs/site-lisp/tmda.el




%changelog
* Wed Mar 30 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.1.12-1mdv2011.0
+ Revision: 649098
- Update to latest release available, 1.1.12

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 1.0.3-11mdv2011.0
+ Revision: 592363
- rebuild for python 2.7

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-10mdv2010.0
+ Revision: 445488
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.0.3-9mdv2009.1
+ Revision: 326005
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-8mdv2009.0
+ Revision: 261570
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-7mdv2009.0
+ Revision: 254659
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0.3-5mdv2008.1
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.3-5mdv2007.0
+ Revision: 96544
- Rebuild against new python
- Import tmda

* Mon Jan 30 2006 Michael Scherer <misc@mandriva.org> 1.0.3-4mdk
- Remove requires on specific version
- use mkrel
- clean spec, use macro, fix unowned dir

* Thu Jan 06 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.3-3mdk
- merge spec file changes from the provided spec file, spotted
  by Simon Waldman

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.0.3-2mdk
- Rebuild for new python

* Mon Aug 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.3-1mdk
- 1.0.3

* Thu Feb 26 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.92-2mdk
- own dir

* Tue Dec 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.92-1mdk
- 0.92

