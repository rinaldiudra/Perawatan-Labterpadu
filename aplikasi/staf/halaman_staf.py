from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /daftar
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/staf", methods=["GET"])
def tampilkan_halaman_staf():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("staf.j2")


@app.route("/lihatstaf", methods=["GET"])
def tampilkan_halaman_lihatstaf():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("lihatstaf.j2")


@app.route("/tambahstaf", methods=["GET"])
def tampilkan_halaman_tambahstaf():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("tambahstaf.j2")


@app.route("/ubahpassword", methods=["GET"])
def tampilkan_halaman_ubahpassword():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("ubahpassword.j2")