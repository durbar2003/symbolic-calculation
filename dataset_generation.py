from sympy import symbols, diff, cos, sin, exp
import numpy as np

# Define symbols for x and the variables for the derivatives
x = symbols('x')
x0 = symbols('x0')
h = symbols('h')
f = symbols('f')

# Define the functions to be used in the dataset
functions = [cos(x), sin(x), exp(x)]

# Define the order of the Taylor expansion
order = 4

# Generate the dataset
dataset = []
for func in functions:
    # Calculate the Taylor expansion up to the specified order
    taylor_expansion = func.series(x, x0, n=order+1).removeO().subs(x0, 0)
    
    # Tokenize the function and its Taylor expansion
    function_tokens = np.array(str(func).replace(' ', '').replace('**', '^').split(' '))
    taylor_tokens = np.array(str(taylor_expansion).replace(' ', '').replace('**', '^').split(' '))
    
    # Append the function and its Taylor expansion to the dataset
    dataset.append((function_tokens, taylor_tokens))

# Print the generated dataset
print(dataset)
