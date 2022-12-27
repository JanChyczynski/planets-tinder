from typing import List

from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout


class ListEditingLayout(BoxLayout):
    title = StringProperty()
    items = ListProperty()

    def __init__(self, title: str, items: List[str], **kwargs):
        super().__init__(**kwargs)
        self.items = items
        self.title = title


    def add_item(self, name: str):
        self.items.append(name)

Builder.load_file('layouts/listEditingLayout.kv')