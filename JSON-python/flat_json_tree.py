import json

file_open = open('json_file/flat.json','r')  # Update the path by adding a sample file to json_file folder or provide direct path
read_file = file_open.read()
file_data = json.loads(read_file)  # json object

# Global Variable
PARENT_CHILD_KEY = ''


def flat_tree(file_data):
    # Variables
    item = []
    result = {}
    output = {}
    for page_key, page_dict in file_data.items():  # for loop to fetch the key (Parent node)
        if isinstance(page_dict, dict):
            for key, value in page_dict.items():
                item.append(page_key + '_' + key)
        result[page_key] = item.copy()
        result2 = recursive(page_dict, result, page_key)  # Calling the recursive function
        output = {**result, **result2}
    return output


def recursive(dict2, result, page_key):  # Returns keys(Parent node) of nested dict and add them to child node
    global PARENT_CHILD_KEY
    PARENT_CHILD_KEY = ''  # Make the variable empty for next parent key value
    item = []

    for key, value in dict2.items():
        PARENT_CHILD_KEY = page_key
        if type(value) is dict:  # Checks if the value is a dictionary
            for i in range(len(value.keys())):
                item.append(page_key + '_' + key + '_' + str(list(value.keys())[i]))
            result[page_key + '_' + key] = item.copy()
            item.clear()  # To clear the list which contains results from previous iteration

            PARENT_CHILD_KEY = PARENT_CHILD_KEY + '_' + key
            recursive(value, result, PARENT_CHILD_KEY)

        else:
            result[PARENT_CHILD_KEY + '_' + key] = value

    return result


print(flat_tree(file_data))
