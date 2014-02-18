%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio

Name: oauth
Summary: oauth lib
Group: Internet/Applications
License: Apache
Version: 20100601
Release: 4%{?dist}
URL: http://oauth.net/code/
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

BuildRequires: java >= 0:1.6.0
BuildRequires: ant >= 0:1.7.0
BuildRequires: jakarta-commons-httpclient >= 3.1
%if 0%{?rhel} == 7
BuildRequires: tomcat-servlet-3.0-api
%else
BuildRequires: tomcat6-servlet-2.5-api
%endif

Requires: java >= 0:1.6.0
%define __jar_repack %{nil}

%if 0%{?rhel} == 7
%define tomcat_servlet_jar tomcat-servlet-api.jar
%else
%define tomcat_servlet_jar tomcat6-servlet-2.5-api.jar
%endif


%description
oauth

%prep
%setup -q

%build
ant -Dlibdir=/usr/share/java -Dversion=%{version} -Dtomcat-servlet-jar=%{tomcat_servlet_jar} clean package

%install
rm -rf $RPM_BUILD_ROOT
# Create the directory structure required to lay down our files
# common
install -d -m 755 $RPM_BUILD_ROOT/usr/share/java/
install -m 644 commons/dist/lib/oauth.jar $RPM_BUILD_ROOT/usr/share/java/
install -m 644 consumer/dist/lib/oauth-consumer.jar $RPM_BUILD_ROOT/usr/share/java/
install -m 644 provider/dist/lib/oauth-provider.jar $RPM_BUILD_ROOT/usr/share/java/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/share/java/oauth.jar
/usr/share/java/oauth-consumer.jar
/usr/share/java/oauth-provider.jar


%changelog
* Tue Feb 18 2014 Chris Duryee (beav) <cduryee@redhat.com>
- use tomcat-servlet instead of tomcat6-servlet for el7 (cduryee@redhat.com)

* Wed Mar 21 2012 Chris Duryee (beav) <cduryee@redhat.com>
- remove version from jar filename (cduryee@redhat.com)
- add in missing files (cduryee@redhat.com)

* Wed Feb 29 2012 Chris Duryee (beav) <cduryee@redhat.com>
-  tag for building

* Tue Feb 28 2012 Chris Duryee (beav) <cduryee@redhat.com>
- new package built with tito

* Tue Feb 28 2012 Chris Duryee (beav) <cduryee@redhat.com>
- initial commit
