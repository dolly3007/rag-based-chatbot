# tools/physics_solver.py
from sympy import symbols, Eq, solve
import re

def solve_physics_equation(expr: str) -> str:
    try:
        expr = expr.strip().replace("^", "**")
        x = symbols("x")
        lhs, rhs = expr.split("=")
        eq = Eq(eval(lhs), eval(rhs))
        solutions = solve(eq, x)
        return f"Solution: {solutions}"
    except Exception as e:
        return f"Error solving equation: {e}"
