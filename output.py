
import sys
import gi
import random as rnd
#Here are the imports
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Gdk, Adw, Gio, GLib
# About the app
GLib.set_application_name("Example GTML App")
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
        
        css_data = '''.title_tomik {
    font-size: 100px;
    font-weight: bold;
}

.paragraph {
    font-weight: bold;
}'''
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(css_data.encode())
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.main_box)
        
        self.header_0_header = Gtk.HeaderBar()
        self.header_0 = Gtk.Box()
        self.header_0_header.pack_start(self.header_0)
        self.set_titlebar(self.header_0_header)
        #Here are the attributes for header_0

        self.button_1_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.button_1 = Gtk.Button(label=f"""Open Document""")
        self.button_1_container.append(self.button_1)
        self.header_0.append(self.button_1_container)
        self.button_1.connect('clicked', open_document)
                
        self.button_1.set_icon_name("document-open-symbolic")
        #Here are the attributes for button_1

        self.nice_popover = Gio.Menu.new()
        self.nice_popover_popover = Gtk.PopoverMenu()
        self.nice_popover_popover.set_menu_model(self.nice_popover)
        #Here are the attributes for nice_popover

        self.menu_action_3_name = f"""Test""".replace(" ", "_").lower()
        self.menu_action_3 = Gio.SimpleAction.new(self.menu_action_3_name, None)
        self.menu_action_3.set_enabled(True)
        self.add_action(self.menu_action_3)
        self.nice_popover.append(f"""Test""", f"win.{self.menu_action_3_name}")
        self.menu_action_3.set_enabled(True)
        self.menu_action_3.connect("activate", test_menu_action)
        #Here are the attributes for menu_action_3

        self.menu_button_4_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.menu_button_4 = Gtk.MenuButton(label=f"""""")
        self.menu_button_4_container.append(self.menu_button_4)
        self.header_0.append(self.menu_button_4_container)
        self.menu_button_4.set_icon_name("open-menu-symbolic")
        self.menu_button_4.set_popover(self.nice_popover_popover)
        #Here are the attributes for menu_button_4
        
        self.text_5 = Gtk.Label()
        self.text_5.set_text(f"""A big text""")
        self.main_box.append(self.text_5)
        self.text_5.set_css_classes('title_tomik'.split(" "))
        #Here are the attributes for text_5
        
        self.component_with_id = Gtk.Label()
        self.component_with_id.set_text(f"""Small text""")
        self.main_box.append(self.component_with_id)
        self.component_with_id.set_css_classes('paragraph'.split(" "))
        #Here are the attributes for component_with_id

        self.box_7 = Gtk.Box()
        self.box_7.set_spacing(5)
        self.main_box.append(self.box_7)
        self.box_7.set_orientation(Gtk.Orientation.HORIZONTAL)
        #Here are the attributes for box_7
        
        self.text_8 = Gtk.Label()
        self.text_8.set_text(f"""Nested text""")
        self.box_7.append(self.text_8)
        #Here are the attributes for text_8
        
        self.text_9 = Gtk.Label()
        self.text_9.set_text(f"""Horizontal text""")
        self.box_7.append(self.text_9)
        #Here are the attributes for text_9

        self.box_10 = Gtk.Box()
        self.box_10.set_spacing(5)
        self.main_box.append(self.box_10)
        self.box_10.set_orientation(Gtk.Orientation.VERTICAL)
        #Here are the attributes for box_10
        
        self.data_binding = Gtk.Label()
        self.data_binding.set_text(f"""This is data binding!: {i}""")
        self.box_10.append(self.data_binding)
        #Here are the attributes for data_binding
        
        self.text_12 = Gtk.Label()
        self.text_12.set_text(f"""Vertical text""")
        self.box_10.append(self.text_12)
        #Here are the attributes for text_12

        self.button_13_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.button_13 = Gtk.Button(label=f"""A BUTTON""")
        self.button_13_container.append(self.button_13)
        self.main_box.append(self.button_13_container)
        self.button_13.connect('clicked', clicked)
                
        #Here are the attributes for button_13

        self.wise_check = Gtk.CheckButton(label=f"""A Czech button! Oh wait...""")
        self.main_box.append(self.wise_check)
        self.wise_check.connect('toggled', checked)
        #Here are the attributes for wise_check

        self.switch_15_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.switch_15 = Gtk.Switch()
        self.switch_15_label = Gtk.Label(label=f"""Switch""")
        self.switch_15_container.append(self.switch_15)
        self.switch_15_container.append(self.switch_15_label)
        self.switch_15_container.set_spacing(5)
        self.main_box.append(self.switch_15_container)
        self.switch_15.connect('state-set', switch_toggled)
        #Here are the attributes for switch_15

        self.slider_16 = Gtk.Scale()
        self.main_box.append(self.slider_16)
        self.slider_16.set_digits(0)
        self.slider_16.set_range(0,20)
        self.slider_16.set_draw_value(False)
        self.slider_16.set_value(10)
        self.slider_16.connect('value-changed', slider_changed)
        #Here are the attributes for slider_16

        self.entry_17 = Gtk.Entry()
        self.entry_17.set_text(f"""Entry""")
        self.entry_17_container = Gtk.Box()
        self.entry_17_container.append(self.entry_17)
        self.main_box.append(self.entry_17_container)
        self.entry_17.set_placeholder_text("Placeholder text")
        self.entry_17.connect('changed', entry_changed)
        #Here are the attributes for entry_17

        self.color_button_18_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.color_button_18 = Gtk.ColorButton()
        self.color_button_18_label = Gtk.Label(label=f"""Color button""")
        self.color_button_18_container.append(self.color_button_18)
        self.color_button_18_container.append(self.color_button_18_label)
        self.color_button_18_container.set_spacing(5)
        self.main_box.append(self.color_button_18_container)
        self.color_button_18.connect('color-set', color_selected)
        #Here are the attributes for color_button_18
#Here are the components
class App(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
    def on_activate(self, app):
        allow_more_instances = False
        if not allow_more_instances:
            if not hasattr(self, "win"):
                self.win = MainWindow(application=app)
        else:
            self.win = MainWindow(application=app)
        self.win.present()

app = App(application_id="com.kosa.example.app")
app.run(sys.argv)
