# revision 30451
# category Package
# catalog-ctan /macros/latex/contrib/exsol
# catalog-date 2013-05-13 10:56:37 +0200
# catalog-license lppl1.3
# catalog-version 0.6
Name:		texlive-exsol
Version:	0.6
Release:	6
Summary:	Exercises and solutions from same source, into a book
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exsol
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exsol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exsol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exsol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The packageThe exsol package provides macros to allow for
embedding exercises and solutions in the LaTeX source of an
instructional text (e.g., a book or a course text) while
generating the following separate documents: - your original
text that only contains the exercises, and - a solution book
that contains only the solutions to the exercises (optionally,
the exercises themselves are also copied to the solution book).
The exercise data are generated when running LaTeX on your
document; the first run also writes the solutions to a
secondary file that may be included in a simple document
harness, may be processed by LaTeX, to generate a nice solution
book. The code of the package was derived (in large part) from
fancyvrb.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/exsol/exsol.sty
%doc %{_texmfdistdir}/doc/latex/exsol/LICENSE
%doc %{_texmfdistdir}/doc/latex/exsol/exsol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/exsol/exsol.dtx
%doc %{_texmfdistdir}/source/latex/exsol/exsol.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
