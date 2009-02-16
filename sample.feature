Feature: proof of concept

  In order to read Cucumber features faster and eaiser on Github 
  As a Cucumber user
  I want to have syntax highlighting for Gherkin

  Background:
    Given cheese is good

  Scenario Outline: this is a test 
    Given I have a <var1> and some "string"
    And the following table and some 'string'
      | header 1  | header 2  |
      | cell 1-1  | cell 1-2  |
      | cell 2-1  | "cell 2-2"|

    When I do <var2>
    And here is a string with single and double quotes- "i'll be back" 
    And here is a string with the opposite 'the quote is "Foo"'
    And what about a var in a quote like so: "<var2>"

    Then I should see something...
    But not something else...

  Examples:
    | var1  |  var2  |
    | foo   |  bar   |
    | dog   |  food  |

  Scenario: more examples
    Given some context# this is an inline comment
    # This is a comment
# So is this with no space at front...

