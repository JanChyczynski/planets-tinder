from typing import List
import numpy as np


def rate(criteria_matrices: List[np.matrix], criterion_importance_m: np.matrix):
    criterions = len(criteria_matrices)
    alternatives = len(criteria_matrices[0])

    for matrix in criteria_matrices:
        if matrix.shape != (alternatives, alternatives):
            raise ValueError(f"criteria matrices must be of shape {(alternatives, alternatives)}")

