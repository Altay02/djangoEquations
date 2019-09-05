from django.shortcuts import render
from sympy import *
from random import *
from sympy.polys import Poly
from sympy.printing.mathml import print_mathml
from sympy.printing.mathml import mathml
# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={},
    )

def differentSigns(request):
    class differentSign:
        a, b, c, x, f = symbols('a b c x f')
	
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
        nab = fraction(Rational(-x1 - x2, 1))[1]
        nb = fraction(Rational(-x1 - x2, 1))[0]
        nac = fraction(Rational(x1 * x2, 1))[1]
        nc = fraction(Rational(x1 * x2, 1))[0]
        na = NOK(nac, nab)
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
        temp = differentSign()
        temp.a = randomEq(strNameParametr)
        temp.b = randomEq(strNameParametr)
        temp.c = randomEq(strNameParametr)
        temp.x = symbols(strNameVariable)
        temp.f = Poly(temp.a * temp.x**2 + temp.b * temp.x + temp.c, temp.x).as_expr()
        a = symbols('a')
        temp.ans = solve_poly_inequality(Poly(temp.a * temp.c, a), '<')
        temp.ans = tuple(temp.ans)
        return temp
    f = parametr1()
    fString = mathml(simplify(f.f), 'presentation') # print_mathml
    fAns = mathml(f.ans, 'presentation') # mathml

    	
    return render(
        request,
        'differentSign.html',
        context={'equation':fString,'ans':fAns},
    )