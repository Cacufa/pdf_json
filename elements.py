from socket import if_nameindex


class Element:
    def __init__(self, type, id=123, align="left", bold=False, underline=False, width=200, height=200, labelWidthPercentage=45):
        self.type = type
        self.id = id
        self.align = align
        self.bold = bold
        self.underline = underline
        self.width = width
        self.height = height
        self.labelWidthPercentage =  labelWidthPercentage
    
    def get_element(self):
        return {"type" : self.type,
                "id" : self.id,
                "align" : self.align,
                "bold" : self.bold,
                "underline" : self.underline,
                "width" : self.width,
                "height" : self.height,
                "labelWidthPercentage" : self.labelWidthPercentage
                        }
    
    def new_line(self):
        return {"type" : "newline"}

    def text_element(self, text):
        return {"type" : "text",
                "value": text
                }

if __name__ == "__main__":
    elm = Element("text", 986986)
    element = elm.get_element()
    print(element)
    newline = elm.new_line()
    print(newline)
    text_elem = elm.text_element("This is a test for the text")
    print(text_elem)
