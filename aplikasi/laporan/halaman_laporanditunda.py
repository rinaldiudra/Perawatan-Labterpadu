from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /ditunda
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/ditunda", methods=["GET"])
def tampilkan_halaman_laporanditunda():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("ditunda.j2")


@app.route("/detailditunda", methods=["GET"])
def tampilkan_halaman_detailditunda():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("detailditunda.j2")