#!/bin/bash

baseurl="https://svn.java.net/svn/jsp~svn/tags/"
pkgname="javax.servlet.jsp-api"

version=`grep Version: *spec | sed -e 's/Version:\s*\(.*\)/\1/'`
version="$version`sed -n 's/%global\s\+reltag\s\+/-/p' *.spec`"
echo $version

svn export "${baseurl}/${pkgname}-${version}"
tar cvJf ${pkgname}-${version}.tar.xz  ${pkgname}-${version}/
