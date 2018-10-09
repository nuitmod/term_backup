class Model

  attr_reader :n, :c

  def initialize(options={})
    @n=options[:n]
    @c=options[:c]
  end

  def mod_i
    puts "#{n} from #{c}"
  end

end
