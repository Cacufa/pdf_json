import csv



def process_data():
    file_name = "file.csv" #input('Enter a File Name: ')
    holder = {}
    holder['sections']=[]
    count = -1
    with open(file_name, 'r') as file: # open the csb file.
        raw_data = csv.reader(file, delimiter=',')
        for data in raw_data:
            print("")
            if data[0] == "group":
                temp_group = {}
                temp_group[data[1]] = []
                holder['sections'].append(temp_group)
                print("container found")
                container = process_container(data)
            elif data[1] == "field":
                field = process_field(data)
                holder['sections'][count][data[0]].append(field)
            print(holder)
        


def process_container(container):

    elements = {}
    elements["name"] =container[1]
    elements["type"] = container[2]
    elements["maxwidth"] = 1
    elements["height"] = container[3]
    elements["bordered"] = container[4]
    return elements


def process_field(field):
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

def insert_field(holder, elements, item):
    '''find the proper group within the json file and insert the item properly
    1-find the position of the group in the dict-list
    2-insert the item 
    3-return a new holder dict
    '''
    print(holder)
    elements_pos = holder['sections'].index(elements)
    print(elements_pos)
    try:
        holder['sections'][elements_pos][elements].append(item)
    except:
        print("Error inserting item")
    return holder


def run():
    process_data()

    ''' 
   holder = {}
    holder['sections'] = []
    elements = {} 
    elements['elements'] = []
    holder['sections'].append(elements)
    item = {}
    item['name']="carlos"
    item['age'] = 25
    final_holder = insert_field(holder, 'elements', item)
    print(final_holder)
    '''
    

if __name__ == '__main__':
    run()