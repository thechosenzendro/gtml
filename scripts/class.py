def tomik():
    print("This code is in the class!!")


tomik()


def clicked(self):
    global i
    i = rnd.randint(0, 100)
    print("Clicked!")


def checked(self):
    if self.get_active():
        print("Checked!")
    else:
        print("Unchecked!")


def switch_toggled(self, switch):
    print("Switch toggled!")


def slider_changed(self):
    print(f"Value of slider changed: {self.get_value()}")


def open_document(self):
    print("Opening document...")


def test_menu_action(self, action):
    print("It works!")


def entry_changed(self):
    print(f"Entry changed!! Text: {self.get_text()}")


def color_selected(self):
    print(f"Color selected! Color: {self.get_color()}")
