class costo:
    def __init__(self, k, _lambda, wq, w, mu, dl, cs, cu, sw, l):
        self.k = k
        self._lambda = _lambda
        self.wq = wq
        self.w = w
        self.mu = 1 / mu
        self.dl = dl
        self.cs = cs
        self.cu = cu
        self.sw = sw
        self.l = l

    # C. totales
    # C. diario tiempo cola
    def c_t_te(self):
        if self.sw == 'TE':
            return self._lambda * self.dl * self.wq * self.cu
        else:
            return 0

    # C. diario tiempo sistema
    def c_t_ts(self):
        if self.sw == 'TS':
            print("w:", self.w)
            print("lambda:", self._lambda)
            print("Horas:", self.dl)
            print("Costo:", self.cu)
            return self.l * self.dl * self.cu
        else:
            return 0

    # C. diario tiempo servicio
    def c_t_tse(self):
        if self.sw == 'TSE':
            return self._lambda * self.dl * self.mu * self.cu
        else:
            return 0

    # C. diarios servidor
    def c_t_s(self):
        return self.k * self.cs * self.dl

    def c_t(self):
        return self.c_t_s() + self.c_t_ts() + self.c_t_te() + self.c_t_tse()

    def reporte_costos(self):
        return {'ctte': self.c_t_te(), 'ctts': self.c_t_ts(), 'cttse': self.c_t_tse(), 'cts': self.c_t_s(), 'ct': self.c_t()}