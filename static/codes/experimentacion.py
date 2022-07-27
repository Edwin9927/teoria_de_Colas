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
        for k in range(1, 11):
            self.picm.k = k
            if self.picm.rho_k() < 1:
                #print('k', self.picm.k)
                obj_costo = costo(
                    self.picm.k,
                    self.picm._lambda,
                    self.picm.w_q(),
                    self.picm.w(),
                    self.picm.mu,
                    self.dl,
                    self.cs,
                    self.cu,
                    self.costo,
                    self.picm.l()
                )
                exp.append({'k': self.picm.k,
                            'p0': self.picm.p_cero(),
                            'l': self.picm.l(),
                            'lq': self.picm.l_q(),
                            'ln': self.picm.l_n(),
                            'w': self.picm.w(),
                            'wq': self.picm.w_q(),
                            'wn': self.picm.w_n(),
                            'ct': obj_costo.c_t()})
        return exp

    def costo_optimo(self):
        return min(self.datos(), key=lambda x: x['ct'])
