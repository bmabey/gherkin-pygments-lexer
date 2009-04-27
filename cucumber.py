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
        'comments': [
            (r'#.*$', Comment),
          ],
        'multiline_descriptions' : [
            (r'(Given|When|Then|And|But)', Keyword, "#pop"),
            include('comments'),
            (r"(\s|.)", Name.Constant),
          ],
        'scenario_table_description': [
            (r"\s+\|", Text, 'scenario_table_header'),
            include('comments'),
            (r"(\s|.)", Name.Constant),
          ],
        'scenario_table_header': [
            (r"\s+\|\s*$", Text, "#pop:2"),
            (r"(\s+\|\s*)(#.*)$", bygroups(Text, Comment), "#pop:2"),
            include('comments'),
            (r"\s+\|", Text),
            (r"[^\|]", Literal.String.Symbol),
          ],
        'narrative': [
            (r'(\s+)(Background|Scenario|Scenario Outline)(:)(.*)$', bygroups(Text, Name.Class, Name.Class, Name.Constant), "#pop"),
            (r"(\s|.)", Name.Builtin),
          ],
        'table_vars': [
            (r'(<)([^>]*)(>)', bygroups(Operator, Literal.String.Symbol, Operator)),
          ],
        'string': [
            include('table_vars'),
            (r'(\s|.)', String),
          ],
        'py_string': [
            (r'"""', String, "#pop"),
            include('string'),
          ],
        'double_string': [
            (r'"', String, "#pop"),
            include('string'),
          ],
        'single_string': [
            (r"'", String, "#pop"),
            include('string'),
          ],
        'root': [
            (r'\n', Text),
            include('comments'),
            (r'"""', String, "py_string"),
            (r'"', String, "double_string"),
            (r"'", String, "single_string"),
            include('table_vars'),
            (r'@[^@\s]+', Name.Namespace),
            (r'(Given|When|Then|And|But)', Keyword),
            (r'^(Feature|Story)(:)(.*)$', bygroups(Name.Class, Name.Class, Name.Constant), 'narrative'),
            (r'(\s+)(Background|Scenario|Scenario Outline)(:)(.*)$', bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions"),
            (r'(\s+)(Scenarios|Examples)(:)(.*)$', bygroups(Text, Name.Class, Name.Class, Name.Constant), "scenario_table_description"),
            (r'(\s|.)', Text),
        ]

    }

def main():
  code = open(sys.argv[1]).read()
  print highlight(code, GherkinLexer(), HtmlFormatter(encoding='utf-8'))

if __name__ == "__main__":
  main()



