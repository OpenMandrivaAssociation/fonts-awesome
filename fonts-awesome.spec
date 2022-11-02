%define pkgname 	Font-Awesome

%define fontname 	awesome
%define	ttffontdir	%{_datadir}/fonts/TTF/%{fontname}
%define otffontdir	%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Iconic font set
Name:		fonts-ttf-awesome
Version:	6.2.0
Release:	1
License:	OFL
Group:		System/Fonts/True type
URL:		https://github.com/FortAwesome/Font-Awesome/
Source0:	https://github.com/FortAwesome/Font-Awesome/archive/%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontscale
BuildRequires:	mkfontdir

%description
Iconic font set

%package -n fonts-otf-awesome
Group:		System/Fonts/Open type
Summary:	Iconic font set

%description -n fonts-otf-awesome
Iconic font set

%prep
%setup -qn %{pkgname}-%{version}

%build


%install
mkdir -p %{buildroot}%{fontconfdir}/

# TTF fonts
install -dm 0755 %{buildroot}/%{ttffontdir}/
install -m 644 webfonts/*.ttf %{buildroot}%{_xfontdir}/TTF/awesome
mkfontscale %{buildroot}%{ttffontdir}/
mkfontdir %{buildroot}%{ttffontdir}/
ln -s ../../..%{buildroot}%{ttffontdir} %{buildroot}%{fontconfdir}/ttf-%{fontname}:pri=50

# OTF fonts
install -dm 0755 %{buildroot}/%{otffontdir}/
install -m 644 otfs/*.otf %{buildroot}%{_xfontdir}/OTF/awesome
mkfontscale %{buildroot}%{otffontdir}/
mkfontdir %{buildroot}%{otffontdir}/
ln -s ../../..%{buildroot}%{otffontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50


%files
%dir %{ttffontdir}
%{fontconfdir}/ttf-%{fontname}:pri=50
%{ttffontdir}/*.ttf
%verify(not mtime)%{ttffontdir}/fonts.dir
%{ttffontdir}/fonts.scale
%license LICENSE.txt

%files -n fonts-otf-awesome
%dir %{otffontdir}
%{fontconfdir}/otf-%{fontname}:pri=50
%{otffontdir}/*.otf
%verify(not mtime)%{otffontdir}/fonts.dir
%{otffontdir}/fonts.scale
%license LICENSE.txt
