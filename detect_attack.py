from flask import Flask
from flask import render_template, request, url_for
app = Flask(__name__)
import requests
import json
import base64
import pandas as pd
import pickle
import numpy as np
state = 0

@app.route('/client',methods=['POST'])
def getdata():
	print 'start'
	path = '/home/hackathontest/hackathonproject/venv/src/'
	#Get data
	request_data=request.get_json()
	if request_data is not None:
		last_rate_s = str(request_data['last_rate'])
		ip_s = request_data['ip']
		df = pd.DataFrame({'ip':ip_s,'last_rate': float(last_rate_s)},index = [0])
		fileObject = open(path + 'LR', 'rb')
        	pipeline = pickle.load(fileObject)
        	detect_attack = pipeline.predict(df)
		if detect_attack:
			print 'Attack!'
			return 'Not Normal Traffic'
		else:
			print 'Not Attack.'
			return 'Normal Traffic'

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=6000)
