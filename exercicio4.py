"""
    AG001 - Avaliação Global INATEL

    QUARTO EXERCICO - LEIS DE KIRCHOFF

    Autor: Ítalo Thalyson de Moura
"""
from sympy import Symbol, solve, linsolve

# Constante C, minha matricula(96) resto por 10
c = 96 % 10

v1 = 10 + (2 * c)
v2 = 5 + (2 * c)

# Equação para determinar corrente das malhas adotodas Ia e Ib
def equacI(Ia, Ib):
    return 35*Ia - 10*Ib - v1

# Equação para determinar corrente das malhas adotodas Ia e Ib
def equacII(Ia, Ib):
    return -10*Ia + 30*Ib + v2

# verificando se valor da corrente é +, se for - irei multiplicar por -1 pois adotei polaridade incorreta
def verifyCorrente(I):
    if(I < 0):
        return I*-1
    return I


Ia = Symbol('Ia')
Ib = Symbol('Ib')
I = Symbol('I')


eqcI1 = equacI(Ia,Ib)
eqcI3 = equacII(Ia,Ib)

# I1 = eqcI1  /// I3 = eqcI3
res = solve((eqcI1, eqcI3))

#Verificando polarização e adicionando as variaveis
I1 = verifyCorrente(res[Ia])
I3 = verifyCorrente(res[Ib])
# I2 = I3 - I1
I2 = I3 - I1

print("Corrente I1 = ", I1)
print("Corrente I2 = ", verifyCorrente(I2))
print("Corrente I3 = ", I3)