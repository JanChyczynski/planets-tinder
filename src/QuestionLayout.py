from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class QuestionLayout(BoxLayout):
    criterion = StringProperty()
    left_planet_name = StringProperty()
    right_planet_name = StringProperty()

    def __init__(self, criterion: str, left_planet_name: str, right_planet_name: str, **kwargs):
        super().__init__(**kwargs)
        self.left_planet_name = left_planet_name
        self.right_planet_name = right_planet_name
        self.criterion = criterion

    def finish_input(self):
        print(self.ids.comp_input_field.text)


Builder.load_file('layouts/questionLayout.kv')