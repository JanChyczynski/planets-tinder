from typing import List
from unittest import TestCase

import numpy as np

from src.AHP.rating import rate, get_koczkodaj_index


class Test(TestCase):
    @staticmethod
    def compare_with_eps(actual: List[float], expected: List[float], eps: float):
        for actual_el, expected_el in zip(actual, expected):
            assert abs(actual_el - expected_el) < eps

    def test_calculations_1(self):
        pairwise_comps = [np.matrix([[1, 1, 2],
                                     [1, 1, 1],
                                     [0.5, 1, 1]], dtype=float),
                          np.matrix([[1, 10, 5],
                                     [1 / 10, 1, 10],
                                     [1 / 5, 1 / 10, 1]])]

        Test.compare_with_eps(rate(pairwise_comps,
                   np.matrix([[1, 1 / 2],
                              [2, 1]], dtype=float)),
                              [0.577, 0.285, 0.137], 0.001)

        Test.compare_with_eps([get_koczkodaj_index(pc) for pc in pairwise_comps], [0.5, 0.95], 0.01)

    def test_calculations_2(self):
        pairwise_comps = [np.matrix([[1, 10, 10],
                                     [10.1, 1, 10],
                                     [10.1, 10.1, 1]], dtype=float),
                          np.matrix([[1, 1 / 3, 5],
                                     [3, 1, 7],
                                     [1 / 5, 1 / 7, 1]])]

        Test.compare_with_eps(rate(pairwise_comps,
                   np.matrix([[1, 1 / 2],
                              [2, 1]], dtype=float)),
              [0.299, 0.540, 0.160], 0.001)

        Test.compare_with_eps([get_koczkodaj_index(pc) for pc in pairwise_comps], [0.90, 0.53], 0.01)

    def test_calculations_3(self):
        pairwise_comps = [np.matrix([[1, 1 / 7, 1 / 5],
                                     [7, 1, 3],
                                     [5, 1 / 3, 1]]),
                          np.matrix([[1, 1 / 3, 5],
                                     [3, 1, 7],
                                     [1 / 5, 1 / 7, 1]])]

        Test.compare_with_eps(rate(pairwise_comps,
                   np.matrix([[1, 1 / 2],
                              [2, 1]], dtype=float)),
                              [0.213, 0.643, 0.143], 0.001)

        Test.compare_with_eps([get_koczkodaj_index(pc) for pc in pairwise_comps], [0.53, 0.53], 0.01)
