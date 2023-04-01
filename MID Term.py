import sympy as sym
import matplotlib.pyplot as plt

t = sym.symbols('t')
y = sym.Function('y')(t)

k_vals = [0.1, 0.2, 0.5]
initial_condition = {y.subs(t, 0): 5}

solutions = {}
for k_val in k_vals:
    differential_equation = sym.diff(y, t) + k_val*y
    solution = sym.dsolve(differential_equation, ics=initial_condition).rhs
    solutions[k_val] = solution

for k_val, solution in solutions.items():
    time_values = [i/10 for i in range(101)]
    y_values = [solution.subs(t, t_val) for t_val in time_values]
    plt.plot(time_values, y_values, label=f'k={k_val}')

plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.legend()
plt.show()
