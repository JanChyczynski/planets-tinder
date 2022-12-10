from typing import List
import numpy as np
import sympy as sp


def calc_priority_vector(matrix: np.matrix) -> np.array:
    size = matrix.shape[0]
    for i in range(size):
        matrix[:, i] /= matrix[:, i].sum()

    ans = np.array([0] * size, dtype=float)

    for i in range(size):
        ans[i] = matrix[i, :].sum() / float(size)
    return ans


def rate(criteria_matrices: List[np.matrix], criterion_importance_m: np.matrix):
    criterions = len(criteria_matrices)
    alternatives = len(criteria_matrices[0])

    eigen_v: List[np.array] = []

    for matrix in criteria_matrices:
        if matrix.shape != (alternatives, alternatives):
            raise ValueError(f"criteria matrices must be of shape {(alternatives, alternatives)}")

    for matrix in criteria_matrices:
        eigen_v.append(calc_priority_vector(matrix))
    priority_vectors_matrix = np.matrix(eigen_v).transpose()

    return priority_vectors_matrix @ calc_priority_vector(criterion_importance_m)
