#!/usr/bin/ruby
#Usage script <argument>

name = "Ruth"
puts "Hello, #{name}!"
#if #{ARGV[0].capitalize}
#puts "#{ARGV[0].capitalize} is here!"
sleep(0.5)
puts "Input your name: "
n=gets.chomp
if n.empty?
 puts "No imputted arguments!"
else
 puts "#{n.capitalize} is here!"
end
