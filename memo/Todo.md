~~- Add page break for each chapter~~
~~- Convert the simplified version~~
~~- Generate simplified book from the command line~~
~~- Generate Zhongyong book~~
~~- Add buildlog file with timestamp~~
	~~@echo Build began at: %DATE% %TIME% > %BuildSummary%~~
	~~set BuildLog=Buildlog.txt~~
	~~set BuildSummary=BuildSummary.txt~~
- Convert Simplified version properly.	
- Decorate name does not work.
- If a generated PDF file is imported to Kindle device, Kindle device could only display first few pages. Starting from page 9-or page 10, the text is not displayed properly.
- Use different page number for Table Of Content.
- The Table of Content does not contain the chapter numbers in order to save the paper.
- Remove Traditional suffix from the source name
- Review Daxue
- Generate DaXue
- Add Preface
- Add Cover Page
- Use python script to iterate all the font size and font name.
- Set up Git hub repository
- Write copy right statement.
- Use the vertical format.
- Add pronunciation for each word.
- Command line accept better format of option, for example, --FontType Traditional

# Conversion from traditional to simplified
- Some words are converted incorrectly.

	孟子：
	將徹　－》將彻
	以旂　－》以旗
	關弓 -> 关
	遏糴 -》 籴
	徵招 -》征招


# Installer
- Markdown Edit includes Pandoc into packages.
- Include htmltopdf software
- Include ccconverter package
- Include fonts into installer.