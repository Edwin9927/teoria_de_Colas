from flask import Flask, request, render_template

from static.codes.PFCM import pfcm
from static.codes.PICM import picm

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        if data["m"] == '':
            print("PI")
            print(data["m"])
            obj_picm = picm(int(data["k"]), float(data["mu"]), float(data["lambda"]))
            if obj_picm.estabilidadSistema():
                """print("p0=", obj_picm.p_cero())
                print("pk=", obj_picm.p_k())
                print("p0=", obj_picm.p_n(0))
                print("l=", obj_picm.l())
                print("lq=", obj_picm.l_q())
                print("ln=", obj_picm.l_n())
                print("w=", obj_picm.w())
                print("wq=", obj_picm.w_q())
                print("wn=", obj_picm.w_n())
                print("pn", obj_picm.generarPn())
                print(data)"""
            else:
                print("Sistema no valido")
            return render_template(
                'data.html',
                nav=data,
                rho=obj_picm.rho(),
                rho_k=obj_picm.rho_k(),
                estabilidad=obj_picm.estabilidadSistema(),
                p0=obj_picm.p_cero(),
                pk=obj_picm.p_k(),
                pne=obj_picm.complemnto_p(),
                l=obj_picm.l(),
                lq=obj_picm.l_q(),
                ln=obj_picm.l_n(),
                w=obj_picm.w(),
                wq=obj_picm.w_q(),
                wn=obj_picm.w_n(),
                pn=obj_picm.generarPn()
            )
        else:
            print("PF")
            obj_pfcm = pfcm(int(data["k"]), float(data["mu"]), float(data["lambda"]), int(data["m"]))
            print("p0_parte1", obj_pfcm.p_cero_parte1())
            print("p0_parte2", obj_pfcm.p_cero_parte2())
            print("p0", obj_pfcm.p_cero())
            print(obj_pfcm.generarPn())
            print("pe", obj_pfcm.p_e())
            print("pne", obj_pfcm.p_ne())
            print("l", obj_pfcm.l())
            print("lq", obj_pfcm.l_q())
            print("ln", obj_pfcm.l_n())
            print("w", obj_pfcm.w())
            print("wq", obj_pfcm.w_q())
            print("wn", obj_pfcm.w_n())
            return "Hola"

    return render_template('index.html')



@app.route("/show", methods=['GET', 'POST'])
def show():
    return render_template('data.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)