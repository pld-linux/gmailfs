Summary:	provides a mountable Linux filesystem which uses Gmail account as its storage medium.
Name:		gmailfs
Version:	0.2
Release:	0.1
Epoch:		0
License:	GPLv2
Group:		Applications/System
Source0:	http://richard.jones.name/google-hacks/gmail-filesystem/%{name}.tar.gz
# Source0-md5:	ef36e6964ef679d6f14be04857f9d3f8
# Source0-size:	14478
URL:		http://richard.jones.name/google-hacks/gmail-filesystem/gmail-filesystem.html
Requires:	python
Requires:	libfuse >= 1.3
Requires:	python-libgmail
Requires:	python-fuse
# does it need "import profile" for real ?
Requires:	python-devel-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GmailFS provides a mountable Linux filesystem which uses your Gmail
account as its storage medium. GmailFS is a Python application and
uses the FUSE userland filesystem infrastructure to help provide the
filesystem, and libgmail to communicate with Gmail.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_bindir}
cp gmailfs.py $RPM_BUILD_ROOT%{_bindir}/gmailfs.py

install -d $RPM_BUILD_ROOT%{_sbindir}
cp mount.gmailfs $RPM_BUILD_ROOT%{_sbindir}/mount.gmailfs

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/gmailfs.py
%attr(755,root,root) %{_sbindir}/mount.gmailfs
