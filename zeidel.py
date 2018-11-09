import numpy as np

def zeidel(a: np.ndarray, b: np.ndarray, accurency: float):
    C = np.zeros(a.shape)
    for i, raw in enumerate(a):
        C[i] = raw/a[i][i]
    C = C - np.tril(C) + np.tril(C, k=-1)
    D = []
    for idx in range(a.shape[0]):
        D.append([b[idx]/a[idx][idx]])
    D = np.array(D)
    Rs = []
    Rs.append(np.zeros(shape=b.shape))
    while True:
        new = Rs[-1].copy()
        for i in range(3):
            tmp_d, tmp_c = D[i][0], C[i]
            x = np.around(tmp_d - tmp_c.dot(new), decimals=3)
            new[i][0] = x
        Rs.append(new)
        if abs(Rs[-1] - Rs[-2]).max() < accurency:
            return Rs

