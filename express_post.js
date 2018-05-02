const fs = require('fs');
const _ = require('lodash');

const moment = require('moment');

const express = require('express');
var app = express();
var server = require('http').Server(app);
var io = require('socket.io')(server);

const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: false }));

const low = require('lowdb');
const FileSync = require('lowdb/adapters/FileSync');
const adapter = new FileSync('db.json');
const db = low(adapter);
const lodashId = require('lodash-id');
db._.mixin(lodashId);

const collection = db.defaults({ frames: [] }).get('frames');

app.use(express.static('public'));

app.post('/process_post', async (req, res) => {
  let frame = req.body;
  frame.createdBy = moment().valueOf();
  await collection.insert(frame).write();
  await io.emit('insert frame', frame);
  return res.status(200).send('OK');
});

app.get('/frames', async (req, res) => {
  let data = await db.get('frames').sortBy('createdBy').reverse().take(50).value();
  return res.send(data);
});

app.delete('/frames', async (req, res) => {
  let data = await db.set('frames', []).write();
  return res.status(200).send('OK');
});

server.listen(8081, () => {
  const host = server.address().address;
  const port = server.address().port;

  console.log('Express is listening at http://%s:%s', host, port);
});