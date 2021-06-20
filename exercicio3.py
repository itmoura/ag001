"""
    AG001 - Avaliação Global INATEL

    TERCEIRO EXERCICO - INTEGRAL

    Autor: Ítalo Thalyson de Moura
"""
from sympy import Integral, Symbol

# Constante C, minha matricula(96) resto por 10
c = 96 % 10

def func(x):
    return x**3 - 4*(x**2) + 5*x - c

x = Symbol('x')

#Calcula a integral definida para x entre 0 e 5.
Resultado = Integral(func(x), (x, 0, 5)).doit()

print ('Integral definida para x entre 0 e 5.')
print (Resultado)