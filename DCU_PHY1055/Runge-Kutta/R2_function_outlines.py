import numpy as np
import matplotlib.pyplot as plt
def differential_rl(v, r, l, i, h):
    """
    Calculates the change in current over time from the formula
    L(dI/dt) = V - RI
    :param v: Float for voltage
    :param r: Float for resistance
    :param l: Float for inductance
    :param i: Float for current
    :param h: Float for time step
    :return: The new current value
    """
    di_dt = (v - r * i) / l
    new_i = i + h * di_dt
    return new_i
def exact_solution_rl(v, r, l, t):
    """
    Calculates the exact solution for the current over time from the formula
    I = (V/R)(1-exp(-Rt/L))
    :param v: Float for voltage
    :param r: Float for resistance
    :param l: Float for inductance
    :param t: Float for time
    :return: The exact current value
    """
    return (v / r) * (1 - np.exp(-r * t / l))
def main():
    v = 10  # voltage
    r = 50  # resistance
    l = 100  # inductance
    i0 = 0  # initial current
    t_max = 10  # maximum time
    h = 0.5  # time step

    t = np.arange(0, t_max, h)
    i_approx = np.zeros(len(t))
    i_approx[0] = i0

    for n in range(1, len(t)):
        i_approx[n] = differential_rl(v, r, l, i_approx[n-1], h)

    i_exact = exact_solution_rl(v, r, l, t)

    plt.plot(t, i_approx, label='Approximate Solution')
    plt.plot(t, i_exact, label='Exact Solution')
    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')
    
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
