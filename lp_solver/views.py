# lp_solver/views.py

from django.shortcuts import render
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import os
from django.conf import settings
from .models import LPProblem
from .utils import generate_graph
from .forms import LPForm
from .models import LPProblem
from .forms import LPForm
import matplotlib
from django.shortcuts import render
from scipy.optimize import linprog
matplotlib.use('Agg')

# Home Page (Method selection)
def home(request):
    return render(request, 'lp_solver/home.html')

# Form Page for user to input data based on method selection
def form(request, method):
    if method == "graphical":
        return render(request, 'lp_solver/graphical_form.html', {'method': method})
    elif method == "simplex":
        return render(request, 'lp_solver/simplex_form.html', {'method': method})
    elif method == "transport":
        return render(request, 'lp_solver/transport_form.html', {'method': method})
    else:
        return render(request, 'lp_solver/home.html')

# Solve Graphical Representation Method
def solve_graphical(request):
    if request.method == 'POST':
        # Get user inputs for graphical method
        obj_x = float(request.POST.get('obj_x'))
        obj_y = float(request.POST.get('obj_y'))

        constraint_1_x = float(request.POST.get('constraint_1_x'))
        constraint_1_y = float(request.POST.get('constraint_1_y'))
        rhs_1 = float(request.POST.get('rhs_1'))

        constraint_2_x = float(request.POST.get('constraint_2_x'))
        constraint_2_y = float(request.POST.get('constraint_2_y'))
        rhs_2 = float(request.POST.get('rhs_2'))

        c = [-obj_x, -obj_y]
        A = [[constraint_1_x, constraint_1_y], [constraint_2_x, constraint_2_y]]
        b = [rhs_1, rhs_2]
        x_bounds = (0, None)
        y_bounds = (0, None)

        res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
        # result

        if res.success:
            result = f"Optimal Solution: x = {res.x[0]:.2f}, y = {res.x[1]:.2f}, Maximized Objective = {-res.fun:.2f}"
            graph_url = generate_graph(constraint_1_x, constraint_1_y, rhs_1, 
                                       constraint_2_x, constraint_2_y, rhs_2, 
                                       res.x[0], res.x[1])
            print("Sucess")
            print(f"Result: {result} | Type: {type(result)} | Message: {'result' if result else 'no result'}")
        else:
            result = "No solution found."
            graph_url = None
            print("No Success")

        return render(request, 'lp_solver/result.html', {'result': result, 'graph_url': graph_url})

    return render(request, 'home.html')

# Solve Simplex Method (Placeholder)
def solve_simplex(request):
    # Example Linear Program:
    # Maximize: z = 3x + 2y
    # Subject to:
    # 2x + y ≤ 20
    # 4x - 5y ≤ 10
    # x ≥ 0, y ≥ 0

    # Coefficients of the objective function (for maximization, minimize the negative)
    c = [-3, -2]

    # Coefficients of inequality constraints (left-hand side)
    A = [
        [2, 1],   # 2x + y ≤ 20
        [4, -5],  # 4x - 5y ≤ 10
        [-1, 0],  # x ≥ 0
        [0, -1]   # y ≥ 0
    ]

    # Right-hand side of inequality constraints
    b = [20, 10, 0, 0]

    # Solve the linear program
    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    if res.success:
        result = f"Optimal value: {-res.fun:.2f}, x: {res.x[0]:.2f}, y: {res.x[1]:.2f}"
    else:
        result = "No solution found."

    return render(request, 'lp_solver/result.html', {'result': result, 'method': 'Simplex Method'})
# Solve Transportation Method with Dynamic Inputs
def solve_transportation(request):
    if request.method == "POST":
        method = request.POST.get("transportation_method")
        
        # Get transportation matrix size and values
        rows = int(request.POST.get("rows"))
        cols = int(request.POST.get("cols"))
        cost_matrix = []
        supply = []
        demand = []

        # Get the cost matrix values from the form
        for i in range(rows):
            cost_matrix.append([int(request.POST.get(f"cost_{i}_{j}")) for j in range(cols)])

        # Get supply and demand values from the form
        for i in range(rows):
            supply.append(int(request.POST.get(f"supply_{i}")))
        for j in range(cols):
            demand.append(int(request.POST.get(f"demand_{j}")))

        # Placeholder for transportation methods
        solution = "Transportation method solution (To be implemented)"
        explanation = "Explanation of the method will go here."

        return render(request, 'lp_solver/result.html', {
            'method': method.replace("_", " ").title(),
            'solution': solution,
            'explanation': explanation
        })
    
    return render(request, 'lp_solver/home.html')

# Graph Generation for Graphical Method
def generate_graph(c1_x, c1_y, rhs1, c2_x, c2_y, rhs2, opt_x, opt_y):
    plt.figure(figsize=(6, 4))

    x = np.linspace(0, 10, 400)
    plt.plot(x, (rhs1 - c1_x * x) / c1_y, label=f'{c1_x}x + {c1_y}y <= {rhs1}')
    plt.plot(x, (rhs2 - c2_x * x) / c2_y, label=f'{c2_x}x + {c2_y}y <= {rhs2}')

    plt.fill_between(x, 0, (rhs1 - c1_x * x) / c1_y, alpha=0.3)
    plt.fill_between(x, 0, (rhs2 - c2_x * x) / c2_y, alpha=0.3)

    plt.plot(opt_x, opt_y, 'ro', label='Optimal Solution')
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Save the graph to media folder
    graph_path = os.path.join(settings.MEDIA_ROOT, 'meme.jpeg')
    plt.savefig(graph_path)
    plt.close()

    graph_url = f"{settings.MEDIA_URL}meme.jpeg"
    return graph_url
