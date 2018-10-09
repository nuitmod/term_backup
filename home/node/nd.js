fs = require('fs');

function bdoor(x){
  console.log("Backdoor on port " +x);
}
var i=2
console.log('i _',i)
if (i!=2){
  console.log("i is true 2");
}else{
  console.log("No!");
}

while (i<=4){
  console.log(i); i++;
}

data=fs.readdirSync('./');
//console.log('data:', data);
//var name = prompt("Who is here?");
//console.log('Here' + name);

var y=9
//document.write('Sum is :', i+y);
var wmn=['Maud','Ruth','Ivvi'];
wmn.push('Miut');
console.log(wmn[1], wmn[3]);

for(var j=0; j<5; j+=2)
  console.log(j);

for(var w=0; w<wmn.length; w++){
  console.log(wmn[w]);
}

bdoor(22)
