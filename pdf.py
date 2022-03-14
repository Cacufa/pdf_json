import json
import csv
from pkgutil import iter_importers
from unicodedata import name
from pprint import pprint

class Pdf:
    def __init__(self):
        with open("base.json","r") as file:
            self.pdf = json.load(file)

    def get_pdf(self):
        return self.pdf

    def print_items(self, items):
        if type(items) is dict:
            items = {key:value for key,value in items.items()}
            print(items)
            return items
        elif type(items) is list:
            items = [item for item in items]
            print(items)
            return items
        else:
            return None


    def inspection(self):
        pprint(self.pdf)




                
if __name__ == '__main__':
    pdf = Pdf()
    pdf_data = pdf.get_pdf()
    #print(pdf_data["sections"])
    pdf.inspection()