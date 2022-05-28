from flask import Flask, request, render_template

from static.codes.PICM import picm

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        obj_picm = picm(int(data["c"]), float(data["mu"]), float(data["lambda"]))
        if obj_picm.estabilidadSistema():
            print("p0=", obj_picm.p_cero())
            print("pk=", obj_picm.p_k())
            print("p1=", obj_picm.p_n(2))
            print("l=", obj_picm.l())
            print("lq=", obj_picm.l_q())
            print("ln=", obj_picm.l_n())
            print("w=", obj_picm.w())
            print("wq=", obj_picm.w_q())
            print("wn=", obj_picm.w_n())
            print(data)
        else:
            print("Sistema no valido")
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