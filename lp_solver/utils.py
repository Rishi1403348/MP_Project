# lp_solver/utils.py

import matplotlib.pyplot as plt
import numpy as np
import os
from django.conf import settings

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

    graph_path = os.path.join(settings.MEDIA_ROOT, 'graph.png')
    plt.savefig(graph_path)
    plt.close()

    graph_url = f"{settings.MEDIA_URL}graph.png"
    return graph_url
