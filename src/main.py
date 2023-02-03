import os
import random
import sys

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.AHP.AhpBody import AhpBody
from src.ListEditingLayout import ListEditingLayout
from src.QuestionLayout import QuestionLayout
from src.ResultsLayout import ResultsLayout

kivy.require('2.1.0')

from src.AHP.rating import get_koczkodaj_index


class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.material_style = "M3"
        self.boxLayout = BoxLayout()
        self.ahpBody = AhpBody()
        self.criterias_screen = ListEditingLayout('List of criteria:',
                                                  ['surface temperature', 'distance from earth', 'atmosphere quality'])
        self.boxLayout.add_widget(self.criterias_screen)
        self.criterias_screen.ids.list_edit_next.on_release = lambda: self.planetSelection() if len(
            self.criterias_screen.items) >= 1 else None
        return self.boxLayout

    def planetSelection(self):
        self.boxLayout.clear_widgets()
        self.planets_screen = ListEditingLayout('List of planets:', ['Mars', 'Wenus', 'Naboo'])
        self.boxLayout.add_widget(self.planets_screen)
        self.planets_screen.ids.list_edit_next.on_release = lambda: self.initAhp() if len(
            self.planets_screen.items) >= 3 else None

    def initAhp(self):
        self.ahpBody.criteria = self.criterias_screen.items
        self.ahpBody.planet_names = self.planets_screen.items
        self.questions = self.ahpBody.generateQuestions()
        self.question_counter = 0
        self.ahpBody.createMatrices()
        self.askQuestion()

    def askQuestion(self):
        self.question = self.questions[self.question_counter]
        self.question_counter += 1
        self.boxLayout.clear_widgets()
        self.questionLayout = QuestionLayout(self.ahpBody.criteria[self.question[0]],
                                             self.ahpBody.planet_names[self.question[1]],
                                             self.ahpBody.planet_names[self.question[2]], can_be_zero=True)
        self.boxLayout.add_widget(self.questionLayout)
        self.questionLayout.ids.next_question_button.on_release = self.handleQuestion

    def handleQuestion(self):
        ans = self.questionLayout.ids.comp_input_field.text
        try:
            ans_f = float(ans)
            # print(self.ahpBody.comp_matrices[self.question[0]])
            self.ahpBody.comp_matrices[self.question[0]][self.question[1], self.question[2]] = ans_f
            if ans_f != 0.0:
                self.ahpBody.comp_matrices[self.question[0]][self.question[2], self.question[1]] = 1 / ans_f
            else:
                self.ahpBody.comp_matrices[self.question[0]][self.question[2], self.question[1]] = 0

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
        if len(self.questions) == 0:
            self.showEndResults()
        else:
            self.question = self.questions[self.question_counter]
            self.question_counter += 1
            self.boxLayout.clear_widgets()
            self.questionLayout = QuestionLayout("compare criteria:",
                                                 self.ahpBody.criteria[self.question[0]],
                                                 self.ahpBody.criteria[self.question[1]], "is more important")
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
        resultsView = ResultsLayout(
            sorted(list(zip(self.ahpBody.planet_names, self.ahpBody.rate())), key=lambda x: x[1], reverse=True),
            [(criterion, get_koczkodaj_index(comp_matrix)) for (criterion, comp_matrix) in
             zip(self.ahpBody.criteria, self.ahpBody.comp_matrices)])
        self.boxLayout.add_widget(resultsView)


def main():
    MyApp().run()


if __name__ == "__main__":
    main()
