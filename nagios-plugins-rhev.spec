%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define nagios_plugins_dir %{_libdir}/nagios/plugins

Name:           nagios-plugins-rhev
Version:        1.0.0
Release:        1%{?dist}
Summary:        Nagios Plugin - check_rhev

Group:          Applications/System
License:        GPLv2+
URL:            https://github.com/dougsland/nagios-plugins-rhev/wiki
Source0:        https://github.com/dougsland/nagios-plugins-rhev/raw/master/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%if (0%{?fedora} > 12 || 0%{?rhel} > 5)
BuildRequires: python-devel, python-setuptools-devel, nagios-plugins, python-paramiko
%else
BuildRequires: python-devel, python-setuptools, nagios-plugins, python-paramiko
%endif

%description
This plugin allow you to monitor your RHEV environment.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/%{nagios_plugins_dir}
install -p -m 755 check_rhev $RPM_BUILD_ROOT/%{nagios_plugins_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING
%{nagios_plugins_dir}/check_rhev
%if (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{python_sitelib}/*.egg-info
%endif

%changelog
* Tue Aug 15 2011 Douglas Schilling Landgraf <dougsland@redhat.com> 1.0.0-1
- Initial Commit
