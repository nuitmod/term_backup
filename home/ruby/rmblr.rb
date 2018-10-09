#!/usr/bin/env ruby

def tt_i(i)
  for _ in 1..9 do
    puts "i=#{i}__#{`pwd`}"
    i+=1; sleep 1
  end
end

tt_i(1)
