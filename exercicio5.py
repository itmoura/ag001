"""
    AG001 - Avaliação Global INATEL

    QUINTO EXERCICO - EQUAÇÕES

    Autor: Ítalo Thalyson de Moura
"""

from sympy import Symbol, solve, sin, Derivative
from math import e
import numpy as np
import matplotlib.pyplot as plt

# Constante C, minha matricula(96) resto por 10
c = 96 % 10

def funcOne(x):
    return e**(x-3) + e**(x-1) + e**x - c -1

def funcTwo(x):
    return x**4 - 4*(x**3) + 3*x - c

def funcThree(x):
    return 4*sin((c + 1)*x) + 2

x = Symbol('x')

###### EXERCICIO 5 -> PRIMEIRA EQUAÇÃO
# Plota gráfico da função - Tende ao infinito, portanto gráfico será cortado onde foi limitado
p = np.linspace(-2,6)
plt.plot(p, funcOne(p))
plt.grid()
plt.show()

# Resolve a equação funcOne.
res = solve(funcOne(x))

print('Resposta da equação: e^(x-3) + e^(x-1) + e^x = c + 1')
print(res)
print("\n")
###### EXERCICIO 5 -> SEGUNDA EQUAÇÃO
# Plota gráfico da função - Tende ao infinito, portanto gráfico será cortado onde foi limitado
p = np.linspace(-2,6)
plt.plot(p, funcTwo(p))
plt.grid()
plt.show()

# Resolve a equação funcTwo
res = solve(funcTwo(x))

print('Resposta da equação: x^4 - 4*x^3 + 3*x = c')
print(res)

print('Resposta da equação Derivando: x^4 - 4*x^3 + 3*x = c')
print("Derivadando --> ", Derivative(funcTwo(x), x).doit())
print("\n")
###### EXERCICIO 5 -> TERCEIRA EQUAÇÃO
# Resolve a equação funcThree.
res = solve(funcThree(x))

print('Resposta da equação: 4sin[(c + 1)*x] = -2')
print(res)