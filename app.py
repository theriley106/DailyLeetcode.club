import os
from flask import Flask, redirect, request, jsonify
from datetime import date
import requests
import json
import random

app = Flask(__name__)

RANDOM_QUESTION_URL = "https://leetcode.com/problems/random-one-question/all"
MAX_RETRY = 10
PROBLEMS = json.load(open("problems.json"))['stat_status_pairs']
E_WEIGHTS = 60
M_WEIGHTS = 30
H_WEIGHTS = 10

QUESTIONS_BY_DIFFICULTY = {}

for val in PROBLEMS:
	if val['difficulty']['level'] not in QUESTIONS_BY_DIFFICULTY:
		QUESTIONS_BY_DIFFICULTY[val['difficulty']['level']] = []
	url = "https://leetcode.com/problems/" + val['stat']["question__title_slug"]
	QUESTIONS_BY_DIFFICULTY[val['difficulty']['level']].append(url)

def random_gen_difficulty():
	category = [1 for i in range(E_WEIGHTS/10)] 
	category += [2 for i in range(M_WEIGHTS/10)] 
	category += [3 for i in range(H_WEIGHTS/10)] 
	return random.choice(category)

def get_today_date():
	return date.today().strftime("%B %d, %Y")

def generate_new_question(history):
	previous_urls = set(history.values())
	for i in range(MAX_RETRY):
		url = random.choice(PROBLEMS)
		url = "https://leetcode.com/problems/{}".format(url['stat']['question__title_slug'])
		if url not in previous_urls:
			return url
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

@app.route('/archive')
def archive():
	if os.path.exists("archive.json") == False:
		write_to_json_file({})
	return jsonify(json.load(open("archive.json")))

@app.route('/')
def index():
	force_reload = request.args.get('force_reload') != None
	question = get_question(force_reload)
	return redirect(question, code=302)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)