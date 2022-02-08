from math import sqrt as square_root


def quadraticSolver(a, b, c):
    discriminant = b ** 2 - ( 4 * a * c )
    try:
        if discriminant > 0:
            solution_1 = (-b + square_root(discriminant)) // (2 * a)
            solution_2 = (-b - square_root(discriminant)) // (2 * a)
            return solution_1, solution_2
        elif discriminant == 0:
            solution = - b // (2 * a)
            return solution
        else:
            return "This quadratic equation has no solution"
    except ZeroDivisionError as err:
        return "Error:", err
   
        
    
    


print(quadraticSolver(1, -6, 5))



