%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio

Name: oauth
Summary: oauth lib
Group: Internet/Applications
License: Apache
Version: 20100601
Release: 2%{?dist}
URL: http://oauth.net/code/
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

BuildRequires: java >= 0:1.6.0
BuildRequires: ant >= 0:1.7.0
BuildRequires: tomcat6-servlet-2.5-api
BuildRequires: jakarta-commons-httpclient >= 3.1
Requires: java >= 0:1.6.0
%define __jar_repack %{nil}

%description
oauth

%prep
%setup -q

%build
ant -Dlibdir=/usr/share/java -Dversion=%{version} clean package

%install
rm -rf $RPM_BUILD_ROOT
# Create the directory structure required to lay down our files
# common
install -d -m 755 $RPM_BUILD_ROOT/usr/share/java/
install -m 644 commons/dist/lib/oauth-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/
install -m 644 consumer/dist/lib/oauth-consumer-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/
install -m 644 provider/dist/lib/oauth-provider-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/share/java/oauth-%{version}.jar
/usr/share/java/oauth-consumer-%{version}.jar
/usr/share/java/oauth-provider-%{version}.jar


%changelog
* Wed Feb 29 2012 Chris Duryee (beav) <cduryee@redhat.com>
-  tag for building

* Tue Feb 28 2012 Chris Duryee (beav) <cduryee@redhat.com>
- new package built with tito

* Tue Feb 28 2012 Chris Duryee (beav) <cduryee@redhat.com>
- initial commit
