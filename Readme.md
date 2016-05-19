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

# How to build this software

## Installation

- Download the latest version of the following softwares.
- Install them.
- Add the folders which contain executable files (bin folder) to `Path` (an environment variable) by running the following command:

	set PATH=%PATH%;[Bin Folder]

### Pandoc

- [Download Link](http://pandoc.org/installing.html ).
- Bin folder: `C:\Users\[user name]\AppData\Local\Pandoc\`.

### OpenCC

- [Download Link] (https://bintray.com/byvoid/opencc/OpenCC ). The current version is `opencc-1.0.4.tar.gz`.
- The release format is *.tar.gz. Unzipp this file to the root folder of Dujing.

### wkhtmltopdf

- [Download Link] (http://wkhtmltopdf.org/downloads.html ).
- Bin folder: `C:\Program Files\wkhtmltopdf\bin`.

### Python

- [Download Link](https://www.python.org/downloads/ ).
- Bin folder: `C:\Python27`

## Build

Generate the classic books by running `build\build.bat`.
