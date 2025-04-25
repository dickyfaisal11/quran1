from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=False)