from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class QuestionLayout(BoxLayout):
    criterion = StringProperty()
    left_planet_name = StringProperty()
    right_planet_name = StringProperty()
    comp_text = StringProperty()

    def __init__(self, criterion: str, left_planet_name: str, right_planet_name: str,comp_text: str = "is better", **kwargs):
        super().__init__(**kwargs)
        self.left_planet_name = left_planet_name
        self.right_planet_name = right_planet_name
        self.criterion = criterion
        self.comp_text = comp_text


Builder.load_file('layouts/questionLayout.kv')