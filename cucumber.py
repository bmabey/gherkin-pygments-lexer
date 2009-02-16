#!/usr/bin/env python
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
        'scenario_table_header': [
            (r"\s+\|", Text),
            (r"(.*)(\|)\s*$", bygroups(Literal.String.Symbol, Text), "#pop"),
            (r"(.*)(\|)", bygroups(Literal.String.Symbol, Text)),
            ],
        'root': [
            (r'\n', Text),
            (r'("[^"]*")', String),
            (r"('[^']*')", String),
            (r'(<)([^>]*)(>)', bygroups(Operator, Literal.String.Symbol, Operator)),
            (r'#.*$', Comment),
            (r'(Given|When|Then|And|But)', Keyword),
            (r"\|(.*)\|", Text),
            (r'^(Feature:|Story:)(.*)$', bygroups(Name.Class, Name.Constant)),
            (r'(\s+)(Background|Scenario|Scenario Outline)(:)(.*)$', bygroups(Text, Name.Class, Name.Class, Name.Constant)),
            (r'\s+(Examples:).*$', Name.Class, "scenario_table_header"),
            (r'\s', Text),
            (r'.', Text)
        ]

    }

def main():
  code = open(sys.argv[1]).read()
  print highlight(code, GherkinLexer(), HtmlFormatter())

if __name__ == "__main__":
  main()



