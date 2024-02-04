from kivymd.app import MDApp
from kivymd.uix.stacklayout import StackLayout
class ConverterApp(MDApp):

    def on_start(self):
        super().on_start()
        self.active_text_input = self.root.ids.text_input1
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
            if ((self.active_text_input.text.count(".") == 0 and value == ".") or value != ".") and len(self.active_text_input.text) <=10:
                self.active_text_input.text += value

    def del_char(self):
        self.active_text_input.text = self.active_text_input.text[:-1]

    def on_text_input_click(self, instance, touch, id_input=0):
        color_default = (0, 0, 0, 0)
        active_color = (0.5, 0, 0, 0.3)
        
        if instance.collide_point(*touch.pos):
            self.root.ids.text_input1.canvas.before.children[3].rgba = color_default
            self.root.ids.text_input2.canvas.before.children[3].rgba = color_default
            self.root.ids.text_input3.canvas.before.children[3].rgba = color_default
            self.root.ids.text_input4.canvas.before.children[3].rgba = color_default
            if id_input == 1:
                self.root.ids.text_input1.canvas.before.children[3].rgba = active_color
            if id_input == 2:
                self.root.ids.text_input2.canvas.before.children[3].rgba = active_color
            if id_input == 3:
                self.root.ids.text_input3.canvas.before.children[3].rgba = active_color
            if id_input == 4:
                self.root.ids.text_input4.canvas.before.children[3].rgba = active_color
            
            self.active_text_input = instance
            print(f"Клікнуто на {instance}")

    def build(self):
        return


ConverterApp().run()