console.log('Uploading...');

function getData(d1, d2){
  console.log('g_dat',d1);
  setTimeout(()=>d2(),2000);
}

getData("payload", ()=>{
  console.log("callback");
})

const fn=(x, y)=>{
  console.log(x+" : "+y());
}

let a=()=>"innoir";

fn("22", a)
