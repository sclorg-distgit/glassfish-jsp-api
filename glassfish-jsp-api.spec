%global pkg_name glassfish-jsp-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global artifactId javax.servlet.jsp-api
%global jspspec 2.2


Name:       %{?scl_prefix}%{pkg_name}
Version:    2.2.1
Release:    9.6%{?dist}
Summary:    Glassfish J2EE JSP API specification

License:    (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:        http://java.net/jira/browse/JSP
Source0:    %{artifactId}-%{version}.tar.xz
# no source releases, but this will generate tarball for you from an
# SVN tag
Source1:    generate_tarball.sh
Source2:    http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:    http://hub.opensolaris.org/bin/download/Main/licensing/cddllicense.txt

BuildArch:  noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}maven-plugin-bundle
BuildRequires:  %{?scl_prefix}maven-jar-plugin
BuildRequires:  %{?scl_prefix}maven-compiler-plugin
BuildRequires:  %{?scl_prefix}maven-source-plugin
BuildRequires:  %{?scl_prefix}maven-javadoc-plugin
BuildRequires:  %{?scl_prefix}jvnet-parent
BuildRequires:  %{?scl_prefix}mvn(javax.servlet:javax.servlet-api)
BuildRequires:  %{?scl_prefix}mvn(javax.el:javax.el-api)

Requires:       %{?scl_prefix}jvnet-parent
Requires:       %{?scl_prefix}mvn(javax.servlet:javax.servlet-api)
Requires:       %{?scl_prefix}mvn(javax.el:javax.el-api)

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
%setup -q -n %{artifactId}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE2} LICENSE
cp -p %{SOURCE3} cddllicense.txt

# Submited upstream: http://java.net/jira/browse/JSP-31
sed -i "/<bundle.symbolicName>/s/-api//" pom.xml

%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE cddllicense.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE cddllicense.txt


%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-9.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-9.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-9.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Michal Srb <msrb@redhat.com> - 2.2.1-9.3
- rebuilt

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2.1-9
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 2.2.1-8
- Migrate away from mvn-rpmbuild (Resolves: #997486)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

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
