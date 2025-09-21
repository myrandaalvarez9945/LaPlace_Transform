import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

t, s = sp.symbols('t s', real=True)
xF = sp.Function('x')
FF = sp.Function('F')
x = xF(t); F_t = FF(t)
X, F = sp.symbols('X F')
m, B, k = sp.symbols('m B k', positive=True, real=True)

transformations = standard_transformations + (implicit_multiplication_application,)

def laplace_zero_ic(expr):
    # Replace x(t) -> X, x'(t)-> s*X, x''(t)-> s^2*X ; F(t)->F
    expr = sp.simplify(expr.replace(
        lambda e: isinstance(e, sp.Derivative) and e.expr == x,
        lambda e: s**(len([v for v in e.variables if v==t])) * X
    ))
    return expr.xreplace({x: X, F_t: F})

print("Enter your TIME-DOMAIN equation (e.g., m*diff(x(t),t,2) + B*diff(x(t),t) + k*x(t) - F(t) = 0)")
line = input("Eq: ").strip()

if '=' in line:
    lhs_str, rhs_str = line.split('=', 1)
    lhs = parse_expr(lhs_str, transformations=transformations, local_dict={
        't': t, 'x': xF, 'F': FF, 'diff': sp.diff, 'm': m, 'B': B, 'k': k
    })
    rhs = parse_expr(rhs_str, transformations=transformations, local_dict={
        't': t, 'x': xF, 'F': FF, 'diff': sp.diff, 'm': m, 'B': B, 'k': k
    })
else:
    lhs = parse_expr(line, transformations=transformations, local_dict={
        't': t, 'x': xF, 'F': FF, 'diff': sp.diff, 'm': m, 'B': B, 'k': k
    })
    rhs = 0

eq_time = sp.Eq(lhs, rhs)
print("\nTime-domain equation you entered:")
sp.pprint(eq_time)


E = sp.simplify(eq_time.lhs - eq_time.rhs)
E_L = laplace_zero_ic(E)

print("\nLaplace-domain (zero IC) equation == 0:")
sp.pprint(E_L)

# Solve for X/F: coefficient of X is (m s^2 + B s + k)
A = sp.expand(E_L).coeff(X, 1)     
Bforce = -sp.expand(E_L).coeff(F, 1)  

G = sp.simplify(Bforce / A)  # X/F
print("\nTransfer function  X(s)/F(s) =")
sp.pprint(sp.factor(G))