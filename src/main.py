from typing import List

import numpy as np
import kivy
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.layout import Layout
import kivymd
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

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
        self.main_screen = ListEditingLayout('List of criteria:',
                                      ["koczkodan", "koczkodan", "koczkodan", "koczkodan", "koczkodan"])
        self.boxLayout.add_widget(self.main_screen)
        self.main_screen.ids.list_edit_next.on_release = self.nextScene
        return self.boxLayout

    def nextScene(self):
        self.boxLayout.clear_widgets()
        self.boxLayout.add_widget(QuestionLayout("hehe", "hiszpańska dziewczyna", "losowa kobieta z karczmy"))


def main():
    MyApp().run()


if __name__ == "__main__":
    main()
