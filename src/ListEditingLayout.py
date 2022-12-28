from typing import List

from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout


class ListEditingLayout(BoxLayout):
    title = StringProperty()
    items = ListProperty()

    def __init__(self, title: str, items: List[str], **kwargs):
        super().__init__(**kwargs)
        self.items = items
        self.title = title


    def add_item(self, name: str):
        self.items.append(name)

    def remove_item(self, name: str):
        self.items.remove(name)

class ItemViewClass(MDBoxLayout):
    text = StringProperty()
    remove = ObjectProperty()

Builder.load_file('layouts/listEditingLayout.kv')