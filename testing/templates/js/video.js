var fs = require('fs'); 
var url = require("url");
var server = require('http').createServer(function(req, res) {

 if(req.url != "/favicon.ico"){
     var pathname = url.parse(req.url).pathname;
     if(pathname == "/"){
          res.writeHead(200, {'Content-Type': 'video/mp4'});  
          var rs = fs.createReadStream('./tt.mp4');  
          
          rs.pipe(res);  
          
          rs.on('end',function(){  
            res.end();  
            console.log('end call');  
          });  

     }else if(pathname == "/sp"){
             var datas = fs.readFileSync("./1.html","utf-8")
             res.writeHead(200, {'Content-Type': 'text/html'}); 
             res.write(datas);
             res.end(" ");

     }
 }
}).listen(8080);

server.on('error',function(err){ 
console.log('err'); 
});