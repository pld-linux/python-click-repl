Summary:	REPL plugin for Click
Summary(pl.UTF-8):	Wtyczka REPL dla Clicka
Name:		python-click-repl
# keep 0.2.x here for python2 compatibility
Version:	0.2.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/click-repl/
Source0:	https://files.pythonhosted.org/packages/source/c/click-repl/click-repl-%{version}.tar.gz
# Source0-md5:	97a5d1dc17b0e4eb09d836872ceb78c8
URL:		https://pypi.org/project/click-repl/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
REPL plugin for Click.

%description -l pl.UTF-8
Wtyczka REPL dla Clicka.

%prep
%setup -q -n click-repl-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/click_repl
%{py_sitescriptdir}/click_repl-%{version}-py*.egg-info
