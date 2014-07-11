# revision 32763
# category Package
# catalog-ctan /fonts/xits
# catalog-date 2014-01-21 01:01:43 +0100
# catalog-license ofl
# catalog-version 1.108
Name:		texlive-xits
Version:	1.108
Release:	3
Summary:	A Scientific Times-like font with support for mathematical typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/xits
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xits.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xits.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xits.source.tar.xz
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
%{_texmfdistdir}/fonts/opentype/public/xits/xits-bold.otf
%{_texmfdistdir}/fonts/opentype/public/xits/xits-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/public/xits/xits-italic.otf
%{_texmfdistdir}/fonts/opentype/public/xits/xits-math.otf
%{_texmfdistdir}/fonts/opentype/public/xits/xits-mathbold.otf
%{_texmfdistdir}/fonts/opentype/public/xits/xits-regular.otf
%doc %{_texmfdistdir}/doc/fonts/xits/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/xits/Makefile
%doc %{_texmfdistdir}/doc/fonts/xits/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/xits/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/xits/README
%doc %{_texmfdistdir}/doc/fonts/xits/build.py
%doc %{_texmfdistdir}/doc/fonts/xits/fontcoverage.py
%doc %{_texmfdistdir}/doc/fonts/xits/postprocess.py
%doc %{_texmfdistdir}/doc/fonts/xits/user-guide.pdf
%doc %{_texmfdistdir}/doc/fonts/xits/user-guide.tex
%doc %{_texmfdistdir}/doc/fonts/xits/xits-math.lfg
%doc %{_texmfdistdir}/doc/fonts/xits/xits-specimen.pdf
%doc %{_texmfdistdir}/doc/fonts/xits/xits-specimen.tex
#- source
%doc %{_texmfdistdir}/source/fonts/xits/xits-bold.sfd
%doc %{_texmfdistdir}/source/fonts/xits/xits-bolditalic.sfd
%doc %{_texmfdistdir}/source/fonts/xits/xits-italic.sfd
%doc %{_texmfdistdir}/source/fonts/xits/xits-math.sfd
%doc %{_texmfdistdir}/source/fonts/xits/xits-mathbold.sfd
%doc %{_texmfdistdir}/source/fonts/xits/xits-regular.sfd
%doc %{_texmfdistdir}/source/fonts/xits/xits.fea

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}
