from flask import Flask, render_template, jsonify
from flask import request as flask_request
from vercel_wsgi import handle_request
import requests
import json
import os

app = Flask(__name__, static_folder='../static', template_folder='../templates')

def get_surah_list():
    try:
        with open('surah_cache.json', 'r') as f:
            return json.load(f)
    except:
        url = "https://equran.id/api/surat"
        response = requests.get(url)
        with open('surah_cache.json', 'w') as f:
            json.dump(response.json(), f)
        return response.json()

def get_ayat(surah_number):
    url = f"https://equran.id/api/surat/{surah_number}"
    return requests.get(url).json()

@app.route('/')
def index():
    return render_template('index.html', surah_list=get_surah_list())

@app.route('/get_ayat/<int:surah_number>')
def get_ayat_route(surah_number):
    return jsonify(get_ayat(surah_number))

# handler for Vercel
def handler(environ, start_response):
    return handle_request(app, environ, start_response)
