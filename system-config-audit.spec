Summary:	Utility for editing audit configuration
Summary(pl.UTF-8):	Narzędzie do zmiany konfiguracji audytu
Name:		system-config-audit
Version:	0.4.20
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/s/y/system-config-audit/%{name}-%{version}.tar.xz
# Source0-md5:	1fe70708385f6e3b4c3a84c9d0bb07ee
URL:		https://fedorahosted.org/system-config-audit/
BuildRequires:	audit-libs-devel
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	intltool
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name} = %{version}-%{release}
Requires:	audit >= 2.0
Requires:	python-audit
Requires:	python-pygtk-glade >= 2:2.0
Requires:	usermode
#Requires:	usermode-gtk ?
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An utility for editing audit configuration.

%description -l pl.UTF-8
Narzędzie do zmiany konfiguracji audytu.

%prep
%setup -q

%{__sed} -i -e 's,/main\.py,/main.pyc,' src/system-config-audit.in

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean $RPM_BUILD_ROOT%{_datadir}/system-config-audit

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/system-config-audit
%attr(755,root,root) %{_libexecdir}/system-config-audit-server
%{_datadir}/system-config-audit
%{_desktopdir}/system-config-audit.desktop
