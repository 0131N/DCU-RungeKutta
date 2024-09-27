import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from pathlib import Path

def damped_pendulum(t, y, b, omega0):
    x, v = y
    dxdt = v
    dvdt = -b*v-(omega0**2)*x
    dydt = np.array([dxdt, dvdt])
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
    b = 0.5  # damping coefficient
    omega0 = 1.2  # resonant frequency

    lfun = lambda t, y: damped_pendulum(t, y, b, omega0)

    result = integrate.solve_ivp(fun=lfun,  # The function defining the derivative
                                 t_span=(t0, tf),  # Initial and final times
                                 y0=y0,  # Initial state
                                 method="RK45",  # Integration method
                                 t_eval=t)  # Time points for result to be defined at

    x, v = result.y
    t = result.t

    plot_time_dependency(t, x, v)
    phase_space(x, v)

    filename = generate_path(basename='Damped-Pendulum', extension='png')
    plt.savefig(filename, bbox_inches='tight')
    print("Output file saved to {}.".format(filename))
    plt.show()

if __name__ == '__main__':
    main()
