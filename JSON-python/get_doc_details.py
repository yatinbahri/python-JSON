import json

PATH = 'json_file/api-response.json'        # Update the path by adding a sample file to json_file folder or provide direct path
status = 'DONE'                             # Update status to get document details based on new status
filename = '10.pdf'                         # Update filename to get document details based on new file name


# Solution to problem 1
PARSE_DATA = ''

def get_document_status(path):
    # Variables
    status_list = []
    output = {}
    global PARSE_DATA

    json_file = open(path, 'r')
    extract_data = json_file.read()
    response_data = json.loads(extract_data)
    PARSE_DATA = response_data['payload']['items']

    for i in range(len(PARSE_DATA)):
        status_list.append(PARSE_DATA[i]['status'])

    # Creating a unique set of status
    unique_status = set(status_list)

    # Change type from set to list
    unique_status = list(unique_status)

    for i in range(len(unique_status)):
        output[unique_status[i]] = status_list.count(unique_status[i])

    return output  # Returns unique status as a dictionary


get_document_status(PATH)   # # To print result in json format print(json.dumps(get_document_status(PATH), indent= 2))


# Solution to Problem 2


def get_details_via_status(status):
    # Variable
    output = []

    # Status validation using Problem 1

    if status in get_document_status(PATH).keys():

        for i in range(len(PARSE_DATA)):

            if PARSE_DATA[i]['status'] == status:
                new_list = PARSE_DATA[i]['document_id'], PARSE_DATA[i]['collection_id'], PARSE_DATA[i]['file_name'], \
                           PARSE_DATA[i]['created_date'], PARSE_DATA[i]['revision_number']
                output.append(new_list)

    # else:
    # print("No file found with given status '{}' ".format(status))  # Un-comment if needed to print the validation message

    return output   # Returns a list of documents details based on status passed as argument


get_details_via_status(status)      # To print result in json format print(json.dumps(get_details_via_status(status), indent= 2))


# Solution to Problem 3

def get_details_via_filename(filename):
    # Variable
    output = []

    get_document_status(PATH)

    for i in range(len(PARSE_DATA)):
        if filename in (PARSE_DATA[i]['file_name']):  # Check file name exists in the json
            new_list = PARSE_DATA[i]['document_id'], PARSE_DATA[i]['collection_id'], PARSE_DATA[i]['status'], \
                       PARSE_DATA[i]['created_date'], PARSE_DATA[i]['revision_number']
            output.append(new_list)

    return output # Returns a list of documents details based on file name passed as argument


get_details_via_filename(filename)  #  print(json.dumps(get_details_via_filename(filename), indent=2))
