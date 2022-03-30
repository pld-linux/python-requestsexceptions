#
# Conditional build:
%bcond_with	tests	# do perform "make test" (tricky python-hacking dependency)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Import exceptions from potentially bundled packages in requests
Name:		python-requestsexceptions
Version:	1.3.0
Release:	7
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/r/requestsexceptions/requestsexceptions-%{version}.tar.gz
# Source0-md5:	85c9a2c5c5ecbd2deb0a491613fbdd12
URL:		https://pypi.python.org/pypi/requestsexceptions
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-hacking >= 0.12.0
BuildConflicts:	python-hacking = 0.13.0
BuildConflicts:	python-hacking >= 0.14
%endif
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-hacking >= 0.12.0
BuildConflicts:	python3-hacking = 0.13.0
BuildConflicts:	python3-hacking >= 0.14
%endif
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Import exceptions from potentially bundled packages in requests.

The python requests library bundles the urllib3 library, however, some
software distributions modify requests to remove the bundled library.
This makes some operations, such as supressing the “insecure platform
warning” messages that urllib emits difficult. This is a simple
library to find the correct path to exceptions in the requests library
regardless of whether they are bundled.

%description -l pl.UTF-8

%package -n python3-requestsexceptions
Summary:	Import exceptions from potentially bundled packages in requests
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-requestsexceptions
Import exceptions from potentially bundled packages in requests.

The python requests library bundles the urllib3 library, however, some
software distributions modify requests to remove the bundled library.
This makes some operations, such as supressing the “insecure platform
warning” messages that urllib emits difficult. This is a simple
library to find the correct path to exceptions in the requests library
regardless of whether they are bundled.

%prep
%setup -q -n requestsexceptions-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/requestsexceptions
%{py_sitescriptdir}/requestsexceptions-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-requestsexceptions
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/requestsexceptions
%{py3_sitescriptdir}/requestsexceptions-%{version}-py*.egg-info
%endif
