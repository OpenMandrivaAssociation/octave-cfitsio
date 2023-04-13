%global octpkg cfitsio

Summary:	I/O routines to read and write FITS (Flexible Image Transport System) files
Name:		octave-cfitsio
Version:	0.0.4
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/cfitsio/
Url:		https://octave-cfitsio.sourceforge.io/
Source0:	https://downloads.sourceforge.net/project/octave-cfitsio/v%{version}/octave-cfitsio-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	pkgconfig(cfitsio)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
I/O routines to read and write FITS (Flexible Image Transport System)
files.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

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

