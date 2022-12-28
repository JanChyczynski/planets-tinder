import kivy
import numpy as np
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

from src.AHP.AhpBody import AhpBody
from src.ListEditingLayout import ListEditingLayout
from src.QuestionLayout import QuestionLayout
from src.ResultsLayout import ResultsLayout

kivy.require('2.1.0')

from src.AHP.rating import rate, get_koczkodaj_index


def test_calculations():
    pairwise_comps = [np.matrix([[1, 1 / 7, 1 / 5],
                                 [7, 1, 3],
                                 [5, 1 / 3, 1]]),
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


class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.material_style = "M3"
        # return QuestionLayout("hehe", "hiszpańska dziewczyna", "losowa kobieta z karczmy")
        self.boxLayout = BoxLayout()
        self.ahpBody = AhpBody()
        self.criterias_screen = ListEditingLayout('List of criteria:', self.ahpBody.criteria)
        self.boxLayout.add_widget(self.criterias_screen)
        self.criterias_screen.ids.list_edit_next.on_release = self.planetSelection
        return self.boxLayout

    def planetSelection(self):
        self.boxLayout.clear_widgets()
        self.planets_screen = ListEditingLayout('List of planets:', self.ahpBody.planet_names)
        self.boxLayout.add_widget(self.planets_screen)
        self.questions = self.ahpBody.generateQuestions()
        self.question_counter = 0
        self.planets_screen.ids.list_edit_next.on_release = self.initAhp

    def initAhp(self):
        self.ahpBody.createMatrices()
        self.askQuestion()

    def askQuestion(self):
        self.question = self.questions[self.question_counter]
        self.question_counter += 1
        self.boxLayout.clear_widgets()
        self.questionLayout = QuestionLayout(self.ahpBody.criteria[self.question[0]],
                                             self.ahpBody.planet_names[self.question[1]],
                                             self.ahpBody.planet_names[self.question[2]])
        self.boxLayout.add_widget(self.questionLayout)
        self.questionLayout.ids.next_question_button.on_release = self.handleQuestion

    def handleQuestion(self):
        ans = self.questionLayout.ids.comp_input_field.text
        try:
            ans_f = float(ans)
            print(self.ahpBody.comp_matrices[self.question[0]])
            self.ahpBody.comp_matrices[self.question[0]][self.question[1], self.question[2]] = ans_f
            self.ahpBody.comp_matrices[self.question[0]][self.question[2], self.question[1]] = 1 / ans_f
        except ValueError:
            self.question_counter -= 1
        if self.question_counter == len(self.questions):
            self.questions = [(i, j) for i in range(len(self.ahpBody.criteria)) for j in
                             range(len(self.ahpBody.criteria))
                             if j > i]
            self.question_counter = 0
            random.shuffle(self.questions)
            self.askCriteriaCompQuestion()
            return
        self.askQuestion()

    def askCriteriaCompQuestion(self):
        self.question = self.questions[self.question_counter]
        self.question_counter += 1
        self.boxLayout.clear_widgets()
        self.questionLayout = QuestionLayout("compare criteria:",
                                             self.ahpBody.criteria[self.question[0]],
                                             self.ahpBody.criteria[self.question[1]],"is more important")
        self.boxLayout.add_widget(self.questionLayout)
        self.questionLayout.ids.next_question_button.on_release = self.handleCriteriaCompQuestion

    def handleCriteriaCompQuestion(self):
        ans = self.questionLayout.ids.comp_input_field.text
        try:
            ans_f = float(ans)
            self.ahpBody.criterion_importance_m[self.question[0], self.question[1]] = ans_f
            self.ahpBody.criterion_importance_m[self.question[1], self.question[0]] = 1 / ans_f
        except ValueError:
            self.question_counter -= 1
        if self.question_counter == len(self.questions):
            self.showEndResults()
            return
        self.askCriteriaCompQuestion()

    def showEndResults(self):
        self.boxLayout.clear_widgets()
        resultsView = ResultsLayout(list(zip(self.ahpBody.criteria, self.ahpBody.rate())),
                                    [("Koczkodan", 23.4), ("terakota", 21.37)])
        self.boxLayout.add_widget(resultsView)


def main():
    MyApp().run()


if __name__ == "__main__":
    main()
