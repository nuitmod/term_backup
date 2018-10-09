class Wm
  attr_accessor :n, :c
  def initialize(void={})
    @n=void[ :n]
    @c=void[ :c]
  end
  def show_wm(i)
    while i<6
      puts "#{i} : #{n} __ #{c}" if i%2==0
      puts "#{i} : #{c} __ #{n}" if i%2!=0
      sleep(0.8); i+=1 
    end
  end
end

class Md < Wm
  attr_accessor :r
  def initialize(void)
#    super({ :n=>"Miuu"}) 
    @r=void[ :r]
    super
  end
  def test
    puts "#{n} from #{c}"
  end
end

wm1=Wm.new({ :n=>"Ruth", :c=> "NY"})
u=wm1.n
puts u
puts wm1.c

md1=Md.new({ :n=>"Umi", :c=>"Tokio", 
:r=>"44"})
md2=Md.new({ :n=>"Kaia", :c=>"Washington", 
:r=>"42"})
puts md1.r
puts md1.n
puts md2.c
md1.test
wm1.show_wm(1)
