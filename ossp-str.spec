#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
%define tarballname str
#
Summary:	OSSP str - string handling library
Summary(pl.UTF-8):   OSSP str - biblioteka do obsługi łańcuchów znaków
Name:		ossp-str
Version:	0.9.12
Release:	0.1
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/str/%{tarballname}-%{version}.tar.gz
# Source0-md5:	3f6da8a6ae6662eedf481f11a65592b2
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.ossp.org/pkg/lib/str/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSP str is a generic string library written in ISO-C which provides
functions for handling, matching, parsing, searching and formatting of
ISO-C strings. So it can be considered as a superset of POSIX
string(3), but its main intention is to provide a more convenient and
compact API plus a more generalized functionality.

%description -l pl.UTF-8
OSSP str to ogólna biblioteka do łańcuchów znaków napisana w ISO-C,
dostarczająca funkcje do obsługi, przetwarzania, przeszukiwania i
formatowania łańcuchów znaków ISO-C. Może być uznawana za nadzbiór
string(3) wg POSIX, ale głównym zamiarem jest dostarczenie bardziej
wygodnego i zwartego API oraz ogólniejszej funkcjonalności.

%package devel
Summary:	OSSP str - header files and development libraries
Summary(pl.UTF-8):   OSSP str - pliki nagłówkowe i biblioteki programistyczne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
OSSP str - header files and development libraries.

%description devel -l pl.UTF-8
OSSP str - pliki nagłówkowe i biblioteki programistyczne.

%package static
Summary:	OSSP str - string handling library - static libraries
Summary(pl.UTF-8):   OSSP str - biblioteka do obsługi łańcuchów znaków - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
OSSP str - string handling library - static libraries.

%description static -l pl.UTF-8
OSSP str - biblioteka do obsługi łańcuchów znaków - biblioteki
statyczne.

%prep
%setup -q -n %{tarballname}-%{version}
%patch0 -p1

%build
mv -f aclocal.m4 acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	%{!?with_static_libs:--enable-static=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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

%if %{with static}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
%endif
