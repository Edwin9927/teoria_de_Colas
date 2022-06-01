class costo:
    def __init__(self, k, _lambda, wq, w, mu, dl, cs, cu, sw):
        self.k = k
        self._lambda = _lambda
        self.wq = wq
        self.w = w
        self.mu = 1 / mu
        self.dl = dl
        self.cs = cs
        self.cu = cu
        self.sw = sw

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
            return self._lambda * self.dl * self.w * self.cu
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
        return self.k * self.cs

    def c_t(self):
        return self.c_t_s() + self.c_t_ts() + self.c_t_te() + self.c_t_tse()
