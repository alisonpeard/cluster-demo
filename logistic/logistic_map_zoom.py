import os, sys

import numpy as np
import matplotlib.pyplot as plt


def logistic(r, x):
    return r * x * (1 - x)


def logistic_series(r, x0=0.1, N=1000):
    x = [x0]
    for i in range(N - 1):
        x.append(logistic(r, x[-1]))
    return x


def plot_logistic_map(r_min, r_max, filename, steps=5000):
    last_n_values = 500
    logistic_result = []
    r_input = []
    for r in np.linspace(r_min, r_max, steps):
        r_input.append([r] * last_n_values)
        logistic_result.append(logistic_series(r)[-last_n_values:])

    f, ax = plt.subplots(figsize=(13, 6))
    ax.scatter(r_input, logistic_result, s=0.001)
    ax.set_xlabel(r"$r$")
    ax.set_ylabel(r"$\mathrm{logistic}(r, x)$")
    f.savefig(filename)
    plt.close(f)


if __name__ == "__main__":

    _, job_id = sys.argv

    with open("params.txt", "r") as fp:
        lines = fp.readlines()

    line_num = int(job_id) - 1
    min_r, max_r = lines[line_num].split()

    os.makedirs("plots", exist_ok=True)
    plot_logistic_map(float(min_r), float(max_r), f"plots/plot_{line_num:03d}.png")
