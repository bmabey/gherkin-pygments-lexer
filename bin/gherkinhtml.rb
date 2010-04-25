#!/usr/bin/env ruby

def pygmentize(file, destination=nil)
  destination ||= "#{File.basename(file,".feature")}.html"
  pygmentized = `pygmentize -f html -O encoding=utf-8 #{file}`
  File.open(destination, "wb") do |io|
    io.write(<<-EOF)
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en-us">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <style>
#{IO.read(File.dirname(__FILE__) + '/../gherkin.css')}
  </style>
  <body>
EOF
    io.write(pygmentized)

    io.write(<<-EOF)
  </body>
</html>
EOF
  end
end

if $0 == __FILE__
  pygmentize(*ARGV)
end
