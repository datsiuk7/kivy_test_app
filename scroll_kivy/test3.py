from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen


class PageHomeScreen(MDScreen):
    ...
class PageHistoryScreen(MDScreen):
    ...



class My3App(MDApp):
    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        ...
        # self.root.ids.screen_manager.current = item_text

    def build(self):
        return 


My3App().run()