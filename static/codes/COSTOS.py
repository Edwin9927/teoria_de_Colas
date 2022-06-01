class costo:
    def __init__(self, k, _lambda, wq, w, mu, dl, cs, cu):
        self.k = k
        self._lambda = _lambda
        self.wq = wq
        self.w = w
        self.mu = 1 / mu
        self.dl = dl
        self.cs = cs
        self.cu = cu

    # C. totales

    # C. diario tiempo cola
    def c_t_te(self):
        return self._lambda * self.dl * self.wq * self.cu

    # C. diario tiempo sistema
    def c_t_ts(self):
        return self._lambda * self.dl * self.w * self.cu

    # C. diario tiempo servicio
    def c_t_tse(self):
        return self._lambda * self.dl * self.mu * self.cu

    # C. diarios servidor
    def c_t_s(self):
        return self.k * self.cs

    def c_t(self):
        return self.c_t_s() + self.c_t_ts()
