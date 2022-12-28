import random
import string

import numpy as np

from src.AHP.rating import rate


class AhpBody:
    def __init__(self):
        self.criteria: list[string] = ['surface temperature', 'distance from earth', 'atmosphere density']
        self.planet_names: list[string] = ['mars', 'wen-su', 'naboo']
        self.comp_matrices: list[np.matrix] = []
        self.criterion_importance_m: [np.matrix, None] = None

    def rate(self):
        return rate(self.comp_matrices, self.criterion_importance_m)

    def generateQuestions(self) -> list[(int,int,int)]:
        question_list = []
        for criterion in range(len(self.criteria)):
            for pl1 in range(len(self.planet_names)):
                for pl2 in range(pl1 + 1, len(self.planet_names)):
                    question_list.append((criterion, pl1, pl2))
        random.shuffle(question_list)
        return question_list

    def createMatrices(self):
        self.comp_matrices = [np.matrix([[0]*(len(self.planet_names))]*(len(self.planet_names)), dtype=float)
                              for _ in range(len(self.criteria))]
        self.criterion_importance_m = np.matrix([[0]*(len(self.criteria))]*(len(self.criteria)), dtype=float)

