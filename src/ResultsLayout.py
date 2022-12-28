from typing import List, Tuple

from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout


class ResultsLayout(BoxLayout):
    criteria = ListProperty()
    planets = ListProperty()

    def __init__(self, planets: List[Tuple[str, float]], criteria: List[Tuple[str, float]], **kwargs):
        super().__init__(**kwargs)
        self.criteria = criteria
        self.planets = planets


class RankingElementView(MDBoxLayout):
    text = StringProperty()
    number = NumericProperty()

Builder.load_file('layouts/resultsLayout.kv')