# This program is a compiler for GTML
import requests
import ast
import re
from lxml import etree
from components import components, global_attributes


# Shoutout to scribu on Stack Overflow for this function
def innertext(tag):
    return f'{(tag.text or "")}{"".join(innertext(e) for e in tag) + (tag.tail or "")}'


def populate_dict_with_data(component, string_to_populate):
    # Adding innertext property to the component function
    # Also, the {innertext} is prefixed with f''' and ended with ''' because that provides data binding.
    innerText = re.sub(r"\s+$", "", innertext(component))

    # Changing the component_definition dictionary to str for the replace() function
    string_to_populate = str(string_to_populate)
    string_to_populate = string_to_populate.replace(
        "#parent_id", parent_of_component_id
    )

    # Adding id property to the component function
    string_to_populate = string_to_populate.replace(
        "#innertext", f'f"""{innerText}"""'.replace(f"\n", "")
    )
    # Adding the parent property to the component function
    string_to_populate = string_to_populate.replace("#id", f"self.{component_id}")
    # And back to dictionary
    populated_dictionary = ast.literal_eval(string_to_populate)
    return populated_dictionary


def populate_string_with_data(component, string_to_populate):
    # Adding innertext property to the component function
    # Also, the {innertext} is prefixed with f''' and ended with ''' because that provides data binding.
    innerText = re.sub(r"\s+$", "", innertext(component))
    string_to_populate = string_to_populate.replace(
        "#parent_id", parent_of_component_id
    )

    # Adding id property to the component function
    string_to_populate = string_to_populate.replace(
        "#innertext", f'f"""{innerText}"""'.replace(f"\n", "")
    )
    # Adding the parent property to the component function
    string_to_populate = string_to_populate.replace("#id", f"self.{component_id}")
    return string_to_populate


input_file = "./example.xml"
output_file = "./output.py"

print("Generating initial project structure...")
buffer = """
import sys
import gi
#Here are the imports
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Gdk, Adw, Gio
#Here is the global code

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, title="#window_title")
        self.set_default_size(#window_width, #window_height)
        #Here is the class code
        #Here would be the css provider
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.main_box)
        #Here are the components
class App(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = App(application_id="#application_id")
app.run(sys.argv)
"""
try:
    print(f"Reading the {input_file} file...")
    print("Parsing xml...")
    code = etree.parse(input_file)
except etree.ParseError:
    print("A parse error occured. Have you closed all the tags?")
    quit()

# Adding imports to buffer
try:
    print("Importing libraries...")
    for import_declaration in code.findall("./imports/import"):
        # Make an object for attributes
        import_obj = {}
        # Adding attributes to the objects
        for atribute in import_declaration.attrib:
            import_obj[atribute] = import_declaration.attrib[atribute]
        import_statement = ""
        # Checks if from attribute exists
        if "from" in import_obj:
            import_statement = (
                f'from {import_obj["from"]} import {import_obj["package"]}'
            )
        else:
            import_statement = f'import {import_obj["package"]}'
        if "as" in import_obj:
            import_statement += f' as {import_obj["as"]}'
        # Adding comment to the statement
        import_statement += f"\n#Here are the imports"
        # Replacing the comment with the import statement
        buffer = buffer.replace("#Here are the imports", import_statement)
except:
    print(
        "An error occured during importing libraries. Did you close all the tags properly? Remember: <import/> not <import>!"
    )
# Adding metadata to buffer
try:
    print("Adding metadata to the project...")
    for meta in code.findall("./metadata/meta"):
        # Declaring key and value for the meta tag
        try:
            meta_key = meta.attrib["key"]
            meta_value = meta.attrib["value"]
        except:
            raise TypeError(
                "Either key or value are not declared. Try checking your meta tags."
            )
        buffer = buffer.replace(f"#{meta_key}", meta_value)
except Exception as error:
    print(f"An error occured while adding metadata. \n{error}")

# Modifying window width, height and title properties (based on what properties user defined)
print("Changing window properties...")
important_window_attributes = {"width": False, "height": False, "title": False}
window = code.find("./window")
for attribute in window.attrib:
    attrib_value = window.attrib[attribute]
    buffer = buffer.replace(f"#window_{attribute}", attrib_value)
    if attribute in important_window_attributes:
        important_window_attributes[attribute] = True

for attribute in important_window_attributes:
    if important_window_attributes[attribute] != True:
        raise TypeError(
            f'The property "{attribute}" was not defined and is set as important. Please define the property.'
        )
# Getting css style information if available
ui = code.find("./window/ui")
ui_attributes = ui.attrib
if "style" in ui_attributes:
    # Extracting the path for the css file from the attribute
    style_path = ui_attributes["style"]
    print(f'Adding CSS data from file "{style_path}"...')
    with open(style_path) as style_file:
        style_file_content = style_file.read()
        # Code for the css provider for the app
        css_provider_code = f"""
        css_data = '''{style_file_content}'''
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(css_data.encode())
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)"""
        buffer = buffer.replace("#Here would be the css provider", css_provider_code)
# Adding components to buffer
print("Generating components...")
mem_address_to_id_dict = {}
for iteration, component in enumerate(code.findall("./window/ui//*")):
    component_tag = component.tag
    tag = component_tag.replace("-", "_")
    attributes = component.attrib
    # Get id of the component
    component_id = ""
    if not "id" in attributes:
        component_id = f"{tag}_{iteration}"
    else:
        component_id = attributes["id"]
    # Getting the memory address
    mem_address = hex(id(component))
    # Adding the component to the dictionary for later
    mem_address_to_id_dict[mem_address] = component_id

    # Get the parent of the component
    parent_of_component_arr = code.getpath(component).split("/")
    # Deleting the child from the XPath to get the parent
    parent_of_component_arr.pop(len(parent_of_component_arr) - 1)
    # Making XPath out of the array
    parent_of_component_xpath = "".join(
        [item + "/" for item in parent_of_component_arr]
    ).replace("/gtml", ".")[:-1]
    parent_of_component = code.find(parent_of_component_xpath)
    parent_of_component_mem_address = hex(id(parent_of_component))
    parent_of_component_id = "self."
    if parent_of_component.tag != "ui":
        parent_of_component_id += mem_address_to_id_dict[
            parent_of_component_mem_address
        ]
    else:
        parent_of_component_id += "main_box"
    print(
        f'Processing component "{component_tag}" with id "{component_id}" and memory address "{mem_address}"...'
    )
    component_code = ""
    if component_tag in components:
        component_definition = components[component_tag]
        component_definition = populate_dict_with_data(component, component_definition)
        component_code = component_definition["component"]
        component_code += f"\n        #Here are the attributes for {component_id}"
        # Attribute system
        attributes = component.attrib

        # Defining attributes the system should ignore
        ignore_attribute = {"id": ""}

        def add_attribute(attribute, attribute_list):
            global component_code
            attribute_value = attributes[attribute]

            def finish_adding_attribute(attribute_code):
                global component_code
                # Populates all the arguments in the attribute code
                attribute_code = populate_string_with_data(component, attribute_code)
                attribute_code = attribute_code.replace("#string", attribute_value)
                # Adds the placeholder to the resulting code
                attribute_code += (
                    f"\n        #Here are the attributes for {component_id}"
                )
                component_code = component_code.replace(
                    f"#Here are the attributes for {component_id}",
                    re.sub("^\s+", "", attribute_code),
                )

            # #string means "I dont care what the value is and im comfortable passing whatever the user types as argument to my code". Checking if there are defined types.
            if not "#string" in attribute_list[attribute]:
                if attribute_value in attribute_list[attribute]:
                    attribute_code = attribute_list[attribute][attribute_value]
                    finish_adding_attribute(attribute_code)
                else:
                    raise Exception(
                        f'Value "{attribute_value}" of attribute "{attribute}" is not present in component definition. Possible values are: {list(attribute_list[attribute].keys())}'
                    )
            else:
                attribute_code = attribute_list[attribute]["#string"]
                finish_adding_attribute(attribute_code)

        for attribute in attributes:
            if not attribute in ignore_attribute:
                # Getting all possible attributes
                attribute_list = component_definition["attributes"]
                if attribute in attribute_list:
                    add_attribute(attribute, attribute_list)
                elif attribute in global_attributes:
                    add_attribute(attribute, global_attributes)
                else:
                    raise Exception(
                        f'The attribute "{attribute}" is not defined on the component "{tag}". Possible attributes are: {list(attribute_list.keys())}'
                    )

        # Adding the Replace tag to the component codes
        component_code += f"\n#Here are the components"
        buffer = buffer.replace("#Here are the components", component_code)
    else:
        raise Exception(
            f'Component "{tag}" not found in components dictionary. Check for spelling errors or declare a custom component.'
        )
print("Components generated.")

# Adding the code to the buffer

print("Writing the code to the file...")

# Getting the global code in the global tag
global_code_path = code.find("./code/global").attrib["source"]
try:
    global_code = open(global_code_path).read()
except (KeyError, FileNotFoundError):
    if KeyError:
        print(
            f"There is no source attribute on the global code tag. You need to specify path for the global code."
        )
    if FileNotFoundError:
        print(
            f'Could not read global code file "{global_code_path}". Does the path exist?'
        )
    quit()
global_code = re.sub(r"\s+$", "", global_code)
# Replacing the placeholder with the code
buffer = buffer.replace("#Here is the global code", global_code)

# Doing the exact same thing with the class tag
class_code_path = code.find("./code/class").attrib["source"]
try:
    class_code = open(class_code_path).read()
except (KeyError, FileNotFoundError):
    if KeyError:
        print(
            f"There is no source attribute on the class code tag. You need to specify path for the class code."
        )
    if FileNotFoundError:
        print(
            f'Could not read class code file "{class_code_path}". Does the path exist?'
        )
    quit()
class_code = re.sub(r"\s+$", "", class_code)
# Replacing the placeholder with the code (Adding the spaces because of intendation)
new_class_code = """"""
for line in class_code.splitlines():
    new_class_code += f"\n        {line}"
buffer = buffer.replace("#Here is the class code", new_class_code)

# Writing the finished buffer to specified file
print(f"Writing data to the {output_file} file...")
with open(output_file, "w") as f:
    f.write(buffer)

print("Compiling process finished. Trying to run the code.")
exec(buffer)
