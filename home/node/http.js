var http = require('http');

var port=8080

var server = http.createServer(function(req, res) {
  console.log('request was made from '+req.url)
  res.writeHead(200);
  res.end('Natachka samaya krasivaja! Ja tebja lublu!');
});

server.listen(port);
console.log('server is listenning on :', port);
