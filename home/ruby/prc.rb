def sys_cmd(delay)
  print "Input a command : "
  cmd=gets.chomp
  print "Input number of iterations : "
  iter=gets.chomp
  c=`#{cmd}`
  i=1
  while i<=iter.to_i
    puts "#{i} : #{c}"
    sleep(delay)
    i+=1
  end
end

sys_cmd(0.8)
