require_relative "model"
require_relative "look"


mod1=Model.new({ :n=>"Kaia", :c=>"NY"}) 
mod2=Model.new({ :n=>"Umi", :c=>"Tokyo"}) 

lk1=Look.new({ :n=>"Kaia", :d=>"blouse", 
:cl=>"purpl"}) 
lk2=Look.new({ :n=>"Umi", :d=> "skirt", 
:cl=>"black"})


mod1.mod_i 
mod2.mod_i

lk1.show_l
lk2.show_l

lk1.cycl(1)
lk2.cycl(1)
