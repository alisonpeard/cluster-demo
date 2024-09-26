import numpy as np

if __name__ == "__main__":

    n_frames = 100
    max_r = 3.86

    arr = np.logspace(1, np.log10(1000), n_frames) / 1000
    arr = np.insert(arr, 0, 0)
    min_r = np.ones_like(arr) * max_r - arr[::-1] * max_r

    with open("params.txt", "w") as fp:
        for value in min_r[:-1]:
            fp.write(f"{value:.6E} {max_r:.6E}\n")
