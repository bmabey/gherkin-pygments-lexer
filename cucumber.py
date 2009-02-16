#!/usr/bin/python
from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *
from pygments import highlight
from pygments.formatters import HtmlFormatter
import sys

class GherkinLexer(RegexLexer):
    name = 'Cucumber'
    aliases = ['cucumber', 'gherkin', 'bdd']
    filenames = ['*.feature', '*.story']

    tokens = {
        'keywords': [
            (r'(Given|When|Then|And|But)\b', Keyword)
            ],
        'root': [
            (r'\n', Text),
            (r'\s', Text),
            (r'("[^"]*")', String),
            (r"('[^']*')", String),
            (r'(<)([^>]*)(>)', bygroups(Operator, Literal.String.Symbol, Operator)),
            (r'#.*$', Comment),
            include('keywords'),
            (r"\|(.*)\|", Text),
            (r'(\s*)(Feature|Story|Background|Examples|Scenario|Scenario Outline)(:)(.*)$', bygroups(Text, Name.Class, Name.Class, Name.Constant)),
            (r'.', Text)
        ]

    }

def main():
  code = open(sys.argv[1]).read()
  print highlight(code, GherkinLexer(), HtmlFormatter())

if __name__ == "__main__":
  main()



