%include	/usr/lib/rpm/macros.perl
Summary:	OpenGL perl module
Summary(pl):	Modu� perla OpenGL
Name:		perl-OpenGL
Version:	0.5
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/OpenGL/OpenGL-%{version}.tar.gz
Patch0:		%{name}-INC.patch
Patch1:		%{name}-noGLU1.2.patch
Patch2:		%{name}-constants.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	OpenGL-devel
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides access to most of the OpenGL 1.0, 1.1, and 1.2
APIs. Some amount of GLU is supported (I'm not quite sure what version
it works out to), and GLUT should be completely supported up to API
version 3. A small portion of GLX and X11 is supported, as an
alternative to GLUT.

%prep
%setup -q -n OpenGL-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README SUPPORTS TODO COPYRIGHT
%{perl_sitearch}/OpenGL*
%{perl_sitearch}/auto/OpenGL*
