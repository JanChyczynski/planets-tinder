import numpy as np

from src.AHP.rating import rate


def main():
    print("hello")
    print(rate([np.matrix([[1, 1 / 7, 1 / 5],
                     [7, 1, 3],
                     [5, 1 / 3, 1]]),
          np.matrix([[1, 1 / 3, 5],
                     [3, 1, 7],
                     [1 / 5, 1 / 7, 1]])],
         np.matrix([[1, 1 / 2],
                    [2, 1]], dtype=float)))


if __name__ == "__main__":
    main()
