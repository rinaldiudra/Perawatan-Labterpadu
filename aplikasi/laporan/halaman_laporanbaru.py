from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /baru
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/baru", methods=["GET"])
def tampilkan_halaman_laporanbaru():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("baru.j2")


@app.route("/detailbaru", methods=["GET"])
def tampilkan_halaman_detailbaru():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("detailbaru.j2")