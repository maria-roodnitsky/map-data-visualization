# Author: Maria Roodnitsky
# Date: 5/31/2019
# Purpose: Take a starting vertex, find the shortest path to a goal vertex, return a list of visited vertex objects
#           along the path.

from collections import deque


def search(start, goal):

    path_dict = {start: None}  # create a dictionary of paths where the key is the
    location_queue = deque()     # location object, the value is the prior location
    location_queue.append(start)  # add the starting location to the queue

    while len(location_queue) != 0:  # continue while the queue is not empty

        current = location_queue.popleft()  # pop a location vertex off of the queue

        for vertex in current.adjacent_list:
            if vertex not in path_dict:  # if the vertex is not in the dictionary, add it, and make its value the
                path_dict[vertex] = current  # preceding vertex
                location_queue.append(vertex)  # add the vertex to the queue

        if current == goal:  # if you have reached the goal, make a list of the places visited along the path
            path = []
            while current is not None:
                path.append(current)  # add the location to the path
                current = path_dict[current]  # trace back
            return path



