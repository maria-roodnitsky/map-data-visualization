# Name: Maria Roodnitsky
# Date: 5/24/2019
# Purpose: Define the vertex class

from cs1lib import *


class Vertex:
    def __init__(self, vertex_name, x_position, y_position, adjacent_list):  # initialize instance variables in correct
        self.vertex_name = str(vertex_name)                                     # type
        self.x_position = int(x_position)
        self.y_position = int(y_position)
        self.adjacent_list = adjacent_list
        self.vertex_start = False  # identifies vertex as start
        self.vertex_path = False  # identifies vertex as part of the path to the goal

    def __str__(self):

        adjacent_str = ""  # initialize the empty string of adjacent vertex names

        for i in range(0, (len(self.adjacent_list) - 1)):  # add the name of each adjacent vertex to this string with a
            adjacent_str += self.adjacent_list[i].vertex_name + ", "  # comma, except the last

        adjacent_str += self.adjacent_list[-1].vertex_name  # add the name of the last adjacent vertex without a comma

        return self.vertex_name + "; Location: " + str(self.x_position) \
            + ", " + str(self.y_position) + "; " + adjacent_str

    def draw_vertex(self):  # draws a circle at the location of the vertex

        enable_fill()
        disable_stroke()

        if self.vertex_start or self.vertex_path:  # if the vertex is in the path, it is red
            set_fill_color(1, 0, 0)
        else:  # otherwise, the vertex is blue
            set_fill_color(0, 0, 1)

        draw_circle(self.x_position, self.y_position, 7)

    def draw_paths(self):  # draw the lines connecting the vertexes

        set_stroke_width(3)
        enable_stroke()

        for connecting in self.adjacent_list:  # connect each vertex to its adjacent vertexes

            if (self.vertex_start or self.vertex_path) and (connecting.vertex_start or connecting.vertex_path):
                set_stroke_color(1, 0, 0)  # if the two vertexes are on the path, draw a red line
            else:
                set_stroke_color(0, 0, 1)  # if not, a blue line
            draw_line(self.x_position, self.y_position, connecting.x_position, connecting.y_position)

    def start(self, sm_x, sm_y):  # if the mouse is pressed within the vertex, it is the start (set boolean to true)

        if self.x_position - 6 <= sm_x <= self.x_position + 6 and self.y_position - 6 <= sm_y <= self.y_position + 6:
            self.vertex_start = True
        else:
            self.vertex_start = False

    def rolled(self, m_x, m_y):  # if the mouse is rolled over the vertex, it is the goal vertex (set boolean to true)

        if self.x_position - 6 <= m_x <= self.x_position + 6 and self.y_position - 6 <= m_y <= self.y_position + 6:
            self.vertex_path = True
        else:
            self.vertex_path = False
