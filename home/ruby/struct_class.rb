#!/usr/bin/env ruby

# Wm class
Struct.new('Wm', :name, :job)
wm1=Struct::Wm.new('Ruth', 'programmer')
wm2=Struct::Wm.new('Miut', 'contacter')

puts "1 : #{wm1.name} is a #{wm1.job}"
puts "2 : #{wm2.name} is a #{wm2.job}"

#system func
def sys_dat
  `sleep 1`
  puts `pwd` 
end

wm1.each {|iter| puts iter.size}

sys_dat
