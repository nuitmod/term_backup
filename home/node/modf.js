fn=(i)=>{
  console.log(i+7);
}

var prt={
  x : 9900,
  y : ()=>{console.log("Ruth")}
}

fn(2)
prt.y()
var chn=Object.create(prt);
var inf_ch=()=>{
  console.log(chn.x+" : "+chn.y);
}
inf_ch()
console.log("Dir is",__dirname)
