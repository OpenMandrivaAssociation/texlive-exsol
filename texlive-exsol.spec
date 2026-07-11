%global tl_name exsol
%global tl_revision 73982

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	Exercises and solutions from the same source, into a book
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exsol
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exsol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exsol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exsol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros to allow for embedding exercises and
solutions in the LaTeX source of an instructional text (e.g., a book or
a course text) while generating the following separate documents: your
original text that only contains the exercises, and a solution book that
contains only the solutions to the exercises (optionally, the exercises
themselves can also be copied to the solution book). The exercise data
are generated when running LaTeX on your document; the first run also
writes the solutions to a secondary file that may be included in a
simple document harness, may be processed by LaTeX, to generate a nice
solution book. The code of the package was derived (in large part) from
fancyvrb.

