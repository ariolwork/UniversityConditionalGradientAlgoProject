import sympy.abc 
import sympy
from sympy import *
from sympy.core.sympify import kernS
import sympy.abc 
import copy

from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication, function_exponentiation, convert_xor, rationalize)
transformations = standard_transformations + (implicit_multiplication,) + (function_exponentiation,) + (convert_xor,) + (rationalize,)
a,b,c,d,x,y,z,u,v,w = symbols('a b c d x y z u v w') 

def get_func_and_st_der(str):
    f = parse_expr(str, transformations=transformations)
    def f1(u):   
        parat = []
        fr_sy = list(f.free_symbols)
        for i  in range(0,len(fr_sy)):
            parat.append((fr_sy[i], u[i]))
        return f.subs(parat).evalf()

    def get_standart_der(u):
        der = []
        eps = 0.0000001
        for i in range(0, len(u)):
            u1 = copy.copy(u)
            u1[i] = u1[i]+eps
            der.append((f1(u1)-f1(u))/eps)
            u1[i] = u[i]-eps
        return der

    return f1, get_standart_der


#expr = parse_expr("x**2 + sin(y) + S(10)/2", transformations=transformations)
#print(expr.subs([(x,1),(y,2)]).evalf())
#f, der = get_func_and_st_der("x^2+x*y+y^2")
#print(f([1, 9]))
#print(der([1,9]))