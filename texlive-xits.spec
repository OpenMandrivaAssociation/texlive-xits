%global tl_name xits
%global tl_revision 55730

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.302
Release:	%{tl_revision}.1
Summary:	A Scientific Times-like font with support for mathematical typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/xits
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xits.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xits.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
XITS is a Times-like font for scientific typesetting with proper
mathematical support for modern, Unicode and OpenType capable TeX
engines, namely LuaTeX and XeTeX. For use with LuaLaTeX or XeLaTeX,
support is available from the fontspec and unicode-math packages.

