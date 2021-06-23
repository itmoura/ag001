"""
    AG001 - Avaliação Global INATEL

    SEGUNDO EXERCICO - FÍSICA

    Autor: Ítalo Thalyson de Moura
"""

from sympy import Symbol, solve, Derivative
from math import exp

# Constante C, minha matricula(96) resto por 10
c = 96 % 10

def funcTraj(t):
    return -((t**3)/3) + 2*(t**2) - c

t = Symbol('t')

eqVel = Derivative(funcTraj(t), t, 1).doit()
velT = eqVel.subs(t, 3)
eqAcel = Derivative(funcTraj(t), t, 2).doit()
acelT = eqAcel.subs(t, 5)

print("Equação de Velocidade: ", eqVel)
print("Velocidade em t = 3: ", velT, "m/s")
print("Equação da aceleração: ", eqAcel)
print("Aceleração em t = 5: ", acelT, "m/s²")