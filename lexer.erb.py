#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import \
     Text, Comment, Literal, Operator, Keyword, Name, String

class GherkinLexer(RegexLexer):
    """
    For `Gherkin <http://cukes.info/>` syntax.
    """
    name = 'Gherkin'
    aliases = ['Cucumber', 'cucumber', 'Gherkin', 'gherkin']
    filenames = ['*.feature']
    mimetypes = ['text/x-gherkin']

    feature_keywords         = ur'^(<%= gherkin_keywords(:feature) %>)(:)(.*)$'
    feature_element_keywords = ur'^(\s*)(<%= gherkin_keywords(:background, :scenario, :scenario_outline) %>)(:)(.*)$'
    examples_keywords        = ur'^(\s*)(<%= gherkin_keywords(:examples) %>)(:)(.*)$'
    step_keywords            = ur'^(\s*)(<%= gherkin_keywords(:step) %>)'

    tokens = {
        'comments': [
            (r'#.*$', Comment),
          ],
        'multiline_descriptions' : [
            (step_keywords, Keyword, "#pop"),
            include('comments'),
            (r"(\s|.)", Name.Constant),
          ],
        'multiline_descriptions_on_stack' : [
            (step_keywords, Keyword, "#pop:2"),
            include('comments'),
            (r"(\s|.)", Name.Constant),
          ],
        'examples_table': [
            (r"\s+\|", Keyword, 'examples_table_header'),
            include('comments'),
            (r"(\s|.)", Name.Constant),
          ],
        'examples_table_header': [
            (r"\s+\|\s*$", Keyword, "#pop:2"),
            include('comments'),
            (r"\s*\|", Keyword),
            (r"[^\|]", Name.Variable),
          ],
        'scenario_sections_on_stack': [
            (feature_element_keywords, bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions_on_stack"),
          ],
        'narrative': [
            include('scenario_sections_on_stack'),
            (r"(\s|.)", Name.Builtin),
          ],
        'table_vars': [
            (r'(<[^>]*>)', bygroups(Name.Variable)),
          ],
        'string': [
            include('table_vars'),
            (r'(\s|.)', String),
          ],
        'py_string': [
            (r'"""', Name.Class, "#pop"),
            include('string'),
          ],
          'table_content': [
            (r"\s+\|\s*$", Keyword, "#pop"),
            include('comments'),
            (r"\s*\|", Keyword),
            include('string'),
          ],
        'double_string': [
            (r'"', Text, "#pop"),
            include('string'),
          ],
        'root': [
            (r'\n', Text),
            include('comments'),
            (r'"""', Name.Class, "py_string"),
            (r'\s+\|', Keyword, 'table_content'),
            (r'"', Text, "double_string"),
            include('table_vars'),
            (r'@[^@\s]+', Name.Namespace),
            (step_keywords, bygroups(Text, Keyword)),
            (feature_keywords, bygroups(Name.Class, Name.Class, Name.Constant), 'narrative'),
            (feature_element_keywords, bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions"),
            (examples_keywords, bygroups(Text, Name.Class, Name.Class, Name.Constant), "examples_table"),
            (r'(\s|.)', Text),
        ]
    }
