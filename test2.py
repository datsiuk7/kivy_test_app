from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

class ScrollableTableWithDeleteButtonApp(App):
    def build(self):
        # Список даних для таблиці
        self.data = [(str(i), str(i * 2), str(i * 3)) for i in range(1, 101)]

        # Створення GridLayout для таблиці
        self.table_layout = GridLayout(cols=4, spacing=10, size_hint_y=None)

        # Встановлення висоти таблиці
        self.table_layout.bind(minimum_height=self.table_layout.setter('height'))

        # Додавання заголовків для стовпців
        self.table_layout.add_widget(Label(text='Колонка 1'))
        self.table_layout.add_widget(Label(text='Колонка 2'))
        self.table_layout.add_widget(Label(text='Колонка 3'))
        self.table_layout.add_widget(Label())

        # Додавання даних зі списку у таблицю та кнопок для видалення рядка
        for row_data in self.data:
            for data in row_data:
                self.table_layout.add_widget(Label(text=data))
            delete_button = Button(text="Видалити рядок", size_hint=(None, None))
            delete_button.bind(on_release=self.delete_row)
            self.table_layout.add_widget(delete_button)

        # Створення ScrollView і додавання до нього GridLayout з таблицею
        scroll_view = ScrollView()
        scroll_view.add_widget(self.table_layout)

        return scroll_view

    def delete_row(self, instance):
        # Видалення рядка зі списку та оновлення таблиці
        row_index = self.table_layout.children.index(instance) // 4  # 4 - кількість елементів у кожному рядку
        del self.data[row_index]
        self.update_table()

    def update_table(self):
        # Оновлення таблиці з оновленим списком даних
        self.table_layout.clear_widgets()
        # Додавання заголовків для стовпців
        self.table_layout.add_widget(Label(text='Колонка 1'))
        self.table_layout.add_widget(Label(text='Колонка 2'))
        self.table_layout.add_widget(Label(text='Колонка 3'))
        self.table_layout.add_widget(Label())
        # Додавання даних зі списку у таблицю та кнопок для видалення рядка
        for row_data in self.data:
            for data in row_data:
                self.table_layout.add_widget(Label(text=data))
            delete_button = Button(text="Видалити рядок", size_hint=(None, None))
            delete_button.bind(on_release=self.delete_row)
            self.table_layout.add_widget(delete_button)

if __name__ == '__main__':
    ScrollableTableWithDeleteButtonApp().run()
