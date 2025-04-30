from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def anasayfa():
    return render_template("anasayfa.html")

@app.route("/giris_sayfasi.html")
def giris_sayfasi():
    return render_template("giris_sayfasi.html")

@app.route("/cikis_ekrani.html")
def cikis_ekrani():
    return render_template("cikis_ekrani.html")

@app.route("/dersler.html")
def dersler():
    return render_template("dersler.html")

@app.route("/kayıtekranı.html")
def kayıtekranı():
    return render_template("kayıtekranı.html")

@app.route("/notlar.html")
def notlar():
    return render_template("notlar.html")

@app.route("/ogrenciler.html")
def ogrenciler():
    return render_template("ogrenciler.html")

@app.route("/raporlar.html")
def raporlar():
    return render_template("raporlar.html")

if __name__ == "__main__": 
    app.run(debug=True)
