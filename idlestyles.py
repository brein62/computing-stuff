from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

class YourStyle(Style):
    default_style = ""
    styles = {
        Comment:                '#dd0000',
        Keyword:                '#D87C20',
        Name:                   '#000',
        Name.Builtin:           '#a0a',
        String:                 '#00aa00'
        
    }
