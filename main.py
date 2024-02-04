from kivymd.app import MDApp
from kivymd.uix.stacklayout import StackLayout
from kivy.uix.image import Image

class Home_page(StackLayout):
    pass
class ConverterApp(MDApp):

    def on_start(self):
        super().on_start()
        self.active_text_input = ""
        # self.root.ids.field1.focus = True
        # self.root.ids.tabs.switch_tab(icon="home")
        # self.root.ids.tabs.set_active_item(self.root.ids.tabs.get_tabs_list()[2])  # Встановити другу вкладку (індекс 1) як активну
        # print("-----------------")
        print(self.root.ids)
        # print("-----------------")
        # print(self.root.ids.tabs.get_tabs_list())
        # print(dir(self.root.ids.tabs.default_tab))
        # self.root.ids.tabs.switch_tab(self.root.ids.tab_history)
        

        
    def add_char(self, value):
        # print(Home_page().ids.text_input1)
        if self.active_text_input:
            print(self.active_text_input)
            if (self.active_text_input.text.count(".") == 0 and value == ".") or value != ".":
                self.active_text_input.text += value

    def del_char(self):
        if self.active_text_input:
            self.active_text_input.text = self.active_text_input.text[:-1]

    def on_text_input_click(self, instance, touch, tt):
        print(tt)
        if instance.collide_point(*touch.pos):
            # instance.canvas.before.children[3].rgba = (1, 0, 0, 0.5)
            self.active_text_input = instance
            print(f"Клікнуто на {instance}")
            Home_page().ids.text_input1.canvas.before.children[3].rgba = (1, 0, 0, 0.5)
            Home_page().ids.text_input2.canvas.before.children[3].rgba = (1, 0, 0, 0.5)

    def build(self):
        # self.theme_cls.theme_style = "Dark"
        # background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        return


ConverterApp().run()