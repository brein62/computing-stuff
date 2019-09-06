from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from idlestyles import YourStyle
import os

filename = input("Enter file name here: ")
newfilename = filename[:-3] + "_highlight.html"
file = open(filename, "r")
opfile = open(newfilename, "w")
code = file.read()

result = "<style type='text/css'>\n"
result += HtmlFormatter(style=YourStyle).get_style_defs('.highlight')
result += "\n</style>\n"
result += highlight(code, PythonLexer(), HtmlFormatter(style=YourStyle))

opfile.write(result)
opfile.close()
file.close()
os.system(newfilename)

#print(result)

#wot
