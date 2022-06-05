from math import factorial


class picm:

    def __init__(self, k, mu, _lambda):
        self.k = k
        self.mu = mu
        self._lambda = _lambda
        
    def rho_k(self):
        return self._lambda / (self.k * self.mu)

    def rho(self):
        return self._lambda / self.mu

    def estabilidadSistema(self) -> object:
        if self.rho_k() > 1:
            return False
        else:
            return True

    def calculoPrevio(self):
        return (1 / factorial(self.k)) * ((self.rho()) ** self.k) * (
                (self.k * self.mu) / ((self.k * self.mu) - self._lambda))

    # Calculo de p
    # Probalidad de encontrar
    def p_cero(self):
        n = self.k - 1
        sum1 = 0
        while n >= 0:
            sum1 += (1 / factorial(n)) * ((self.rho()) ** n)
            n = n - 1
        sum2 = self.calculoPrevio()
        return 1 / (sum1 + sum2)

    def p_k(self):
        sum1 = self.calculoPrevio()
        sum2 = self.p_cero()
        return sum1 * sum2

    def complemnto_p(self):
        return 1 - self.p_k()

    def p_n(self, n):
        if n >= self.k:
            part1 = 1 / (factorial(self.k) * (self.k ** (n - self.k)))
            part2 = (self.rho()) ** n
            part3 = self.p_cero()
            return part3 * part2 * part1
        else:
            parte_1 = self.p_cero() / factorial(n)
            parte_2 = self.rho() ** n
            return parte_1 * parte_2

    def generarPn(self):
        cpn = self.p_cero()
        dic = [{'n': '0', 'pn': str(cpn), 'cpn': str(cpn), 'ccpn': str(1-cpn)}]
        for i in range(1, 31):
            cpn += self.p_n(i)
            dic.append({'n': i, 'pn': self.p_n(i), 'cpn': str(cpn), 'ccpn': str(1-cpn)})
        return dic

    # Calculo de L
    # Numero esperado de
    def l_part1(self):
        return (self.mu * self._lambda) * (self.rho() ** self.k)

    def l_part2(self):
        return (factorial(self.k - 1)) * (((self.k * self.mu) - self._lambda) ** 2)

    def l(self):
        return ((self.l_part1() / self.l_part2()) * self.p_cero()) + self.rho()

    def l_q(self):
        return (self.l_part1() / self.l_part2()) * self.p_cero()

    def l_n(self):
        return self.l_q() / self.p_k()

    # Calculo de W
    # tiempo esperado
    def w_part1(self):
        return self.mu * (self.rho() ** self.k)

    def w_part2(self):
        return self.l_part2()

    def w(self):
        return ((self.w_part1() / self.w_part2()) * self.p_cero()) + (1 / self.mu)

    def w_q(self):
        return (self.w_part1() / self.w_part2()) * self.p_cero()

    def w_n(self):
        return self.w_q() / self.p_k()


