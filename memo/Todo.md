~~- Add page break for each chapter~~
~~- Convert the simplified version~~
~~- Generate simplified book from the command line~~
~~- Generate Zhongyong book~~
~~- Add buildlog file with timestamp~~
	~~@echo Build began at: %DATE% %TIME% > %BuildSummary%~~
	~~set BuildLog=Buildlog.txt~~
	~~set BuildSummary=BuildSummary.txt~~
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


## Some word could not be shown in simplied version

孟子： *𫗦*啜, *𫛞*舌之人 *𫍙𫍙*

中庸： *𫓧*钺

論語： 
- 大车无􀀀，小车无􀀀，其何以行之哉
- 袗􀀀绤，必表而出之。

# Installer
- Markdown Edit includes Pandoc into packages.
- Include htmltopdf software
- Include ccconverter package
- Include fonts into installer.