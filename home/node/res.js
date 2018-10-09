function getInfo(){
  console.log("Info is getting up");
    let p=new Promise(function(resolve, reject){
        setTimeout(function(){
          let i=2;
          if(i<9){
            resolve();
          }else{
            reject()
          }
        }, 1000);
    })
  return p;
}

getInfo().then(
    res=>console.log("allright!!!"),
    rej=>console.log("No!")
);
