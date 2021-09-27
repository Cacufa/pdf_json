import csv
import json


def process_data():
    file_name = "file.csv" #input('Enter a File Name: ')
    #holder = {}
    #holder['sections']=[]
    with open("base.json","r") as json_file:
        holder = json.load(json_file)
    count = -1
    with open(file_name, 'r') as file: # open the csv file.
        raw_data = csv.reader(file, delimiter=',')
        for data in raw_data:
            if data[0] == "group":
                temp_group = {}
                temp_group[data[1]] = []
                container = process_container(data)
                holder['sections'].append(container)
            elif data[1] == "field":
                field = process_field(data)
                insert_field(holder,data[0],field)

    with open("final_file.json","w") as fp:
        json.dump(holder,fp)
        


def process_container(container):
    ##called by process_data
    dict = {}
    dict['elements'] = []
    dict["name"] =container[1]
    dict["type"] = container[2]
    dict["maxwidth"] = 1
    dict["height"] = container[3]
    dict["bordered"] = container[4]
    return dict

def insert_field(data,cont_name,field):
    '''in order to find the container route elements based on cont name 
    we need to iterate in to the dict elements and validate 
    '''
    count = 0
    for item in data['sections']:
        if cont_name == item['name']: #if the containe name is the same as provided insert the field
            data['sections'][count]['elements'].append(field)
        count += 1

def process_field(field):
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
    process_data()

    

if __name__ == '__main__':
    run()