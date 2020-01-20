import os
from flask import Flask, redirect, request
from datetime import date
import requests
import json
import random

app = Flask(__name__)

RANDOM_QUESTION_URL = "https://leetcode.com/problems/random-one-question/all"

MAX_RETRY = 3

def get_today_date():
	return date.today().strftime("%B %d, %Y")

def generate_new_question(history):
	previous_urls = set(history.values())
	for i in range(MAX_RETRY):
		res = requests.get(RANDOM_QUESTION_URL, timeout=5)
		if res.url not in previous_urls:
			return res.url
	return random.choice(list(previous_urls))

def get_question(force_new=False):
	dateVal = get_today_date()
	if os.path.exists("archive.json") == False:
		history = {}
	else:
		history = json.load(open("archive.json"))

	if dateVal not in history or force_new:
		question = generate_new_question(history)
		history[dateVal] = question
		write_to_json_file(history)
	else:
		question = history[dateVal]
	return question

def write_to_json_file(newData):
	with open("archive.json", 'w') as f:
		json.dump(newData, f)

@app.route('/')
def index():
	force_reload = request.args.get('force_reload') != None
	question = get_question(force_reload)
	return redirect(question, code=302)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)



