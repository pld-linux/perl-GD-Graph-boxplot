%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Graph-boxplot
Summary:	GD::Graph::boxplot Perl module - create box-and-whisker plots
Summary(pl):	Modu³ Perla GD::Graph::boxplot - tworzenie wykresów pude³kowe
Name:		perl-GD-Graph-boxplot
Version:	1.00
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	45193804ffc099eedff7e893bb037018
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GD >= 1.18
BuildRequires:	perl-GD-Graph >= 1.30
BuildRequires:	perl-Statistics-Descriptive >= 2.4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Graph::boxplot is a package to generate PNG box and whisker plots,
using GD and GD::Graph modules.

%description -l pl
GD::Graph::boxplot to pakiet do tworzenia obrazków PNG z wykresami
pude³kowymi przy u¿yciu modu³ów GD i GD::Graph.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc boxplot.html
%{perl_vendorlib}/GD/Graph/boxplot.pm
%{_mandir}/man3/*
