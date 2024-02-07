from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer, MDDialogSupportingText
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDListItem, MDListItemHeadlineText
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import NoTransition
from kivy.uix.gridlayout import GridLayout
import math
import random
from kivy.uix.recycleview import RecycleView

class PageHomeScreen(MDScreen):
    ...
class PageHistoryScreen(MDScreen):
    ...
class PageSettingScreen(MDScreen):
    ...
class TableRow(BoxLayout):
    # def __init__(self, text1='', text2='', text3='', **kwargs):
    #     super(TableRow, self).__init__(**kwargs)
    #     self.text1 = text1
    #     self.text2 = text2
    #     self.text3 = text3
    # def __init__(self, col1_text, col2_text, col3_text, col4_text, **k):
    #     self.col1_text = col1_text
    #     self.col2_text = col2_text
    #     self.col3_text = col3_text
    #     self.col4_text = col4_text
    ...
class MyRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(MyRecycleView, self).__init__(**kwargs)
        self.data = [{'v': str(i), 'a': str(i), 'w': str(i), 'o': str(i)} for i in range(12)]


class ConverterApp(MDApp):

    def on_start(self):
        super().on_start()
        # self.page_home = PageHomeScreen()
        # self.page_history = PageHistoryScreen()
        self.lists_input = [
            self.root.ids.screen_manager.get_screen('screenHome').ids.text_input0,
            self.root.ids.screen_manager.get_screen('screenHome').ids.text_input1,
            self.root.ids.screen_manager.get_screen('screenHome').ids.text_input2,
            self.root.ids.screen_manager.get_screen('screenHome').ids.text_input3,
        ]
        self.active_text_input = self.lists_input[0]

        matrix = [[str(random.randint(0, 9)) for _ in range(4)] for _ in range(10)]
        # for item in matrix:
        #     row = TableRow()
        #     self.root.ids.screen_manager.get_screen('screenHistory').ids.list_items.add_widget(row)

    def navigate_to_screen1(self, num):
        self.root.ids.screen_manager.current = str(num)
        self.root.ids.screen_manager.transition = NoTransition()

        
    def add_char(self, value):
        # print(Home_page().ids.text_input1)
        print(self.active_text_input)
        if ((self.active_text_input.text.count(".") == 0 and value == ".") or value != ".") and len(self.active_text_input.text) <=10:
            self.active_text_input.text += value

    def del_char(self):
        new_item = MDListItem()
        new_item.add_widget(MDListItemHeadlineText(text="New Headline"))
        self.root.ids.list_items.add_widget(new_item)
        self.active_text_input.text = self.active_text_input.text[:-1]
        


    def mainCount(self):
        count_input_empty = [input.text for input in self.lists_input].count("")
        if count_input_empty == 2:
            V = self.lists_input[0].text
            A = self.lists_input[1].text
            W = self.lists_input[2].text
            O = self.lists_input[3].text
            if V and A:
                self.lists_input[2].text = str(float(V) * float(A))
                self.lists_input[3].text= str(float(V) / float(A))
            elif V and W:
                self.lists_input[1].text = str(float(W) / float(V))
                self.lists_input[3].text = str(float(V) / float(self.lists_input[1].text))
            elif V and O:
                self.lists_input[1].text= str(float(V) / float(O))
                self.lists_input[2].text = str(float(self.lists_input[1].text) * float(V) )
            elif A and W:
                self.lists_input[0].text = str(float(W) / float(A))
                self.lists_input[3].text = str(float(W) / (float(A)*float(A)))
            elif A and O:
                self.lists_input[0].text = str(float(A) * float(O))
                self.lists_input[2].text = str((float(A)*float(A)) * float(O))
            elif W and O:
                self.lists_input[0].text = str(math.sqrt(float(W) * float(O)))
                self.lists_input[1].text= str(math.sqrt(float(W) / float(O)))
            for input in self.lists_input:
                if len(input.text) > 9:
                    input.text = input.text[:10]+"..."
        else:
            self.show_alert_dialog()

    def on_text_input_click(self, instance, touch, id_input):
        if instance.collide_point(*touch.pos):
            color_default = (0, 0, 0, 0)
            active_color = (0.5, 0, 0, 0.3)
            print("active inpupt", id_input)
            for input in self.lists_input:
                input.canvas.before.children[3].rgba = color_default
            
            self.lists_input[id_input].canvas.before.children[3].rgba = active_color
            
            self.active_text_input = self.lists_input[id_input]


    def show_alert_dialog(self):
        content = BoxLayout(orientation='vertical', padding=20) 
        self.dialog = MDDialog(
            MDDialogHeadlineText(
                text="Увага!",
                halign="left",
            ),
            MDDialogSupportingText(
                text="Ви повинні ввести лише 2 поля!",
                halign="left",
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Ок"),
                    style="text", on_release=lambda _:self.dialog.dismiss()
                ),
                spacing="8dp",
            ),
        )
        self.dialog.open()
        
    def build(self):
        return


ConverterApp().run()