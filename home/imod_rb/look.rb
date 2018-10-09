class Look < Model
  attr_reader :d, :cl

  def initialize(options)
    @d=options[:d]
    @cl=options[:cl]
    super
  end

  def show_l
    puts "#{n} in #{cl} #{d}"
  end

  def cycl(i)
    while i<6
      puts "#{i} :_#{d}_#{cl}_#{`date`}"
      sleep(0.9)
      i+=1
    end
  end
end
