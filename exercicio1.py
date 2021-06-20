"""
    AG001 - Avaliação Global INATEL

    PRIMEIRO EXERCICO - LIMITS

    Autor: Ítalo Thalyson de Moura
"""

# Import de bibliotecas para ser feito os calculos
from sympy import Limit, Symbol, S

# Constante C, minha matricula(96) resto por 10
c = 96 % 10

def func(x):
    return (3*x**3 - 3) / (4*x**2 - 4) * (c+1)

x = Symbol('x')

###### EXERCICIO 1 -> PRIMEIRO LIMIT
#Calcula limite da função quando x -> 1.
res = Limit(func(x), x, 1).doit()

print('Limite para x -> 1.')
print(res)

###### EXERCICIO 1 -> SEGUNDO LIMIT
#Calcula limite da função quando x -> oo.
res = Limit(func(x), x, S.Infinity).doit()

print('Limite para x -> oo.')
print(res)

###### EXERCICIO 1 -> TERCEIRO LIMIT
#Calcula limite da função quando x -> -oo.
res = Limit(func(x), x, -S.Infinity).doit()

print('Limite para x -> oo.')
print(res)