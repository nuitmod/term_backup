class Wmn
  def initialize(name, job)
    @n=name
    @j=job
  end

  def get_name
    @n
  end
  
  def get_job
    @j
  end
  
end
wm1=Wmn.new('Ruth', 'programmmer')
wm2=Wmn.new('Maud', 'security')

puts "#{wm1.get_name} is a #{wm1.get_job}!"
#wm1.get_name
#wm2()
