from flask import Flask, request, jsonify, make_response, render_template
import json
import dialogflow_v2 as dialogflow
import datetime
import os
import sys
import apiai
#----------HELPER FUNCTIONS----------------
DEV_KEY = "7e88db9b2e3e42dc85146cf7e571aa01"

def parse_incoming_text(incoming_request):
    return json.loads((incoming_request).decode("utf-8"))['message']

def process_chat(chat_input):
    ai = apiai.ApiAI(DEV_KEY)

    chat_request = ai.text_request()

    chat_request.query = parse_incoming_text(chat_input)

    chat_response = chat_request.getresponse()
    response = make_response(json.loads(chat_response.read())['result']['fulfillment']['speech'])

    return response

# #----------API FRAMEWORK/PROCCESSING-------------------
app = Flask(__name__)

@app.route("/")
def home():
    return 'hello'

@app.route("/process_chat", methods = ['POST'])
def home():
    return process_chat(request.data)

if __name__ == '__main__':
    app.run()
