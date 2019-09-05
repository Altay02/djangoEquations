from sympy import *
from random import *

x, a, b, c = symbols('x a b c')
x1 = choice([i / 10 for i in range(-100, 105, 5)])
x2 = choice([i / 10 for i in range(-100, 105, 5)])
x3 = choice([i / 10 for i in range(-100, 105, 5)])
na = randint(1,4)
temp = na
x1 = Rational(x1, na)[0]
x2 = Rational(x2, na)[0]

nb = na * (-x1 - x2)
nc = na * x1 * x2
f = expand(na*(x - x1)*(x - x2))
print(x1, x2)
print (f)
f = simplify(f)
print(f)
print(na, nb, nc)
