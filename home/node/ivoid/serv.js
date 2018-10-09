const express=require('express')
const app=express()

var port=8080;

app.get('/', function(req, res){
  console.log('request from :',req.url);
  res.send('hello from void');
});

app.get('/void', function(req, res){
  console.log(req.url);
  res.sendFile(__dirname + '/fi.html');
});

app.get('/iphp', (req, res)=>{
  console.log(req.url);
  res.sendFile(__dirname + '/pi.html');
});

app.get('/phpf', (req,res)=>{
  console.log(req.url);
  res.sendFile(__dirname + '/phpf.php');
});

app.listen(port)
console.log('server is wait on port :',port)


