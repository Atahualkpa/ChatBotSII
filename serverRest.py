# coding=utf-8
from flask import Flask, request, json
from regexRules import getResponse

app = Flask(__name__)

@app.route('/messages', methods = ['GET'])
def api_message():
    message = request.json['message']
    if message is '/start'
    	return 'Sono un bot, poco furbo ma abbastanza simpatico, PROVAMI!!'
    return getResponse(message.lower())

if __name__ == '__main__':
    app.run()