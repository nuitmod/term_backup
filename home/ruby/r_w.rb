
def wm(n)
  x=File.open("noir.txt", 'r')
  puts n
  x.each {|i| puts i}
#  list=x.to_a
#  list.each {|z| puts "#{n}:#{z} isgreat!"; n+=1}
#def wm(n)
#  for name in list
#    puts "#{n} : #{name} is beautiful!"  
#    n+=1
#  end
#  while n<6
#    puts "#{n} : #{list.each} is good!"
#    sleep(0.6)
#    n+=1
#  end
  x.close()
#  File.close()
end

wm(1)

if ARGV.empty?
  puts "No imputted args..."
else 
  puts "Hello, #{ ARGV[0].capitalize }"
end
