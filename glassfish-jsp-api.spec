%{?scl:%scl_package glassfish-jsp-api}
%{!?scl:%global pkg_name %{name}}

%global artifactId javax.servlet.jsp-api
%global jspspec 2.2
%global reltag b01


Name:       %{?scl_prefix}glassfish-jsp-api
Version:    2.3.2
Release:    0.6.%{reltag}.2%{?dist}
Summary:    Glassfish J2EE JSP API specification

License:    (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:        http://java.net/jira/browse/JSP
Source0:    %{artifactId}-%{version}-%{reltag}.tar.xz
# no source releases, but this will generate tarball for you from an
# SVN tag
Source1:    generate_tarball.sh
Source2:    http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:    http://hub.opensolaris.org/bin/download/Main/licensing/cddllicense.txt

BuildArch:  noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}maven-plugin-bundle
BuildRequires:  %{?scl_prefix}maven-source-plugin
BuildRequires:  %{?scl_prefix}jvnet-parent
BuildRequires:  %{?scl_prefix}mvn(javax.servlet:javax.servlet-api)
BuildRequires:  %{?scl_prefix}mvn(javax.el:javax.el-api)

%description
This project provides a container independent specification of JSP
2.2. Note that this package doesn't contain implementation of this
specification. See glassfish-jsp for one of implementations

%package javadoc
Summary:        API documentation for %{pkg_name}
BuildArch:      noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{artifactId}-%{version}-%{reltag}
cp -p %{SOURCE2} LICENSE
cp -p %{SOURCE3} cddllicense.txt

# Submited upstream: http://java.net/jira/browse/JSP-31
sed -i "/<bundle.symbolicName>/s/-api//" pom.xml

%pom_xpath_remove "pom:dependency[pom:groupId='javax.el' or pom:groupId='javax.servlet']/pom:scope"

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin

%mvn_alias : javax.servlet:jsp-api

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE cddllicense.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE cddllicense.txt

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 2.3.2-0.6.b01.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 2.3.2-0.6.b01.1%{?dist}
- Automated package import and SCL-ization

* Thu May 25 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.2-0.6.b01
- Add javax.servlet:jsp-api alias

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-0.5.b01
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-0.4.b01
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-0.3.b01
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.2-0.2.b01
- Remove maven-javadoc-plugin execution

* Mon Jan 19 2015 Michael Simacek <msimacek@redhat.com> - 2.3.2-0.1.b01
- Update to upstream version 2.3.2-b01

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Michael Simacek <msimacek@redhat.com> - 2.3.1-3
- Drop manual requires

* Tue Feb 25 2014 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-2
- Do not require jvnet-parent.

* Thu Jan 02 2014 Michal Srb <msrb@redhat.com> - 2.3.1-1
- Update to upstream version 2.3.1

* Mon Aug 05 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-8
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Oct 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> 2.2.1-4
- Change OSGi Bundle-SymbolicName to better match Eclipse needs
- Update URL
- Resolves: rhbz#868169

* Tue Sep  4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-3
- Fix license tag
- Install license files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-1
- Initial version of the package
