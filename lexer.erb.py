#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import \
     Text, Comment, Literal, Operator, Keyword, Name, String

class GherkinLexer(RegexLexer):
    name = 'Gherkin'
    aliases = ['Cucumber', 'cucumber', 'Gherkin', 'gherkin']
    filenames = ['*.feature', '*.story']

    feature_keywords_regexp  = ur'^(<%= feature_keywords %>)(:)(.*)$'
    scenario_sections_regexp = ur'(\s+)(<%= scenario_keywords %>)(:)(.*)$'
    examples_regexp          = ur'(\s+)(<%= examples_keywords %>)(:)(.*)$'
    step_keywords_regexp     = ur'(\s+)(<%= step_keywords %>)'

    tokens = {
        'comments': [
            (r'#.*$', Comment),
          ],
        'multiline_descriptions' : [
            (step_keywords_regexp, Keyword, "#pop"),
            include('comments'),
            (r"(\s|.)", Name.Constant),
          ],
        'multiline_descriptions_on_stack' : [
          (step_keywords_regexp, Keyword, "#pop:2"),
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
        'scenario_sections_on_stack': [
            (scenario_sections_regexp, bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions_on_stack"),
            ],
        'narrative': [
            include('scenario_sections_on_stack'),
            (r"(\s|.)", Name.Builtin),
          ],
        'table_vars': [
            (r'(<[^>]*>)', bygroups(Literal.String.Symbol)),
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
            (step_keywords_regexp, bygroups(Text, Keyword)),
            (feature_keywords_regexp, bygroups(Name.Class, Name.Class, Name.Constant), 'narrative'),
            (scenario_sections_regexp, bygroups(Text, Name.Class, Name.Class, Name.Constant), "multiline_descriptions"),
            (examples_regexp, bygroups(Text, Name.Class, Name.Class, Name.Constant), "scenario_table_description"),
            (r'(\s|.)', Text),
        ]

    }
