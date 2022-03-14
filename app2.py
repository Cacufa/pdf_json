import csv 
import json
from container import *
from elements import *


def open_file():
    print("running open file")
    with open("base.json","r") as file:
        pdf = json.load(file)
        #print(pdf["sections"])
    

    cont = Container("Contenedor 1")
    #cont.add_element("Contenedor 1", elm.text_element("This is a text"))
    #cont.add_element("Contenedor 1", elm.element_new_line())
    #cont.add_element("Contenedor 1" ,element_data)

    elm = Element("text", 986986)
    cont.add_element("Contenedor 1" ,element_data)


    pdf['sections'].append(cont.get_cont())

    print(pdf["sections"])
    
open_file()

