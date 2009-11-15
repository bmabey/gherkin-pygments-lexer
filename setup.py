# -*- coding: utf-8 -*-
"""
Setup for the Gherkin Pygments Lexer
"""
from setuptools import setup
 
__author__ = 'ben@benmabey.com'
 
setup(
    name='Gherkin Pygments Lexer',
    version='0.1.0',
    description=__doc__,
    author=__author__,
    packages=['gherkin_lexer'],
    entry_points='''[pygments.lexers]
gherkinlexer = gherkin_lexer:GherkinLexer
'''
)