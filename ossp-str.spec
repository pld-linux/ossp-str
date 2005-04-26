
%define tarballname str

Summary:	OSSP str - string handling library
Name:		ossp-str
Version:	0.9.10
Release:	0.1
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/%{tarballname}/%{tarballname}-%{version}.tar.gz
# Source0-md5:	067832cd34c06980f2dc1bc4142d9987
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.ossp.org/pkg/lib/%{tarballname}/
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSP str is a generic string library written in ISO-C which provides
functions for handling, matching, parsing, searching and formatting of
ISO-C strings. So it can be considered as a superset of POSIX
string(3), but its main intention is to provide a more convenient and
compact API plus a more generalized functionality.

%package devel
Summary:	OSSP str - header files and development libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
OSSP str - header files and development libraries.

%package static
Summary:	OSSP str - string handling library - static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
OSSP str - string handling library - static libraries.

%prep
%setup -q -n %{tarballname}-%{version}
%patch0 -p1

%build
mv -f aclocal.m4 acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man[13]/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
