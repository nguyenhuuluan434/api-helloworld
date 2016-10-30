#!/usr/bin/python
from flask import Flask,json,request
import db

application = Flask(__name__)

@application.route('/')
def api_message():
    #if request.headers['Content-Type'] == 'application/json':
	data = db.getData("hello world")
	data_return = {}
	data_return["data"] = data[0][1]
	return json.dumps(data_return)
    #else:
	#return "Unsupported request type."
if __name__ == '__main__':
    application.run()
