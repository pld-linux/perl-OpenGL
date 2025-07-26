#
# Conditional build:
%bcond_with	tests	# unit tests
#
Summary:	OpenGL - Perl module to display 3D data using OpenGL, GLU, GLUT, and GLX
Summary(pl.UTF-8):	OpenGL - moduł Perla przedstawiający dane korzystając z bibliotek OpenGL, GLU, GLUT i GLX
Name:		perl-OpenGL
Version:	0.7000
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/C/CH/CHM/OpenGL-0.70.tar.gz
# Source0-md5:	8b651500162e9b999347a06dc0664ab6
Patch0:		%{name}-build.patch
URL:		https://metacpan.org/dist/OpenGL
BuildRequires:	OpenGL-devel
BuildRequires:	freeglut-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
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
%setup -q -n OpenGL-0.70
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	interface=FREEGLUT \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# packaged as man
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/{OpenGL,OpenGL/Array,OpenGL/Tessellation}.pod

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
%{_mandir}/man3/Array.3pm*
%{_mandir}/man3/OpenGL*.3pm*
%{_mandir}/man3/Tessellation.3pm*
%{_examplesdir}/%{name}-%{version}
