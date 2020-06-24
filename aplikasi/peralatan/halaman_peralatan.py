from flask import render_template

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /peralatan
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/daftarperalatan", methods=["GET"])
def tampilkan_halaman_daftarperalatan():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("daftarperalatan.j2")


@app.route("/lihatperalatan", methods=["GET"])
def tampilkan_halaman_lihatperalatan():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("lihatperalatan.j2")


@app.route("/tambahperalatan", methods=["GET"])
def tampilkan_halaman_tambahperalatan():
    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("tambahperalatan.j2")