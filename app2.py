import csv 
import json
from container import *
from elements import *


def open_file():
    print("running open file")

    elm = Element("text", 986986)
    element_data = elm.get_element()

    cont = Container("Contenedor 1")
    cont.add_element("Contenedor 1", elm.text_element("This is a text"))
    cont.add_element("Contenedor 1", elm.element_new_line())
    cont.add_element("Contenedor 1" ,element_data)

    ## PENDING IT IS NOT WORKING FINE RELATED TO THE ADD ELEMENT FROM THE CONTAINER
    

    


    print(cont.get_cont())


def operation():
    pass

open_file()

