from sympy import *
from random import *
from sympy.polys import Poly

def NOK(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)

def squareEq(strName):
    x = symbols(strName)
    temp = choice((1, 2, 3))
    x1 = Rational(choice([i for i in range(-10, 10, 1)]), temp)
    x2 = Rational(choice([i for i in range(-10, 10, 1)]), temp)
    x3 = choice([i / 10 for i in range(-100, 105, 5)])
    nab = fraction(Rational(-x1 - x2, 1))[1]
    nb = fraction(Rational(-x1 - x2, 1))[0]
    nac = fraction(Rational(x1 * x2, 1))[1]
    nc = fraction(Rational(x1 * x2, 1))[0]
    na = NOK(nac, nab)
    #if not (type(na / nab) is int):
    #    raise TypeError('alalanab:' + (na / nab))
    #if not (type(na / nac) is int):
    #    raise TypeError('alalanac:' + (na / nac))
    nb = nb * (na / nab)
    nc = nc * (na / nac)
    f = expand(na*(x - x1)*(x - x2))
    return f

def linearEq(strName):
    x = symbols(strName)
    xMult = choice([i for i in range(1, 5)])
    if (random() > 0.8):
        f = xMult * x
    else:
        f = xMult * x - Rational(choice([i for i in range(-10, 10, 1)]), choice((1, 2)))
    return f

def randomEq(strName):
    if (random() > 0.5):
        return linearEq(strName)
    else:
        return squareEq(strName)

def parametr1(strNameParametr='a', strNameVariable='x'):
    temp = differentSigns()
    temp.a = randomEq(strNameParametr)
    temp.b = randomEq(strNameParametr)
    temp.c = randomEq(strNameParametr)
    temp.x = symbols(strNameVariable)
    temp.f = temp.a * temp.x**2 + temp.b * temp.x + temp.c #Poly(temp.a * temp.x**2 + temp.b * temp.x + temp.c, temp.x)[0]
    a = symbols('a')
    temp.ans = solve_poly_inequality(Poly(temp.a * temp.c, a, domain='ZZ'), '<')
    temp.ans = tuple(temp.ans)
    return temp



class differentSigns:
    a, b, c, x, f = symbols('a b c x f')


i = 0
