from static.codes.COSTOS import costo


class experimentacion:

    def __init__(self, picm, dl, cs, cu, costo):
        self.picm = picm
        self.dl = dl
        self.cs = cs
        self.cu = cu
        self.costo = costo

    def datos(self):
        exp = []
        for k in range(1, 6):
            self.picm.k = k
            if self.picm.rho_k() < 1:
                print('k', self.picm.k)
                obj_costo = costo(
                    self.picm.k,
                    self.picm._lambda,
                    self.picm.w_q(),
                    self.picm.w(),
                    self.picm.mu,
                    self.dl,
                    self.cs,
                    self.cu,
                    self.costo
                )
                exp.append({'k': self.picm.k, 'ct': obj_costo.c_t()})
                print('ct', obj_costo.c_t())
        print(min(exp, key=lambda x: x['ct']))
        return exp