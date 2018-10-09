class Wmn
  attr_reader :n, :j
  def initialize(name, job)
    @n=name
    @j=job
  end
  
  def show_w
    puts "#{n} a great #{j}"
  end 

  def level(l)
    x="#{n} from level #{l}"
    puts x
  end

  def cycle(i,d)
    while i<d
      puts "#{i} : #{j}"
      sleep(0.5)
      i+=1
    end
  end

end

wm1=Wmn.new('Ruth', 'programmer')
wm2=Wmn.new('Maud', 'security')

puts "#{wm1.n} is a #{wm1.j}"
puts "#{wm2.n} is beautiful!"
puts "She is a #{wm2.j}"
puts "#{wm1.n} is very beautiful too!"
wm1.show_w
wm2.show_w
wm1.level(99)

puts "First cycle for #{wm1.n}:"
wm1.cycle(1,6)
puts "Second for #{wm2.n}:"
sleep(0.8)
wm2.cycle(9,13)
puts "Finished!!!"
