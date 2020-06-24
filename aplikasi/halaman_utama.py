from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/", methods=["GET"])
def tampilkan_halaman_utama():
    # Render template yang telah kita buat dengan mengirim parameter:
    return render_template("index.j2")
