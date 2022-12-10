import numpy as np

from src.AHP.rating import rate, get_koczkodaj_index


def main():
    pairwise_comps = [np.matrix([[1,  1/7,  1/5],
                                 [7,  1,    3],
                                 [5,  1/3,  1]]),
                      np.matrix([[1, 1 / 3, 5],
                                 [3, 1, 7],
                                 [1 / 5, 1 / 7, 1]])]
    # pairwise_comps = [np.matrix([[1,  10,  10],
    #                              [10.1,  1,  10],
    #                              [10.1,  10.1,  1]], dtype=float),
    #                   np.matrix([[1, 1 / 3, 5],
    #                              [3, 1, 7],
    #                              [1 / 5, 1 / 7, 1]])]

    print(rate(pairwise_comps,
        np.matrix([[1, 1 / 2],
                   [2, 1]], dtype=float)))

    print([get_koczkodaj_index(pc) for pc in pairwise_comps])

if __name__ == "__main__":
    main()
