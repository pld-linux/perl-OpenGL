#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	OpenGL - Perl module to display 3D data using OpenGL, GLU, GLUT, and GLX
Summary(pl.UTF-8):	OpenGL - moduł Perla przedstawiający dane korzystając z bibliotek OpenGL, GLU, GLUT i GLX
Name:		perl-OpenGL
Version:	0.6704
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHM/OpenGL-%{version}.tar.gz
# Source0-md5:	433e4f197d7200c219494a8604f3e06b
Patch0:		%{name}-build.patch
URL:		http://search.cpan.org/dist/OpenGL/
BuildRequires:	OpenGL-devel
BuildRequires:	freeglut-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides access to most of the OpenGL 1.0, 1.1, and 1.2
APIs. Some amount of GLU is supported (I'm not quite sure what version
it works out to), and GLUT should be completely supported up to API
version 3. A small portion of GLX and X11 is supported, as an
alternative to GLUT.

%description -l pl.UTF-8
Ten moduł daje dostęp do większości API OpenGL 1.0, 1.1 i 1.2.
Udostępnia też część GLU (w bliżej nieokreślonej wersji) oraz
powinien udostępniać pełne API GLUT do wersji 3. Jako alternatywa
dla GLUT jest dostępna także niewielka część API GLX i X11.

%prep
%setup -q -n OpenGL-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	interface=FREEGLUT \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README SUPPORTS TODO COPYRIGHT
%{perl_vendorarch}/OpenGL.pm
%dir %{perl_vendorarch}/OpenGL
%{perl_vendorarch}/OpenGL/Config.pm
%dir %{perl_vendorarch}/auto/OpenGL
%{perl_vendorarch}/auto/OpenGL/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/OpenGL/*.so
%dir %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*.3pm*
%{_examplesdir}/%{name}-%{version}/*
