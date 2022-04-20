import csv
import json
import tkinter as tk
from tkinter import ttk
from tkinter import constants


class CSV_IMPORT():

    def __init__(self):
        raiz = tk.Tk()
        raiz.geometry('900x600')
        raiz.configure(bg = 'beige')
        raiz.title('Aplicación')
        ttk.Button(raiz, text='process data', 
                   command=self.process_data).grid(row=2,column=0)

        self.messg_entry = tk.Entry(raiz, width=60).grid(row=0, column=1, columnspan=8)

        ttk.Label(raiz,text="Messages:").grid(row=0,column=0)
        
        ttk.Button(raiz, text='Salir', 
                   command=raiz.destroy).grid(row=5,column=0)

        ## Labels and text
        self.text = tk.Text(raiz, height = 20, width = 75).grid(row=1, column=3, rowspan=5, columnspan=5)
        self.text.insert(constants.INSERT, "test")
        #txt.insert(constants.INSERT,'You text goes here') # recommend
                
        raiz.mainloop()



    def insert_field(self,data,cont_name,field):
        '''in order to find the container route elements based on cont name 
        we need to iterate in to the dict elements and validate'''
        count = 0
        for item in data['sections']:
            if cont_name == item['name']: #if the containe name is the same as provided insert the field
                data['sections'][count]['elements'].append(field)
            count += 1

    def process_data(self):
        self.messg_entry.insert(0, "status bar")
        file_name = "file.csv" #input('Enter a File Name: ')
        #holder = {}
        #holder['sections']=[]
        spacer_field = {"type": "newline"}
        with open("base.json","r") as json_file:
            holder = json.load(json_file)
        count = -1
        with open(file_name, 'r') as file: # open the csv file.
            raw_data = csv.reader(file, delimiter=',')
            for data in raw_data:
                print(data)
                if data[0] == "group":
                    temp_group = {}
                    temp_group[data[1]] = []
                    container = self.process_container(data)
                    holder['sections'].append(container)
                elif data[1] == "field":
                    field = self.process_field(data)
                    self.insert_field(holder,data[0],field)
                    self.insert_field(holder,data[0],spacer_field)

        with open("final_file.json","w") as fp:
            json.dump(holder,fp)
            


    def process_container(self, container):
        ##called by process_data
        dict = {}
        dict['elements'] = []
        dict["name"] =container[1]
        dict["type"] = container[2]
        dict["maxwidth"] = 1
        dict["height"] = container[3]
        dict["bordered"] = container[4]
        return dict

    def process_field(self,field):
        ##called by process_data
        element = {}
        try:
            if field[3] == "List":
                element['type'] = "select"
                element['align'] = "left"
                element['id'] = int(field[2])
            elif field[3] == "Signature":
                element['type'] = "signature"
                element['align'] = "left"
                element['id'] = int(field[2])
                element['width'] = 200
            elif field[3] == "Photo":
                element['type'] = "image"
                element['align'] = "left"
                element['id'] = int(field[2])
                element['width'] = 200
            else:
                element['type'] = "text"
                element['align'] = "left"
                element['id'] = int(field[2])
        except:
            print("Issue found")
        return element


def run():
    print("Process Started")
    mi_app = Aplicacion()
    print("Process Ended")
    

if __name__ == '__main__':
    run()