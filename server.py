from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/+", methods=['POST', 'GET'])
def index_():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return "Datos recibidos"
    elif request.method == 'GET':
        return render_template('index.html')
    else:
        return "Metodo no valido"


@app.route("/sytle")
def style():
    return "/style/stile.css"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)