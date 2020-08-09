from sympy.solvers.solveset import nonlinsolve


__PLACEHOLDER_VALUE__ = 1


def solve_system(system: list, variables: list) -> dict:
    """Finds a solution of given system of equations"""

    solution_set = nonlinsolve(system, variables)                   # FiniteSet of possible solutions

    solution = solution_set.args[0]                                 # A solution from solution_set
    solution_value = []                                             # Calculated solution (list of float)
    subs_map = {item: __PLACEHOLDER_VALUE__ for item in variables}
    for expr in solution:
        solution_value.append(float(expr.subs(subs_map)))
    solution_map = dict(zip([item.name for item in variables], solution_value))
    
    return solution_map



