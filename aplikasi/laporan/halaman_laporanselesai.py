from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /selesai
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/selesai", methods=["GET"])
def tampilkan_halaman_laporanselesai():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("selesai.j2")


@app.route("/detailselesai", methods=["GET"])
def tampilkan_halaman_detailselesai():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("detailselesai.j2")