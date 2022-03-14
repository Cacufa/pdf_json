from elements import *

class Container:

    def __init__(self, name, elements=[{"new":1}], heigth=200, type="vcontainer", bordered=True):
        self.name = name
        self.height = heigth
        self.elements = elements
        self.type = type
        self.bordered = bordered

    def get_cont(self):
        return {"elements":self.elements,
                "name":self.name,
                "height":self.height,
                "type":self.type,
                "bordered":self.bordered
                }

    def add_element(self, pdf, element):
        pdf["sections"][0]["elements"].append()
        input("Continue")
        print(element)
        self["elements"].append(element)

if __name__ == "__main__":
    ele = Element("select", 9645567)
    element = ele.get_element()
    newline = ele.new_line()
    cont = Container("test")

    print(cont.get_cont())
    cont.add_element(element)


    data = cont.get_cont()
    print(data)
    cont.add_element(data, "element added")
    print(data)

