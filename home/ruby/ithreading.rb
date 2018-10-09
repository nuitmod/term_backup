#!/usr/bin/env ruby

t1=Thread.new do
i=1
  while i<=9 do
    print "t1_i_#{i} "
    puts `pwd`
    `sleep 1` ; i+=1
  end
end

sleep(0.5)

t2=Thread.new do
i=1
  while i<=9 do
    print "t2__i#{i} "
    puts `uptime`
    `sleep 2` ; i+=1
  end
end

t1.join
t2.join

p 'multithreading complite!'
