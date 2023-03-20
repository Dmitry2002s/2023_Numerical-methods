# -*- coding: cp1251 -*-

import sympy

from sympy.abc import x 

f = sympy.exp(6*x) 

print(f.evalf(subs = {x : 6})) 