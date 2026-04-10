from flask import Flask, render_template

app = Flask(__name__)

hayvonlar = ["Sher", "Fil", "Tulki", "Bo'ri", "Quyon", "Maymun"]


@app.route('/hayvonlar')
def hayvonlar_royxati():
    alfabit = sorted(hayvonlar)
    teskari = sorted(hayvonlar, reverse=True)
    return render_template('hayvonlar.html', alfabit=alfabit, teskari=teskari)


if __name__ == "__main__":
    app.run(debug=True)
