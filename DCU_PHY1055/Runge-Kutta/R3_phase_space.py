import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from pathlib import Path

def simple_pendulum(t, y):
    x, v = y
    dydt = np.array([v, -x])
    return dydt

def generate_path(home_folder=str(Path.home()), subfolder='/Documents/', basename='output', extension='png'):
    output_folder = home_folder + subfolder
    filename = basename + '.' + extension
    output_path = output_folder + filename
    return output_path

def phase_space(x, v):
    plt.figure()
    plt.plot(v, x, 'k')
    plt.axis('equal')
    plt.xlabel(r"$x$")
    plt.ylabel(r"$v$")


def plot_time_dependency(t, x, v):
    plt.figure()
    plt.plot(t, x, label=r"$x(t)$")
    plt.plot(t, v, label=r"$v(t)$")
    plt.xlabel("Time (t)")
    plt.ylabel("Position (x) and Velocity (v)")

    plt.legend(loc=1)

def main():
    x0 = 0
    v0 = 1
    y0 = (x0, v0)
    t0 = 0
    tf = 10*np.pi
    n = 1001
    t = np.linspace(t0, tf, n)

    result = integrate.solve_ivp(fun=simple_pendulum, t_span=(t0, tf), y0=y0, method="RK45", t_eval=t)
    x, v = result.y
    t = result.t

    # Create a figure with two subplots
    fig, axs = plt.subplots(2)
    plot_time_dependency(t, x, v)
    phase_space(x, v)
    plt.tight_layout()

    filename = generate_path(basename='Harmonic-init', extension='png')
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    plt.show()

if __name__ == '__main__':
    main()
