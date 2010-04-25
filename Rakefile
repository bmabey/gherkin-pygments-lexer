require 'rubygems'
require 'launchy'

desc 'Generate Gherkin lexer for all languages supported by Cucumber'
task :i18n_generate do
  require 'erb'
  require 'gherkin/i18n'

  def gherkin_keywords(*keys)
    Gherkin::I18n.keyword_regexp(*keys).gsub(/'/, "\\\\'")
  end

  template    = ERB.new(IO.read(File.dirname(__FILE__) + '/lexer.erb.py'))
  syntax      = template.result(binding)

  syntax_file = File.dirname(__FILE__) + '/gherkin_lexer/__init__.py'
  File.open(syntax_file, "w") do |io|
    io.write(syntax)
  end
end

desc 'Install'
task :install => :i18n_generate do
  sh "sudo python setup.py install"
end

desc "Manually Eyeball output for all of Cucumber's i18n features"
task :eyeball_cucumber => :install do
  Dir[File.dirname(__FILE__) + '/../cucumber/examples/i18n/**/*.feature'].each do |f|
    sh "pygmentize #{f}"
  end
end

desc "Manually Eyeball the sample.feature"
task :eyeball_sample => :install do
  sh "pygmentize sample.feature"
end

desc "Manually Eyeball the sample.feature in HTML"
task :eyeball_sample_html => :install do
  sh "#{File.dirname(__FILE__)}/bin/gherkinhtml.rb sample.feature"
  Launchy::Browser.run("#{File.dirname(__FILE__)}/sample.html")
end

task :default => :eyeball_sample
