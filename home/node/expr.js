var express = require('express');
var app=express()

var port=3000;

app.get('/', function(req, res){
  console.log('request vas from :',req.url) 
  res.send('Hello Ruth')
});

app.listen(port);
console.log('server is wait on port :',port)
