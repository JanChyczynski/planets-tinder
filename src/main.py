from typing import List

import numpy as np
import kivy
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.layout import Layout
import kivymd
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from src.AHP.AhpBody import AhpBody
from src.ListEditingLayout import ListEditingLayout
from src.QuestionLayout import QuestionLayout

kivy.require('2.1.0')

from kivy.app import App

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
        self.criterias_screen = ListEditingLayout('List of criteria:', self.ahpBody.criterions)
        self.boxLayout.add_widget(self.criterias_screen)
        self.criterias_screen.ids.list_edit_next.on_release = self.planetSelection
        return self.boxLayout

    def planetSelection(self):
        self.boxLayout.clear_widgets()
        self.planets_screen = ListEditingLayout('List of planets:', self.ahpBody.planet_names)
        self.boxLayout.add_widget(self.planets_screen)
        self.questions = self.ahpBody.generateQuestions()
        self.question_counter = 0
        self.planets_screen.ids.list_edit_next.on_release = self.askQuestion

    def askQuestion(self):
        question = self.questions[self.question_counter]
        self.question_counter += 1
        self.boxLayout.clear_widgets()
        self.questionLayout = QuestionLayout(self.ahpBody.criterions[question[0]],
                                                 self.ahpBody.planet_names[question[1]],
                                                 self.ahpBody.planet_names[question[2]])
        self.boxLayout.add_widget(self.questionLayout)
        self.questionLayout.ids.next_question_button.on_release = self.handleQuestion

    def handleQuestion(self):
        print(self.questionLayout.ids.comp_input_field.text)
        if self.question_counter == len(self.questions):
            self.showEndResults()
            return
        self.askQuestion()

    def showEndResults(self):
        self.boxLayout.clear_widgets()
        label = Label()
        label.text = "todo es finito"
        self.boxLayout.add_widget(label)

def main():
    MyApp().run()


if __name__ == "__main__":
    main()
