#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (not included in sdist)
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Import exceptions from potentially bundled packages in requests
Summary(pl.UTF-8):	Importowanie wyjątków z pakietów potencjalnie załączonych do requests
Name:		python-requestsexceptions
Version:	1.4.0
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/r/requestsexceptions/requestsexceptions-%{version}.tar.gz
# Source0-md5:	f43b246ccd7d5b618e6f0dc946a6c3f3
URL:		https://pypi.org/project/requestsexceptions/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Import exceptions from potentially bundled packages in requests.

The Python requests library bundles the urllib3 library, however, some
software distributions modify requests to remove the bundled library.
This makes some operations, such as supressing the "insecure platform
warning" messages that urllib emits difficult. This is a simple
library to find the correct path to exceptions in the requests library
regardless of whether they are bundled.

%description -l pl.UTF-8
Importowanie wyjątków z pakietów potencjalnie załączonych do requests.

Biblioteka Pythona requests załącza bibliotekę urllib3, jednak
niektóre dystrybucje oprogramowania modyfikują requests, aby usunąć
załączoną bibliotekę. To powoduje, że niektóre operacje, takie jak
pomijanie komunikatów "insecure platform warning" z urllib są
utrudnione. requestsexceptions to prosta biblioteka znajdująca ścieżki
do wyjątków w bibliotece requests niezależnie od tego, czy są
załączone.

%package -n python3-requestsexceptions
Summary:	Import exceptions from potentially bundled packages in requests
Summary(pl.UTF-8):	Importowanie wyjątków z pakietów potencjalnie załączonych do requests
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-requestsexceptions
Import exceptions from potentially bundled packages in requests.

The python requests library bundles the urllib3 library, however, some
software distributions modify requests to remove the bundled library.
This makes some operations, such as supressing the "insecure platform
warning" messages that urllib emits difficult. This is a simple
library to find the correct path to exceptions in the requests library
regardless of whether they are bundled.

%description -n python3-requestsexceptions -l pl.UTF-8
Importowanie wyjątków z pakietów potencjalnie załączonych do requests.

Biblioteka Pythona requests załącza bibliotekę urllib3, jednak
niektóre dystrybucje oprogramowania modyfikują requests, aby usunąć
załączoną bibliotekę. To powoduje, że niektóre operacje, takie jak
pomijanie komunikatów "insecure platform warning" z urllib są
utrudnione. requestsexceptions to prosta biblioteka znajdująca ścieżki
do wyjątków w bibliotece requests niezależnie od tego, czy są
załączone.

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
%{__make} -C doc html
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
