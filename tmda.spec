%define name	tmda
%define version 1.0.3
%define release %mkrel 7


Summary:	Tagged Message Delivery Agent
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
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
mv htdocs/README README.htdocs

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
%doc ChangeLog CODENAMES COPYING CRYPTO INSTALL README* THANKS UPGRADE contrib htdocs/{*.html,img/}
%attr(0755,root,root) %{_bindir}/*
%{py_puresitedir}/TMDA/
%{_datadir}/tmda/*

%files emacs
%defattr(0644,root,root)
%{_datadir}/emacs/site-lisp/tmda.el


