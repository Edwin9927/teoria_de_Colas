from flask import Flask, request, render_template

from static.codes.COSTOS import costo
from static.codes.PFCM import pfcm
from static.codes.PICM import picm
from static.codes.experimentacion import experimentacion

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        # Determinar si el sistema es finito
        if data["m"] == '':
            obj_picm = picm(int(data["k"]), float(data["mu"]), float(data["lambda"]))

            # Determinar si la condicion del sistema es valido
            if obj_picm.estabilidadSistema():
                dl = 1
                # Determinar las horas de trabajo en un dia
                if data["dl"] == '':
                    pass
                else:
                    dl = int(data['dl'])
                # Determinar si se ingreso el costo del servidor
                if data["cs"] == '':
                    print("No hay costes")
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
                    obj_exp = experimentacion(
                        obj_picm,
                        int(data['dl']),
                        float(data['cs']),
                        float(data['cu']),
                        data['costo']
                    )

                    obj_costo = costo(
                        obj_picm.k,
                        float(data["lambda"]),
                        obj_picm.w_q(),
                        obj_picm.w(),
                        float(data["mu"]),
                        dl,
                        float(data['cs']),
                        float(data['cu']),
                        data['costo']
                    )
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
                        pn=obj_picm.generarPn(),
                        d_ct=obj_costo.reporte_costos(),
                        d_exp=obj_exp.datos(),
                        d_exp_opt=obj_exp.costo_optimo()
                    )

            else:
                print("Sistema no valido")

        else:
            obj_pfcm = pfcm(int(data["k"]), float(data["mu"]), float(data["lambda"]), int(data["m"]))

            # Determinar las horas de trabajo en un dia
            if data["dl"] == '':
                pass
            else:
                dl = int(data['dl'])

            # Determinar si se ingreso el costo del servidor
            if data["cs"] == '':
                print("No hay costes")
                return render_template(
                    'dataPFCM.html',
                    nav=data,
                    p0=obj_pfcm.p_cero(),
                    pe=obj_pfcm.p_e(),
                    pne=obj_pfcm.p_ne(),
                    l=obj_pfcm.l(),
                    lq=obj_pfcm.l_q(),
                    ln=obj_pfcm.l_n(),
                    w=obj_pfcm.w(),
                    wq=obj_pfcm.w_q(),
                    wn=obj_pfcm.w_n(),
                    pn=obj_pfcm.generarPn()
                )
            else:
                """print("Hay costes")
                obj_exp = experimentacion(
                    obj_pfcm,
                    int(data['dl']),
                    float(data['cs']),
                    float(data['cu']),
                    data['costo']
                )

                print("obj_exp:", obj_exp)"""

                obj_costo = costo(
                    obj_pfcm.k,
                    float(data["lambda"]),
                    obj_pfcm.w_q(),
                    obj_pfcm.w(),
                    float(data["mu"]),
                    dl,
                    float(data['cs']),
                    float(data['cu']),
                    data['costo']
                )

                print("obj_costo:", obj_costo)

                return render_template(
                    'dataPFCM.html',
                    nav=data,
                    p0=obj_pfcm.p_cero(),
                    pe=obj_pfcm.p_e(),
                    pne=obj_pfcm.p_ne(),
                    l=obj_pfcm.l(),
                    lq=obj_pfcm.l_q(),
                    ln=obj_pfcm.l_n(),
                    w=obj_pfcm.w(),
                    wq=obj_pfcm.w_q(),
                    wn=obj_pfcm.w_n(),
                    pn=obj_pfcm.generarPn(),
                    d_ct=obj_costo.reporte_costos()
                )

    return render_template('index.html')


@app.route("/show", methods=['GET', 'POST'])
def show():
    return render_template('data.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
