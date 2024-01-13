import numpy as np


def main():
    a = np.array([[1., 2.], [3., 4.]])
    y = np.array([[5.], [7.]])
    print(a)
    a_t = np.array([[1., 3.], [2., 4.]])
    print(a_t)
    b = np.eye(2)
    print(b)
    tr_b = b[1][1] + b[0][0]
    print(tr_b)
    print(np.linalg.solve(a, y))


if __name__ == "__main__":
    main()