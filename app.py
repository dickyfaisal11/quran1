from flask import Flask, render_template, request, jsonify
import requests
import json
import os

app = Flask(__name__, template_folder="templates", static_folder="static")


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)


# Fungsi untuk mendapatkan daftar surah
def get_surah_list():
    try:
        # Cek apakah file cache ada
        if os.path.exists('surah_cache.json'):
            with open('surah_cache.json', 'r') as f:
                return json.load(f)
        else:
            raise FileNotFoundError

    except (FileNotFoundError, json.JSONDecodeError):
        # Jika tidak ada cache, ambil dari API dan simpan ke file cache
        try:
            url = "https://equran.id/api/surat"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                with open('surah_cache.json', 'w') as f:
                    json.dump(data, f)
                return data
            else:
                return {"error": "Failed to fetch data from API"}
        except requests.RequestException as e:
            return {"error": f"Error occurred: {str(e)}"}

# Fungsi untuk mendapatkan ayat berdasarkan surah
def get_ayat(surah_number):
    try:
        url = f"https://equran.id/api/surat/{surah_number}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch ayat for Surah {surah_number}"}
    except requests.RequestException as e:
        return {"error": f"Error occurred: {str(e)}"}

@app.route('/')
def index():
    # Mengambil daftar surah dan render ke halaman index.html
    surah_list = get_surah_list()
    if 'error' in surah_list:
        return render_template('index.html', error=surah_list['error'])
    return render_template('index.html', surah_list=surah_list)

@app.route('/get_ayat/<int:surah_number>')
def get_ayat_route(surah_number):
    # Mengambil ayat untuk surah tertentu dan mengirimkan data dalam format JSON
    return jsonify(get_ayat(surah_number))

if __name__ == '__main__':
    app.run(debug=False)
