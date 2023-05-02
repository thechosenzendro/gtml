
import sys
import gi
import random as rnd
#Here are the imports
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


i = 0
print("This code is in a global scope!!")

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, title="Example app")
        self.set_default_size(800, 800)
                
        def tomik():
            print("This code is in the class!!")
        tomik()
        def clicked(self):
            global i
            i = rnd.randint(0,100)
            print(i)

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.main_box)
                
        self.text_0 = Gtk.Label()
        self.text_0.set_text(f"""text""")
        self.text_0.set_name("self.text_0")
        self.main_box.append(self.text_0)
        #Here are the attributes for text_0
        
        self.component_with_id = Gtk.Label()
        self.component_with_id.set_text(f"""222222""")
        self.component_with_id.set_name("self.component_with_id")
        self.main_box.append(self.component_with_id)
        #Here are the attributes for component_with_id

        self.box_2 = Gtk.Box()
        self.main_box.append(self.box_2)
        #Here are the attributes for box_2
        
        self.text_3 = Gtk.Label()
        self.text_3.set_text(f"""Nested text""")
        self.text_3.set_name("self.text_3")
        self.box_2.append(self.text_3)
        #Here are the attributes for text_3

        self.box_4 = Gtk.Box()
        self.main_box.append(self.box_4)
        #Here are the attributes for box_4

        self.box_5 = Gtk.Box()
        self.box_4.append(self.box_5)
        #Here are the attributes for box_5
        
        self.text_6 = Gtk.Label()
        self.text_6.set_text(f"""This is data binding!: {i}""")
        self.text_6.set_name("self.text_6")
        self.box_5.append(self.text_6)
        #Here are the attributes for text_6

        self.button_7 = Gtk.Button(label=f"""A BUTTON""")
        self.main_box.append(self.button_7)
        self.button_7.connect('clicked', clicked)
                
        #Here are the attributes for button_7
#Here are the components
class App(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = App(application_id="com.kosa.example.app")
app.run(sys.argv)
