var fs=require('fs');

var rd=fs.readFileSync('readme.txt','utf8');
console.log(rd);

wr="My world is empty\n"
//fs.writeFileSync('writeme.txt', wr);
console.log("It's written!");
