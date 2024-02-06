from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsPrimary
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel

class Tab1(MDBoxLayout, MDTabsPrimary):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        scroll_view = MDScrollView()
        label = MDLabel(text="Why fast move not scroll?")
        scroll_view.add_widget(label)
        
        self.add_widget(scroll_view)

class MyApp(MDApp):
    def build(self):
        return

MyApp().run()
