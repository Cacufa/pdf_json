from elements import Element

class Container:

    def __init__(self, name, elements=[], heigth=200, type="vcontainer", bordered=True):
        self.name = name
        self.height = heigth
        self.elements = [{"type":"text", "value":self.name}]
        self.type = type
        self.bordered = bordered

    def get_cont(self):
        return {"elements":self.elements,
                "name":self.name,
                "height":self.height,
                "type":self.type,
                "bordered":self.bordered
                }

    def add_element(self, element):
        input("function add element")
        #print(self.elements)
        input("Next appending element")
        self.elements.append(element)


if __name__ == "__main__":
    ele = Element("select", 9645567)
    element = ele.get_element()
    newline = ele.new_line()
    print("Elements---------------- ")


    print("-")
    print("Container ---------------------- ")
    cont = Container("test")
    print(cont.get_cont())


    print("-")
    print("Add element to container")
    
    data = cont.get_cont()

    cont.add_element(element)
    cont.add_element(newline)
    print(data)

