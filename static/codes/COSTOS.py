    from 
   class costo:
   
    
    def __init__(self, k, mu, _lambda, h_labo, c_s):
        self.k = k
        self.mu = mu
        self._lambda = _lambda
        self.h_labo = h_labo
        self.c_s = c_s
        
    #Calculo de Costos
    #Costos unitarios

    #C. unitaio en cola
    def c_u_c(self):
      return
      
    #C. unitario sistema
    def c_u_ts(self):
      return
      
    #C. unitario servicio
    def c_u_tse(self):
      return 
      
    #C. totales
      
    #C. diario tiempo cola
    def c_t_te(self):
      return self.lambda * self.h_labo * self.w_q() * self.c_u_c()
      
    #C. diario tiempo sistema
    def c_t_ts(self):
      return self.lambda * self.h_labo * self.w() * self.c_u_ts()
      
    #C. diario tiempo servicio
    def c_t_tse(self):
      return self.lambda * self.h_labo * (1/self.mu) *  self.c_u_tse()
      
    #C. diarios servidor
    def c_t_s(self):
      return self.k * self.c_s
