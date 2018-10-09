var Wmn=function(name, job){
  this.name=name;
  this.job=job;

  this.who=(i)=>{
  while (i<=4) {
console.log(i+":"+this.name+"_:_:_"+this.job);
  i+=1;}
 }
}
Wmn.prototype.say=function(x){
  console.log(this.name+" say "+x);
}

var wm1=new Wmn("Ruth", "programmer");
var wm2=new Wmn("Maud", "security");

wm2.say("hello!");
wm1.who(1);
console.log(wm1.name);

wm2.describe=function(){
 return this.name +' is a '+ this.job;
}

console.log(wm2.describe()); 

wm1.show=function(){
  console.log(this.name+" : "+this.job);
}
wm1.show();
wm2.who(2);
