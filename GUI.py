import tkinter as tk
from app import process_data
import json
from pprint import pprint

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=4, rowspan=8)

def clear_text():
    text_results.delete("1.0","end")

def load_csv():
    text_results.delete("1.0","end")
    with open("file.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            text_results.insert("end", line)

def show_json():
    text_results.delete("1.0","end")
    with open("final_file.json","r") as file:
            pdf = json.load(file)

            for line in pdf['sections']:
                container_text = f"{line['name']}-{line['type']}-{line['height']}\n"
                text_results.insert("end", container_text)
                for element in line['elements']:
                    print(element)
                    try:
                        element_text = f"\t{element['id']} - {element['type']}\n"
                        text_results.insert("end", element_text)
                    except KeyError:
                        pass
                #imprimir [dict][elements]
                #text_results.insert("end", value)
            text_results.insert("end", "\n------------------------------------------------------------\n")
            text_results.insert("end", pdf)

def convert_data():
    text_results.delete("1.0","end")
    text_results.insert("end", "\nRunning data")
    process_data()
    text_results.insert("end", "\nData Ready")

def process_csv_from_text():
    data = text_results.get("0.0","end")
    data_list = list(data)

    if data_list.count(",") < 20:
        text_results.delete("1.0","end")
        text_results.insert("end", "\nThis does not look like a valid entry please enter a CSV format")
    else:
        with open("file.txt","w") as file:
            file.write(data)
        text_results.delete("1.0","end")
        text_results.insert("end", "\nFile Created, you can now process it!")
    
#labels
instructions = tk.Label(root, text= "This is a tool to upload a CSV File and you will be able to get a JSON \n\ngroup,name of the group,vcontainer,200,TRUE\nname of the group,field,Field id,Text,Field name", font="Raleway")
instructions.grid(columnspan=4, column=0, row=0)

# field_name_lb = tk.Label(root, text= "Field name", font="Raleway")
# field_name_lb.grid(column=1, row=1)

#buttons
process_text = tk.StringVar()
process_data_btn = tk.Button(root, textvariable=process_text, command=lambda:convert_data(), font="Railway")
process_text.set("Process")
process_data_btn.grid(column=0, row=1)

create_csv_text = tk.StringVar()
create_csv_btn = tk.Button(root, textvariable=create_csv_text, command=lambda:process_csv_from_text(), font="Railway")
create_csv_text.set("Create CSV from text box")
create_csv_btn.grid(column=0, row=2)

clear_text_str = tk.StringVar()
clear_btn = tk.Button(root, textvariable=clear_text_str, command=lambda:clear_text(), font="Railway")
clear_text_str.set("Clear")
clear_btn.grid(column=0, row=3)

load_csv_text_str = tk.StringVar()
load_csv_btn = tk.Button(root, textvariable=load_csv_text_str, command=lambda:load_csv(), font="Railway")
load_csv_text_str.set("Load CSV")
load_csv_btn.grid(column=0, row=4)

show_json_text_str = tk.StringVar()
show_json_btn = tk.Button(root, textvariable=show_json_text_str, command=lambda:show_json(), font="Railway")
show_json_text_str.set("Show Json")
show_json_btn.grid(column=0, row=5)

#Fields
# field_name = tk.Entry(root)
# field_name.grid(column=2, row=1)

text_results = tk.Text(root)
text_results.grid(column=1, row=1, rowspan=8)
#text_results.insert(0.0, "test")

root.mainloop()