Name:           libglademm24
Version:        2.6.7
Release:        3.1%{?dist}

Summary:        C++ wrapper for libglade

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libglademm/2.6/libglademm-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  gtkmm24-devel >= 2.6.0
BuildRequires:  libglade2-devel >= 2.6.1

%description
This package provides a C++ interface for libglademm. It is a
subpackage of the GTKmm project.  The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.

%package devel
Summary:        Headers for developing programs that will use libglademm.
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       gtkmm24-devel
Requires:       libglade2-devel

%description devel
This package contains the headers that programmers will need to
develop applications which will use libglademm, part of GTKmm, the C++
interface to the GTK+.


%prep
%setup -q -n libglademm-%{version}


%build
%configure --disable-static --enable-docs
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT docs-to-include
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
%{__mkdir} docs-to-include
%{__mv} ${RPM_BUILD_ROOT}%{_docdir}/gnomemm-2.6/libglademm-2.4/* docs-to-include/
rm -f ${RPM_BUILD_ROOT}%{_datadir}/devhelp/books/libglademm-2.4/*


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig


%postun
/sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, -)
%doc docs-to-include/*
%{_includedir}/libglademm-2.4
%{_libdir}/*.so
%{_libdir}/libglademm-2.4
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 2.6.7-3.1
- Rebuilt for RHEL 6
- Related: rhbz#566527

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Denis Leroy <denis@poolshark.org> - 2.6.7-1
- Update to upstream 2.6.7

* Mon Feb 11 2008 Denis Leroy <denis@poolshark.org> - 2.6.6-1
- Update to 2.6.6, bugfix

* Mon Sep 17 2007 Denis Leroy <denis@poolshark.org> - 2.6.4-1
- Update to 2.6.4
- License tag update

* Tue Oct 10 2006 Denis Leroy <denis@poolshark.org> - 2.6.3-2
- Added dist tag

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 2.6.3-1
- Update to version 2.6.3

* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> - 2.6.2-1
- Update to version 2.6.2

* Fri Nov 25 2005 Denis Leroy <denis@poolshark.org> - 2.6.1-2
- Disable static libraries

* Mon Sep 19 2005 Denis Leroy <denis@poolshark.org> - 2.6.1-1
- Update to 2.6.1

* Thu Apr 28 2005 Denis Leroy <denis@poolshark.org> - 2.6.0-1
- Upgrade to 2.6.0

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Jun 27 2004 Denis Leroy <denis@poolshark.org> - 0:2.4.1-0.fdr.1
- Upgrade to 2.4.1
- Moved docs to regular directory, disabled devhelp

* Thu Sep 25 2003 Eric Bourque <ericb@computer.org>
- Initial build.
