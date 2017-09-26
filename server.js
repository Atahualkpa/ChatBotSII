express = require('express'), http = require('http');
var app = express();
var path = require('path');
var fs = require('fs');
var dateTime = require('node-datetime');
var querystring = require('querystring')
 
 
app.set('views', './views')
app.set('view engine', 'jade')
 
const TelegramBot = require('node-telegram-bot-api');
 
const token = '447768988:AAFvpO7pPaiKmOWJabrndbURneU9iyyGGfk';
 
const bot = new TelegramBot(token, {polling: true});
 
bot.onText(/(.+)/, (msg, match) => {
 
  obj = JSON.stringify({'message' : msg.text.toLowerCase()})
 
  var header  = {
    'User-Agent': 'node',
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(obj)
  }
 
  console.log(Buffer.byteLength(obj))
 
  var options = {
      host: '127.0.0.1',
      port: 5000,
      path: '/messages',
      method: 'GET',
      headers : header
  };
 
  const user = msg.chat.first_name+'_'+msg.chat.last_name+'_'
  const chatId = msg.chat.id;
 
  var dt = dateTime.create();
  var formatted = dt.format('Y-m-d H:M:S');
  fs.appendFileSync(__dirname + '/'+user+chatId+'.log', formatted+' '+msg.text+'\n');
 
  var req = http.request(options, function(res){
    var str = '';
    console.log('STATUS: ' + res.statusCode);
    console.log('HEADERS: ' + JSON.stringify(res.headers));

    res.on('data', function (chunk) {
      str += chunk;
      console.log('BODY: ' + chunk);
    }).on('end', function(){
      
      bot.sendMessage(chatId, str)

      var dt2 = dateTime.create();
      var formatted2 = dt2.format('Y-m-d H:M:S');
      fs.appendFileSync(__dirname + '/'+user+chatId+'.log', formatted2+' '+'bot: '+str+'\n');
      
      console.log('chiuso')
    });
  })
 
  req.write(obj)
 
  req.end()
 
});