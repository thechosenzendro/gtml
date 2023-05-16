# Source file for components used by the compiler.

# $innertext property is for inner text of the component.
# $id property is for the id generated by the compiler.
# $parent property is for the parent component of the component.

components = {
    "header": {
        "attributes": {},
        "template": """
        $id_header = Gtk.HeaderBar()
        $id = Gtk.Box()
        $id_header.pack_start($id)
        self.set_titlebar($id_header)""",
    },
    "box": {
        "attributes": {
            "orientation": {
                "vertical": """
                $id.set_orientation(Gtk.Orientation.VERTICAL)""",
                "horizontal": """
                $id.set_orientation(Gtk.Orientation.HORIZONTAL)""",
            },
            "spacing": {
                "$string": """
                $id.set_spacing($string)"""
            },
        },
        "template": """
        $id = Gtk.Box()
        $id.set_spacing(5)
        $parent_id.append($id)""",
    },
    "text": {
        "attributes": {},
        "template": """        
        $id = Gtk.Label()
        $id.set_text($innertext)
        $parent_id.append($id)""",
    },
    "button": {
        "attributes": {
            "onclick": {
                "$string": """
                $id.connect('clicked', $string)
                """
            },
            "icon": {
                "$string": """
                $id.set_icon_name("$string")"""
            },
        },
        "template": """
        $id_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        $id = Gtk.Button(label=$innertext)
        $id_container.append($id)
        $parent_id.append($id_container)""",
    },
    "check": {
        "attributes": {
            "ontoggle": {
                "$string": """
                $id.connect('toggled', $string)"""
            }
        },
        "template": """
        $id = Gtk.CheckButton(label=$innertext)
        $parent_id.append($id)""",
    },
    "switch": {
        "attributes": {
            "ontoggle": {
                "$string": """
                $id.connect('state-set', $string)"""
            },
            "active": {
                "True": """
                $id.set_active(True)""",
                "False": """
                $id.set_active(False)""",
            },
        },
        "template": """
        $id_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        $id = Gtk.Switch()
        $id_label = Gtk.Label(label=$innertext)
        $id_container.append($id)
        $id_container.append($id_label)
        $id_container.set_spacing(5)
        $parent_id.append($id_container)""",
    },
    "slider": {
        "attributes": {
            "digits": {
                "$string": """
                $id.set_digits($string)"""
            },
            "onchange": {
                "$string": """
                $id.connect('value-changed', $string)"""
            },
            "range": {
                "$string": """
                $id.set_range($string)"""
            },
            "showvalue": {
                "True": """
                $id.set_draw_value(True)""",
                "False": """
                $id.set_draw_value(False)""",
            },
            "value": {
                "$string": """
                $id.set_value($string)"""
            },
        },
        "template": """
        $id = Gtk.Scale()
        $parent_id.append($id)""",
    },
    "entry": {
        "attributes": {
            "placeholder": {
                "$string": """
                $id.set_placeholder_text("$string")"""
            },
            "onchange": {
                "$string": """
                $id.connect('changed', $string)"""
            },
        },
        "template": """
        $id = Gtk.Entry()
        $id.set_text($innertext)
        $id_container = Gtk.Box()
        $id_container.append($id)
        $parent_id.append($id_container)""",
    },
    "color-button": {
        "attributes": {
            "onselect": {
                "$string": """
                $id.connect('color-set', $string)"""
            }
        },
        "template": """
        $id_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        $id = Gtk.ColorButton()
        $id_label = Gtk.Label(label=$innertext)
        $id_container.append($id)
        $id_container.append($id_label)
        $id_container.set_spacing(5)
        $parent_id.append($id_container)""",
    },
    "menu-button": {
        "attributes": {
            "onclick": {
                "$string": """
                $id.connect('clicked', $string)
                """
            },
            "icon": {
                "$string": """
                $id.set_icon_name("$string")"""
            },
            "popover": {
                "$string": """
                $id.set_popover(self.$string_popover)"""
            },
        },
        "template": """
        $id_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        $id = Gtk.MenuButton(label=$innertext)
        $id_container.append($id)
        $parent_id.append($id_container)""",
    },
    "popover-menu": {
        "attributes": {},
        "template": """
        $id = Gio.Menu.new()
        $id_popover = Gtk.PopoverMenu()
        $id_popover.set_menu_model($id)""",
    },
    "menu-action": {
        "attributes": {
            "onactivate": {
                "$string": """
                $id.connect("activate", $string)"""
            },
            "clickable": {
                "True": """
                $id.set_enabled(True)""",
                "False": """
                $id.set_enabled(False)""",
            },
        },
        "template": """
        $id_name = $innertext.replace(" ", "_").lower()
        $id = Gio.SimpleAction.new($id_name, None)
        $id.set_enabled(True)
        self.add_action($id)
        $parent_id.append($innertext, f"win.{$id_name}")""",
    },
}

global_attributes = {
    "class": {"$string": """$id.set_css_classes('$string'.split(" "))"""},
}
# a $variable is a piece of text in the buffer meant to be replaced at compile time. If the key is not defined, it will be replaced with the default here.
default_values = {
    "$window_width": 800,
    "$window_height": 200,
    "$window_title": "GTML App",
    "$application_name": "GTML App",
    "$application_id": "",
    "$allow_more_instances": True,
}
