- Center chapter title
- Add pinyin (reference: https://zhuanlan.zhihu.com/p/66456862) Use tool https://github.com/mozillazg/python-pinyin

- Replace OpenCC with the latest version 1.0.4 (how to build the source code under windows?)
- Move the python script to 3.4
- Line space should have definite value.
- Replace batch file with python script
	Replace generate.bat
		Generate Cover
- Use python script to iterate all the font size and font name.
- Add all word replacements in MengZi.
- Remove dependency on opencc
- ebook-convert could not load all css files.
- remove chapter number in the table of content
- Create txt output
- Work on kindle generator
- Support Chinese Characters
- Use python script to include non repeat character tools.
- Remove duplicated information related to the cover page.
- Move the conversion to a separate file.
- Create word output

## Not urgent:

- Use the vertical format.
- Add footnote on the text.
- If a generated PDF file is imported to Kindle device, Kindle device could only display first few pages. Starting from page 9-or page 10, the text is not displayed properly.
- Use different page number for Table Of Content.
- The Table of Content does not contain the chapter numbers in order to save the paper.
- Remove Traditional suffix from the source name
- Add pronunciation for each word.
- Command line accept better format of option, for example, --FontType Traditional


# Installer

- Create a dujing installer
- Markdown Edit includes Pandoc into packages.
- Include htmltopdf software
- Include ccconverter package
- Include fonts into installer.