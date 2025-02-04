import math

# Constants
x0 = 1.5
tol = 0.000001

# Initialization
iter = 0
diff = x0
x = x0

print(f"{iter} : {x}")

# Iterative process
while diff >= tol:
    iter += 1
    y = x
    x = (x / 2) + (1 / x)
    print(f"{iter} : {x}")
    
    diff = abs(x - y)

print(f"\nConvergence after {iter} iterations")

def bisection_method(f, a, b, tol, max_iter):
    left = a
    right = b
    i = 0  # Iteration counter

    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2  # Midpoint

        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p

    return p  # Approximate root

# Example usage:
# Define a function, e.g., f(x) = x^2 - 4
def f(x):
    return x**2 - 4

# Call the method with function, interval [a, b], tolerance, and max iterations
root = bisection_method(f, 0, 3, 1e-6, 100)
print("Approximate root:", root)

def fixed_point_iteration(g, p0, tol, max_iter):
    i = 1  # Iteration counter

    while i <= max_iter:
        p = g(p0)  # Compute the next approximation
        
        if abs(p - p0) < tol:  # Convergence check
            print(f"Approximate root: {p}, SUCCESS")
            return p  # Return the found root
        
        i += 1
        p0 = p  # Update for next iteration

    print("FAILURE")  # If max iterations are reached without convergence
    return None

# Example usage:
# Define a function g(x), e.g., g(x) = (x + 2/x) / 2 for solving x = g(x)
def g(x):
    return (x + 2/x) / 2

# Call the method with function g, initial guess, tolerance, and max iterations
root = fixed_point_iteration(g, 1.5, 1e-6, 100)

def newtons_method(f, df, p_prev, tol, max_iter):
    i = 1  # Iteration counter

    while i <= max_iter:
        if df(p_prev) != 0:  # Check if derivative is not zero
            p_next = p_prev - f(p_prev) / df(p_prev)  # Newton's formula

            if abs(p_next - p_prev) < tol:  # Convergence check
                print(f"Approximate root: {p_next}, SUCCESS")
                return p_next  # Return the found root
            
            i += 1
            p_prev = p_next  # Update for next iteration
        else:
            print("FAILURE: Derivative is zero")
            return None  # Unsuccessful due to zero derivative
    
    print("FAILURE: Max iterations performed")  # If max iterations reached
    return None

# Example usage:
# Define the function f(x) = x^2 - 4 and its derivative df(x) = 2x
def f(x):
    return x**2 - 4

def df(x):
    return 2*x

# Call the method with function f, its derivative df, initial guess, tolerance, and max iterations
root = newtons_method(f, df, 3, 1e-6, 100)
