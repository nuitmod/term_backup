function Wmn(p){
  this.n = p.n;
  this.j = p.j;
}

var w1=new Wmn({
  n : "Ruth", 
  j : "programmer"
})

var w2=new Wmn({
  n: "Maud",
  j: "admin"
});

const Md=function(p){
  Wmn.apply(this, arguments);
  this.l=p.l;
  this.s=p.s;
}

Wmn.prototype.look=function(){
  console.log(this.n+" is "+this.j);
}

Md.prototype=Object.create(Wmn.prototype);
Md.prototype.constructor=Md;

w1.look()
w2.look()

const m1=new Md({
  n: "Ivvi",
  j: "Innermir",
  l: "2299",
  s: ()=>console.log("My world is empty")
})

Md.prototype.level=function(){
  console.log(this.n+" from level "+this.l);
}

m1.level()

//Md.prototype=Object.create(Wmn.prototype);

m1.look()

const exe=i=>y=>console.log(i*9+y);
exe(2)(4);

m1.s()

