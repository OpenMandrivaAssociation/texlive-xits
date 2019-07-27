# revision 32763
# category Package
# catalog-ctan /fonts/xits
# catalog-date 2014-01-21 01:01:43 +0100
# catalog-license ofl
# catalog-version 1.108
Name:		texlive-xits
Version:	1.200.1
Release:	1
Summary:	A Scientific Times-like font with support for mathematical typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/xits
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xits.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xits.doc.tar.xz
#Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xits.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
XITS is a Times-like font for scientific typesetting with
proper mathematical support for modern, Unicode and OpenType
capable TeX engines, namely LuaTeX and XeTeX. For use with
LuaLaTeX or XeLaTeX, support is available from the fontspec and
unicode-math packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files


#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
