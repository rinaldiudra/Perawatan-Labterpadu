from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /ditolak
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/ditolak", methods=["GET"])
def tampilkan_halaman_laporanditolak():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("ditolak.j2")


@app.route("/detailditolak", methods=["GET"])
def tampilkan_halaman_detailditolak():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("detailditolak.j2")