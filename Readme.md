# Introduction

This software package (Dujing) is to generate Chinese classic books automatically from markdown source files.

# Third Party Tools

The executables from the following softwares are used in this package:

- [Pandoc][1]: Convert markdown files to HTML files
- [OpenCC][2]: Convert Chinese traditional fonts to simplified fonts 
- [wkhtmltopdf][3]: Convert HTML files to PDF files

[1]: https://github.com/jgm/pandoc
[2]: https://github.com/BYVoid/OpenCC
[3]: https://github.com/wkhtmltopdf/wkhtmltopdf

# How to build Dujing

- Download `Pandoc` from [here](http://pandoc.org/installing.html).
- Install `Pandoc` and it will be installed in  `C:\Users\[user name]\AppData\Local\Pandoc\`. Add the Pandoc folder to `Path` (an environment variable).

- Download `OpenCC` from [here](https://bintray.com/byvoid/opencc/OpenCC). The current version is `opencc-1.0.4.tar.gz`.
- Unzipp the above file under the root folder of Dujing.

- Download `wkhtmltopdf` from [here](http://wkhtmltopdf.org/downloads.html).
- Install `wkhtmltopdf` and add `wkhtmltopdf` bin folder (C:\Program Files\wkhtmltopdf\bin) to `Path` (an environment variable).

- Run `build\build.bat`. 