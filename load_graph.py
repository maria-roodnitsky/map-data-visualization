# Author: Maria Roodnitsky
# Date: 5/25/2019
# Purpose: Define the load function

from vertex import Vertex


def load_graph(file_name):

    data_file = open(file_name, "r")

    places = {}  # initialize a dictionary to be filled with places

    for line in data_file:
        stripped_line = line.strip()  # strip each line of white space
        line_information = stripped_line.split(";")  # split the line by semicolon
        name = str(line_information[0].strip())  # strip the first information component and store it as a string name

        positions = line_information[2].strip()  # strip the third information component (positions)
        positions = positions.split(",")  # split this component (positions) by comma
        x = positions[0]  # the first component of positions is x; the second, y
        y = positions[1]

        adjacency_list = []

        location = Vertex(name, x, y, adjacency_list)  # return the address of a new Vertex object

        places[name] = location  # create a dictionary entry with the name as the key; the address as the value

    data_file.close()  # close the data file

    data_file = open(file_name, "r")  # reopen the file

    for line in data_file:
        stripped_line = line.strip()   # strip the data
        line_information = stripped_line.split(";")  # split the data by semicolon

        key = line_information[0]  # store the first component (name) of the information as the key

        adjacent_places = line_information[1].strip()  # strip the second component (adjacent vertices)
        adjacent_places = adjacent_places.split(",")  # split this second component (adjacent vertices) by commas

        for place in adjacent_places:
            place = places[place.strip()]  # find the address of each adjacent vertex
            places[key].adjacent_list.append(place)  # append this address to the adjacency list of the key

    return places  # return the dictionary of places


dartmouth_places = load_graph("dartmouth_graph.txt")  # create the dictionary
