import csv



def process_data():
    file_name = "file.csv" #input('Enter a File Name: ')
    holder = {}
    holder['sections']=[]
    with open(file_name, 'r') as file:
        raw_data = csv.reader(file, delimiter=',')
        for data in raw_data:
            print("")
            print(data)
            if data[0] == "group":
                temp_group = {}
                temp_group[data[1]]
                print("container found")
                container = process_container(data)
                print(container)
            elif data[0] == "field":
                field = process_field(data)
                

                print(field)


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
        if field[0] == "List":
            element['type'] = "select"
            element['align'] = "left"
            element['id'] = int(field[1])
        elif field[0] == "Signature":
            element['type'] = "signature"
            element['align'] = "left"
            element['id'] = int(field[1])
            element['width'] = 200
        elif field[0] == "Photo":
            element['type'] = "image"
            element['align'] = "left"
            element['id'] = int(field[1])
            element['width'] = 200
        else:
            element['type'] = "text"
            element['align'] = "left"
            element['id'] = int(field[1])
    except:
        print("Issue found")

    return element

def run():
    process_data()



if __name__ == '__main__':
    run()