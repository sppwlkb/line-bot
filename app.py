from flask import Flask, request, abort
import json
import requests

app = Flask(__name__)

# Channel access token
LINE_ACCESS_TOKEN = '53ytUHOgePSzBOJbJH14kaF4+mof/NDDpTlj/v/i4eiX8AjtRQpWgNMT7ia+++6edIJwwa472H87O+hJp4As6W46nmGYQVAosj4w15KNGOdRkZbm1Zz8ctBu6aht2wRR0cvo49BM65XRKftjqSs+BAdB04t89/1O/w1cDnyilFU='

# Function to reply to the message
def reply_message(reply_token, text):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_ACCESS_TOKEN}',
    }
    body = {
        'replyToken': reply_token,
        'messages': [{'type': 'text', 'text': text}]
    }
    requests.post('https://api.line.me/v2/bot/message/reply', headers=headers, data=json.dumps(body))

@app.route('/callback', methods=['POST'])
def callback():
    try:
        body = request.get_json()
        if 'events' in body:
            for event in body['events']:
                if event['type'] == 'message':
                    reply_token = event['replyToken']
                    message = event['message']['text']
                    reply_message(reply_token, f'你說了: {message}')
        return 'OK'
    except Exception as e:
        abort(400)

if __name__ == "__main__":
    app.run(port=5000)
