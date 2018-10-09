setInterval(()=>{
  console.log('invoid99');
}, 1000)

i_input=(i)=>{
  console.log("i :",i);
  return i;
}

function ww(){
var p=new Promise(function(resolve, reject){
  console.log('prom is called');
    setTimeout(function(){
    let u=99
    console.log('u =',u)
    if(u>=9){
      resolve();
      console.log(u)
    }else{
      reject();
      console.log('rej');
    }
  }, 1000)
});
  return p;
}

i_input(22);

ww().then(
  io1=>console.log('void is coming'),
  io2=>console.log('democraty is hacked')
);

let fn=()=>{
  console.log('innoir');
}


fn()

