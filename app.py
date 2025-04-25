from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    try:
        surah_data = requests.get("https://equran.id/api/surat").json()
    except Exception as e:
        surah_data = []
    return render_template("index.html", surah_list=surah_data)

@app.route("/get_ayat/<int:surah_number>")
def get_ayat(surah_number):
    try:
        ayat_data = requests.get(f"https://equran.id/api/surat/{surah_number}").json()
        return jsonify(ayat_data)
    except Exception as e:
        return jsonify({"error": str(e)})
