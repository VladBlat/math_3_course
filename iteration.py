import numpy as np

def SimpleIterationRoots(A: np.ndarray, B: np.ndarray, accurency: float):
    C = np.array([[A[i][j] / (-A[i][i]) for j in range(A.shape[1])]\
                  for i in range(A.shape[0])])
    for i in range(C.shape[0]):
        C[i][i] = 0

    D = np.array([(B[x] / A[x][x]) for x in range(A.shape[0])])
    X = []
    X.append(np.array([[0], [0], [0]]))

    done = False

    while not done:
        X.append(np.around(C.dot(X[-1]) + D, decimals=3))
        if abs(X[-1] - X[-2]).max() < accurency:
            return X

