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

##　Ｍｏｔｉｖａｔｉｏｎ

“Dujing Academy” 是Montreal時謙學堂在Quebec註冊的非盈利教育機構。她是時謙學堂對外的正式機構，同時為全球讀經教育的推廣盡一份綿薄之力。“Dujing Academy”在申請註冊時，表達了她的使命之一是：
	
	Creates software tools to digitalize classic books so that anyone from anywhere can freely access the electronic version of classic books in any format.

“讓任何人在任何地方都能免費獲得自己喜愛格式的電子經典”是我們做經典電子書的動力。這是一個富有挑戰性的目標，可能永遠無法抵達。我們需要更多人的參與。我們將盡力而為。
