from math import factorial


class pfcm:

    def __init__(self, k, mu, _lambda, m):
        self.k = k
        self.mu = mu
        self._lambda = _lambda
        self.m = m

    def rho_k(self):
        return self._lambda / (self.k * self.mu)

    def rho(self):
        return self._lambda / self.mu

    def estabilidadSistema(self) -> object:
        if self.rho_k() > 1:
            return False
        else:
            return True

    # Calculo de p
    # Probalidad de encontrar
    def m_fac(self) -> object:
        return factorial(self.m)

    def rho_n(self, n):
        return self.rho() ** n

    def p_cero_parte1(self):
        sum1 = 0
        for n in range(self.k):
            sum1 += (self.m_fac() / (factorial(self.m - n) * factorial(n))) * self.rho_n(n)
        return sum1

    def p_cero_parte2(self):
        sum2 = 0
        for n in range(self.k, self.m + 1):
            sum2 += (self.m_fac() / ((factorial(self.m - n)) * factorial(self.k) * (self.k ** (n - self.k)))) * self.rho_n(n)
        return sum2

    def p_cero(self):
        return 1 / (self.p_cero_parte1() + self.p_cero_parte2())

    def p_n(self, n):
        if n >= self.k:
            part1 = factorial(self.m) / (factorial(self.m - n) * (factorial(self.k) * (self.k ** (n - self.k))))
            part2 = self.rho_n(n)
            part3 = self.p_cero()
            return part3 * part2 * part1
        else:
            parte_1 = (self.p_cero() * factorial(self.m)) / (factorial(self.m - n) * factorial(n))
            parte_2 = self.rho() ** n
            return parte_1 * parte_2

    def generarPn(self):
        cpn = self.p_cero()
        # dic = []
        dic = [{'n': '0', 'pn': str(cpn), 'cpn': str(cpn), 'ccpn': str(1-cpn)}]
        for i in range(1, self.m + 1):
            cpn += self.p_n(i)
            dic.append({'n': i, 'pn': self.p_n(i), 'cpn': str(cpn), 'ccpn': str(1-cpn)})
        return dic

    def p_e(self):
        pe = 0
        for n in range(self.k):
            pe += self.p_n(n)
        return 1 - pe

    def p_ne(self):
        return 1 - self.p_e()

    # Calculo de L
    # Numero esperado de
    def l_part1(self):
        l1 = 0
        for n in range(self.k):
            l1 += n * self.p_n(n)
        return l1

    def l_part2(self):
        l2 = 0
        for n in range(self.k, self.m + 1):
            l2 += (n - self.k) * self.p_n(n)
        return l2

    def l(self):
        return self.l_part2() + self.l_part1() + (self.k * self.p_e())

    def l_q(self):
        return self.l_part2()

    def l_n(self):
        return self.l_q() / self.p_e()

    # Calculo de W
    # tiempo esperado
    def w_q(self):
        return self.l_q() / ((self.m - self.l()) * self._lambda)

    def w(self):
        return self.w_q() + (1 / self.mu)

    def w_n(self):
        return self.w_q() / self.p_e()
