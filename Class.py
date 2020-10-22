from unittest import result
from unicodedata import decimal

class ProyectoFinanzas:
    def __init__(self,):
        self.cuentasPersonales = 0.0
    def cuentaTotal(self):
        self.cuentasPersonales = result 
        return result

class Ingresos:
    def __init__(self,Ingresos):
        ProyectoFinanzas.__init__(self)
        self.Ingresos = Ingresos
    def sumIngresos(self):
        self.cuentasPersonales = (self.cuentasPersonales + self.Ingresos) 
        return self.cuentasPersonales

class Egresos:
    def __init__(self, Egresos):
        ProyectoFinanzas.__init__(self)
        self.Egresos = Egresos
    def nuevoEgreso(self): 
        self.cuentasPersonales =(self.cuentasPersonales - self.Egresos)
        return self.cuentasPersonales