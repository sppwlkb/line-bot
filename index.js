
const express = require('express');
const { Client, middleware } = require('@line/bot-sdk');

const config = {
  channelAccessToken: process.env.CHANNEL_ACCESS_TOKEN || '53ytUHOgePSzBOJbJH14kaF4+mof/NDDpTlj/v/i4eiX8AjtRQpWgNMT7ia+++6edIJwwa472H87O+hJp4As6W46nmGYQVAosj4w15KNGOdRkZbm1Zz8ctBu6aht2wRR0cvo49BM65XRKftjqSs+BAdB04t89/1O/w1cDnyilFU=',
  channelSecret: process.env.CHANNEL_SECRET || 'b3f90444f4ed732cd38c6f7a5368591f'
};

const app = express();
const client = new Client(config);

app.post('/webhook', middleware(config), (req, res) => {
  Promise
    .all(req.body.events.map(handleEvent))
    .then(result => res.json(result))
    .catch(err => {
      console.error(err);
      res.status(500).end();
    });
});

function handleEvent(event) {
  if (event.type !== 'message' || event.message.type !== 'text') {
    return Promise.resolve(null);
  }

  const echo = { type: 'text', text: event.message.text };
  return client.replyMessage(event.replyToken, echo);
}

app.listen(process.env.PORT || 3000, () => {
  console.log('Server is running...');
});
