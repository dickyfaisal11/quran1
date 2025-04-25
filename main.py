import tkinter as tk
from tkinter import messagebox

# Membuat jendela utama
window = tk.Tk()
window.title("Aplikasi Al-Qur'an")
window.geometry("600x400")

# Label sambutan
label = tk.Label(window, text="Selamat Datang di Aplikasi Al-Qur'an", font=("Arial", 14))
label.pack(pady=20)

# Fungsi untuk menampilkan pesan (contoh)
def show_ayat():
    messagebox.showinfo("Ayat", "Ini adalah ayat contoh: Al-Fatihah 1:1")

# Tombol untuk menampilkan ayat
button = tk.Button(window, text="Tampilkan Ayat", command=show_ayat)
button.pack(pady=10)

# Jalankan aplikasi
window.mainloop()

import requests

# Ambil data dari API Al-Quran Cloud
response = requests.get("http://api.alquran.cloud/v1/surah/1")
data = response.json()
ayat = data['data']['ayahs'][0]['text']
print(ayat)  # Menampilkan ayat pertama dari Surah Al-Fatihah