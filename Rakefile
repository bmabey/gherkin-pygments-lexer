class SyntaxGenerator
  def generate
    require 'yaml'
    require 'erb'
    require 'cucumber'

    feature_keywords_array = []
    scenario_keywords_array = []
    examples_keywords_array = []
    step_keywords_array     = []

    Cucumber::LANGUAGES.each do |lang, words|
      feature_keywords_array << words.delete('feature').split(/\|/) rescue nil

      scenario_keywords_array << words.delete('scenario').split(/\|/) rescue nil
      scenario_keywords_array << words.delete('scenario_outline').split(/\|/) rescue nil
      scenario_keywords_array << words.delete('background').split(/\|/) rescue nil

      examples_keywords_array << words.delete('examples').split(/\|/) rescue nil

      step_keywords_array << keywords(lang, words)
    end
    
    feature_keywords  = feature_keywords_array.flatten.compact.sort.reverse.uniq.join('|')
    scenario_keywords = scenario_keywords_array.flatten.compact.sort.reverse.uniq.join('|')
    examples_keywords = examples_keywords_array.flatten.compact.sort.reverse.uniq.join('|')
    step_keywords     = step_keywords_array.flatten.compact.sort.reverse.uniq.join('|')

    template    = ERB.new(IO.read(File.dirname(__FILE__) + '/lexer.erb.py'))
    syntax      = template.result(binding)

    syntax_file = File.dirname(__FILE__) + '/gherkin_lexer/__init__.py'
    File.open(syntax_file, "w") do |io|
      io.write(syntax)
    end
  end
  
  def keywords(lang, words)
    space = words['space_after_keyword'] ? '\s+' : ''
    %w{given when then and but}.map do |key|
      words[key].split(/\|/).map{|w| "#{w}#{space}"}
    end
  end
end

desc 'Generate Gherkin lexer for all languages supported by Cucumber'
task :generate do
  SyntaxGenerator.new.generate
end
