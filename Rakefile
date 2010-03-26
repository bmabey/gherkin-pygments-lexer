desc 'Generate Gherkin lexer for all languages supported by Cucumber'
task :i18n_generate do
  require 'erb'
  require 'gherkin/i18n'

  template    = ERB.new(IO.read(File.dirname(__FILE__) + '/lexer.erb.py'))
  syntax      = template.result(binding)

  syntax_file = File.dirname(__FILE__) + '/gherkin_lexer/__init__.py'
  File.open(syntax_file, "w") do |io|
    io.write(syntax)
  end
end
