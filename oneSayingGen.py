import sys
import os
import locale
import codecs

content = input('Please input one saying:')
fh = codecs.open("temp.tex", "w", "utf-8")
texSetup = "\\documentclass[20pt]{article} \\usepackage{fontspec,xunicode,xltxtra} \\usepackage[top=20pt,bottom=20pt,right=1cm,left=1cm]{geometry} \\XeTeXlinebreaklocale \"zh\"  \\XeTeXlinebreakskip = 2pt plus 1pt minus 0.1pt \\newfontfamily\\qingkeben{方正清刻本悦宋简体} \\linespread{2}"
rowNumber = (content.count("\\\\") +1)*60 +50
rowNumberInStr = '%dpt' %rowNumber
texSetup = texSetup + "\\special{papersize=21cm," + rowNumberInStr + "}"

texSetup = texSetup + "\\begin{document}\\qingkeben\\noindent\\centering\\fontsize{35pt}{\\baselineskip}\\selectfont···\\\\"
texSetup = texSetup + content + "\\end{document}"

fh.write(texSetup)
fh.close

os.system("xelatex temp.tex")
os.chdir("C:\\Program Files\\ImageMagick-7.0.2-Q16")
os.system("convert -density 600 c:\\users\\chicken\\docs\\stuff\\pubwechat\\onesayinggen\\temp.pdf c:\\users\\chicken\\docs\\stuff\\pubwechat\\onesayinggen\\out.jpg")
