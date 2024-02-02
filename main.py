from kivymd.app import MDApp
# from kivy.lang import Builder
# Builder.load_file('home.kv')
class ConverterApp(MDApp):
    def on_start(self):
        super().on_start()
        # self.root.ids.tabs.switch_tab(icon="home")
        # self.root.ids.tabs.set_active_item(self.root.ids.tabs.get_tabs_list()[2])  # Встановити другу вкладку (індекс 1) як активну
        # print("-----------------")
        # print(dir(self.root.ids.tabs))
        # print("-----------------")
        # print(self.root.ids.tabs.get_tabs_list())
        # self.root.ids.tabs.set_current_tab(self.root.ids.tab_home)
    def go(self):
        print("привіт")
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        return


ConverterApp().run()