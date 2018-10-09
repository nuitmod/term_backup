function Wmn(name){
  this.name=name;
}

Wmn.prototype.iwmn=function(kompl){
  console.log(this.name +" is "+ kompl);
}

var wm1 = new Wmn("Ruth");
var wm2 = new Wmn("Maud");
wm1.iwmn("beauty");
wm1.iwmn.apply(wm2,["beauty too!"]);
