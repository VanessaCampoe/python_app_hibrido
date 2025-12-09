from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    texto = request.form.get('texto', '')
    return render_template("index.html", saida=texto)


if __name__ == "__main__":
    app.run(debug=True)