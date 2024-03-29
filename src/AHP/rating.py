from copy import deepcopy
from math import inf
from typing import List
import numpy as np


def calc_priority_vector(org_matrix: np.matrix) -> np.array:
    matrix = deepcopy(org_matrix)
    size = matrix.shape[0]
    for i in range(size):
        matrix[:, i] /= matrix[:, i].sum()

    ans = np.array([0] * size, dtype=float)

    for i in range(size):
        ans[i] = matrix[i, :].sum() / float(size)
    return ans


def fill_incomplete_matrix(matrix: np.matrix):
    def count_zeros_in_row(row):
        count = 0
        for i in range(row.size):
            if row[:, i] == np.matrix([[0]]):
                count += 1
        return count

    i = 0
    for row in matrix:
        matrix[i, i] += count_zeros_in_row(row)
        i += 1

    print(matrix)


def rate(criteria_matrices: List[np.matrix], criterion_importance_m: np.matrix):
    criteria = len(criteria_matrices)
    alternatives = len(criteria_matrices[0])

    eigen_v: List[np.array] = []

    for matrix in criteria_matrices:
        if matrix.shape != (alternatives, alternatives):
            raise ValueError(f"criteria matrices must be of shape {(alternatives, alternatives)}")

    if criterion_importance_m.shape != (criteria, criteria):
        raise ValueError(f"criterion importance matrix must be of shape {(criteria, criteria)}")

    for matrix in criteria_matrices:
        fill_incomplete_matrix(matrix)
        eigen_v.append(calc_priority_vector(matrix))
    priority_vectors_matrix = np.matrix(eigen_v).transpose()

    return (priority_vectors_matrix @ calc_priority_vector(criterion_importance_m)).tolist()[0]


def triad_koczkodaj(i: int, j: int, k: int, pc: np.matrix) -> float:
    # print(pc)
    # print(abs(1 - pc[i, k] * pc[k, j] / pc[i, j]), abs(1 - pc[i, j] / (pc[i, k] * pc[k, j])))
    if pc[i, k] == 0 or pc[k, j] == 0 or pc[j, i] == 0:
        return 0
    return min(abs(1 - pc[i, k] * pc[k, j] / pc[i, j]), abs(1 - pc[i, j] / (pc[i, k] * pc[k, j])))


def get_koczkodaj_index(pairwise_comparison: np.matrix) -> float:
    koczkodaj = -inf
    n = pairwise_comparison.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                koczkodaj = max(koczkodaj, triad_koczkodaj(i, j, k, pairwise_comparison))

    return float(koczkodaj)
