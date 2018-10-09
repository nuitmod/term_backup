function inp()
  print('Please, imput something..')
    local x=io.read()
    print('Inputted data is : '..x)
end

function ww(i)
  print('Put a num of iteration _')
  y=io.read()
  z=tonumber(y)
  if z<=0 or z>10 then
    print('Uncorrect number of iterstion!!')
    os.execute('sleep 0.9')
    ww(i)
  else
    while i<=z do
      os.execute('ls -l')
      print(i..' : ')
      os.execute('pwd')
      os.execute('sleep 0.7')
      i=i+1
    end
  end
end

inp()
os.execute('sleep 1')
ww(1)
