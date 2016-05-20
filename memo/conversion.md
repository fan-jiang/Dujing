# Generate PDF file

- From wkhtmltopdf.org, download 64 bit wkhtmltopdf
- Append `C:\Program Files\wkhtmltopdf\bin` the system variable "Path"

# Other recommended ways

- pandoc中文pdf转换攻略

	http://afoo.me/posts/2013-07-10-how-to-transform-chinese-pdf-with-pandoc.html

- 中文markdown转pdf
	http://jiangfeng.org/notes/2013/04/19/markdown-with-pdf.html
	
- http://superuser.com/questions/789968/windows-7-batch-command-line-to-save-as-pdf-file-for-word-2013-docx-file

When the font is changed to DaFangKai, the chinese characters are displayed in vertically, This is what I want. But this does not happen in Word.


- This [link](https://kheresy.wordpress.com/2014/04/02/opencc/) gives the explanation of how to build opencc.

- According to http://www.fileformat.info/info/unicode/char/2b748/fontsupport.htm, MingLiU-ExtB (BabelStone Han, MingLiU_HKSCS-ExtB, PMingLiU-ExtB) font family will show some unreadable Chinese characters.

	After MingLiU-ExtB, MingLiU_HKSCS-ExtB, and PMingLiU-ExtB are enabled in Windows 7, some simplified characters (for example, the simplified version of 㑮) are still shown as blank square.
	
	Download the `BabelStone Han` font from http://www.babelstone.co.uk/Fonts/Han.html. This font can show almost all Chinese characters. The font file is `BabelStoneHan`.ttf. however, this will make the text fixed to this font.