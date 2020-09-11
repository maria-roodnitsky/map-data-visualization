# Author: Maria Roodnitsky
# Date: 5/31/2019
# Purpose: Draw a dynamic map of Dartmouth's campus that identifies and draws shortest paths between locations

from load_graph import dartmouth_places
from cs1lib import *
from bfs import search

dartmouth_image = load_image("dartmouth_map.png")  # load the Dartmouth map

m_x = 0  # initialize the rolling mouse and pressed mouse locations to (0, 0)
m_y = 0
sm_x = 0
sm_y = 0


def mouse_location(x, y):  # track where the mouse is rolling
    global m_x, m_y
    m_x = x
    m_y = y


def start_mouse_location(x, y):  # track where the mouse has been pressed, 's' prefix is to differentiate as start
    global sm_x, sm_y
    sm_x = x
    sm_y = y


def main():

    start = None  # initialize start and end to None
    end = None

    draw_image(dartmouth_image, 0, 0)

    for place in dartmouth_places:
        dartmouth_places[place].start(sm_x, sm_y)  # check to see if the vertex has been clicked as 'start'
        dartmouth_places[place].rolled(m_x, m_y)  # check to see if the vertex has been rolled over as a 'goal'
        if dartmouth_places[place].vertex_start:  # if this is the start, save the object in a 'start' variable
            start = dartmouth_places[place]
        if dartmouth_places[place].vertex_path:  # if this is the goal, save the object in a 'end' variable
            end = dartmouth_places[place]

    if start is not None and end is not None:  # if there is a start and end, perform bfs

        path = search(start, end)  # create a list of visited locations

        for place in path:
            place.vertex_path = True  # for every place in the path, set the path boolean variable to True

    for place in dartmouth_places:  # draw all of the paths in the correct colors
        dartmouth_places[place].draw_paths()

    for place in dartmouth_places:  # draw all of the vertexes in the correct color on top of the paths
        dartmouth_places[place].draw_vertex()


start_graphics(main, width=1012, height=811, mouse_press=start_mouse_location, mouse_move=mouse_location)
