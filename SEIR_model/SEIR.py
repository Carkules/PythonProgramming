"""
This script solves SEIR model with given parameters and draws a diagram.
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import argparse

def seir(SEIR, t, N, beta, delta, gamma):
    (S, E, I, R) = SEIR
    
    dSdt = -beta*S*I/N
    dEdt = beta*S*I/N - delta*E
    dIdt = delta*E - gamma*I
    dRdt = gamma*I

    return dSdt, dEdt, dIdt, dRdt

def draw_diagram(N, S0, E0, I0, R0, beta, sigma, gamma):

    if not N == S0 + E0 + I0 + R0:
        raise ValueError("S+E+I+R is not equal to N")

    t = np.linspace(0, 100)
    SEIR0 = (S0, E0, I0, R0)

    result = odeint(seir, SEIR0, t, args=(N, beta, sigma, gamma))
    S, E, I, R = result.T

    plt.plot(t, S, label="Susceptible")
    plt.plot(t, E, label="Exposed")
    plt.plot(t, I, label="Infectious")
    plt.plot(t, R, label="Recovered")
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-N', type=float, default=1000)
    parser.add_argument('-S0', type = float, default=999)
    parser.add_argument('-E0', type = float, default=1)
    parser.add_argument('-I0', type = float, default=0)
    parser.add_argument('-R0', type = float, default=0)
    parser.add_argument('-beta', type = float, default=1.34)
    parser.add_argument('-sigma', type = float, default=0.19)
    parser.add_argument('-gamma', type = float, default=0.34)

    args = parser.parse_args()

    draw_diagram(args.N, args.S0, args.E0, args.I0, args.R0, args.beta, args.sigma, args.gamma)
