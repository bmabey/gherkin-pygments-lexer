#!/usr/bin/env python
from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *
from pygments import highlight
from pygments.formatters import HtmlFormatter
import sys

class GherkinLexer(RegexLexer):
    name = 'Gherkin'
    aliases = ['Cucumber', 'cucumber', 'gherkin', 'bdd']
    filenames = ['*.feature', '*.story']

    tokens = {
        #'step_table_header': [
            #(r"\s+\|\s*$", Text, "#pop"),
            #(r"[^\|]", Literal.String.Symbol),
            #],
        'multiline_descriptions' : [
            (r'(Given|When|Then|And|But)', Keyword, "#pop"),
            (r"(\s|.)", Name.Constant),
            ],
        'scenario_table_description': [
            (r"\s+\|", Text, 'scenario_table_header'),
            (r"(\s|.)", Name.Constant),
            ],
        'scenario_table_header': [
            (r"\s+\|\s*$", Text, "#pop:2"),
            (r"\s+\|", Text),
            (r"[^\|]", Literal.String.Symbol),
            ],
        'narrative': [
            (r'(\s+)(Background|Scenario|Scenario Outline)(:)(.*)$', bygroups(Text, Name.Class, Name.Class, Name.Constant), "#pop"),
            (r"\s", Comment),
            (r".", Comment),
          ],
        'root': [
            (r'\n', Text),
            (r'("[^"]*")', String),
            (r"('[^']*')", String),
            (r'(<)([^>]*)(>)', bygroups(Operator, Literal.String.Symbol, Operator)),
            (r'#.*$', Comment),
            (r'@\w+', Name.Namespace),
            (r'(Given|When|Then|And|But)', Keyword),
            (r'^(Feature|Story)(:)(.*)$', bygroups(Name.Class, Name.Class, Name.Constant), 'narrative'),
            (r'(\s+)(Background|Scenario|Scenario Outline)(:)(.*)$', bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions"),
            (r'(\s+)(Scenarios|Examples)(:)(.*)$', bygroups(Text, Name.Class, Name.Class, Name.Constant), "scenario_table_description"),
            (r'(\s|.)', Text),
        ]

    }

def main():
  code = open(sys.argv[1]).read()
  print highlight(code, GherkinLexer(), HtmlFormatter())

if __name__ == "__main__":
  main()



