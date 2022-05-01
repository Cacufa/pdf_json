import tkinter as tk
from app import process_data

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#functions

def convert_data():
    text_results.delete("1.0","end")
    text_results.insert("end", "\nRunning data")
    process_data()
    text_results.insert("end", "\nData Ready")

def process_csv_from_text():
    data = text_results.get("0.0","end")
    print(data)
    with open("file.csv","w") as file:
        file.write(data)

    


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
create_csv_text.set("Get CSV from text box")
create_csv_btn.grid(column=1, row=1)

#Fields
# field_name = tk.Entry(root)
# field_name.grid(column=2, row=1)

text_results = tk.Text(root)
text_results.grid(column=0, row=4, columnspan=3)
#text_results.insert(0.0, "test")

root.mainloop()