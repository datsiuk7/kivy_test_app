    self.page_home = PageHomeScreen()
        # print(self.root.ids)

        # self.root.ids.field1.focus = True
        # self.root.ids.tabs.switch_tab(icon="home")
        # self.root.ids.tabs.set_active_item(self.root.ids.tabs.get_tabs_list()[2])  # Встановити другу вкладку (індекс 1) як активну
        # print("-----------------")
        # print(self.root.ids)
        # print("-----------------")
        # print(self.root.ids.tabs.get_tabs_list())
        # print(dir(self.root.ids.tabs.default_tab))
        # self.root.ids.tabs.switch_tab(self.root.ids.tab_history)
        self.lists_input = [
            self.page_home.ids.text_input0,
            self.page_home.ids.text_input1,
            self.page_home.ids.text_input2,
            self.page_home.ids.text_input3,
        ]