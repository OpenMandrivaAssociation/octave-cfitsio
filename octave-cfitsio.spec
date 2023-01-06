%global octpkg cfitsio

Summary:	I/O routines to read and write FITS (Flexible Image Transport System) files
Name:		octave-cfitsio
Version:	0.0.4
Release:	1
License:	GPLv3.0+
Group:		Sciences/Mathematics
Url:		https://octave-cfitsio.sourceforge.io/
Source0:	https://downloads.sourceforge.net/project/octave-cfitsio/v%{version}/%{name}-%{version}.tar.gz
#BuildArch:	noarch

BuildRequires:	octave-devel >= 4.4.0
BuildRequires:	pkgconfig(cfitsio)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
An Octave/Matlab client library for cfitsio.

%files
%license COPYING
%doc README.md NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

