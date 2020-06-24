from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /dikerjakan
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/dikerjakan", methods=["GET"])
def tampilkan_halaman_laporandikerjakan():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("dikerjakan.j2")


@app.route("/detaildikerjakan", methods=["GET"])
def tampilkan_halaman_detaildikerjakan():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("detaildikerjakan.j2")