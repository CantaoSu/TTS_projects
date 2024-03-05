\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{labbook}[2009/02/24]
\LoadClass{article}

\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amsthm,amssymb,amsfonts, fancyhdr, color, comment, graphicx, environ}
\usepackage{tipa}
\usepackage{xcolor}
\usepackage{mdframed}
\usepackage[shortlabels]{enumitem}
\usepackage{indentfirst}
\usepackage{hyperref}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% You might need to specify font here for another language:
\usepackage[T2A]{fontenc}
\usepackage[utf8]{inputenc}
%%%
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=blue,
}

\pagestyle{fancy}

\newenvironment{problem}[4][Assignment]
    { \subsection{#1 #2 }\begin{mdframed}[backgroundcolor=gray!20]
    \textbf{[#3pts]} \textit{#4}:}
    { \end{mdframed}}


% Define solution environment
\newenvironment{solution}
    {\subsubsection*{Answer}}
    {}


\renewcommand{\qed}{\quad\qedsymbol}

% prevent line break in inline mode
\binoppenalty=\maxdimen
\relpenalty=\maxdimen
