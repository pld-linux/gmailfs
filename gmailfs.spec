Summary:	A mountable Linux filesystem which uses Gmail account as its storage medium
Summary(pl):	Montowalny system plików Linuksa u¿ywaj±cy konta Gmail do przechowywania danych
Name:		gmailfs
Version:	0.3
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://richard.jones.name/google-hacks/gmail-filesystem/%{name}-%{version}.tar.gz
# Source0-md5:	d4a6c4c3ef685459e936abf6cefc2d0d
URL:		http://richard.jones.name/google-hacks/gmail-filesystem/gmail-filesystem.html
Requires:	libfuse >= 1.3
Requires:	python
# does it need "import profile" for real ?
Requires:	python-devel-tools
Requires:	python-fuse
Requires:	python-libgmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GmailFS provides a mountable Linux filesystem which uses your Gmail
account as its storage medium. GmailFS is a Python application and
uses the FUSE userland filesystem infrastructure to help provide the
filesystem, and libgmail to communicate with Gmail.

%description -l pl
GmailFS udostêpnia montowalny system plików dla Linuksa wykorzystuj±cy
konto Gmail jako no¶nik do przechowywania danych. GmailFS to aplikacja
w Pythonie, u¿ywaj±ca FUSE (infrastruktury systemu plików w
przestrzeni u¿ytkownika) aby umo¿liwiæ systemowi plików i libgmail
komunikowanie siê z us³ug± Gmail.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/sbin,%{_sysconfdir}}

install mount.gmailfs $RPM_BUILD_ROOT/sbin/mount.gmailfs
install gmailfs.py $RPM_BUILD_ROOT%{_bindir}/gmailfs.py
install gmailfs.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/gmailfs.py
%attr(755,root,root) /sbin/mount.gmailfs
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/gmailfs.conf
