"""
Python file containing main algorithms e.g Dijkstra's algorithm, route lines and changing lines
"""


def dijkstras_algorithm(linked_list, start, end):
    """
    Function for finding shortest path from start station to end station
        through Dijkstra's algorithm

    :arg linked_list: doubly linked list containing all stations
    :arg start: starting station as a string
    :arg end: target station as a string
    Return: path, a list variable containing the stations visited from start to end stations
    """
    # setting initial variables
    # current_station = linked_list._head     # current station is set to head of linked list

    graph = {}                       # dictionary containing all stations
    weighted_costs = {}              # accumulative costs for stations as we visit new ones
    previous_nodes = {}              # dictionary to keep track of previous stations visited
    shortest_path = []               # list containing names of stations visited for shortest path

    # iterate through doubly linked list and add each station to the dictionary graph
    for station in linked_list.iterate_dll():
        graph[station[0]] = station[1]

    # unvisited initially contains all stations which will be deleted during while loop until empty
    unvisited = graph

    # each station time is initially set to infinity as we have not yet visited any
    for station in unvisited:
        weighted_costs[station] = float('inf')

    # first station distance is equal to 0 as we have not travelled anywhere
    weighted_costs[start] = 0

    # while unvisited is not empty dijkstras algorithm is not complete
    while unvisited:
        # min_node is initially set to None
        min_node = None
        # loop through graph of unvisited stations
        for station in unvisited:
            # find the shortest distance and update costs if the current cost is
                # greater than the new cost
            if min_node is None:
                min_node = station
            # if the weighted cost of the current station is less than the min_node
                # update value with smaller cost
            elif weighted_costs[station] < weighted_costs[min_node]:
                min_node = station
        # loop through the connections of the minimum node
        for connection in graph[min_node]:

            temp = connection
            neighbour = temp[0]
            cost = temp[1]
            if cost + weighted_costs[min_node] < weighted_costs[neighbour]:
                weighted_costs[neighbour] = cost + weighted_costs[min_node]
                previous_nodes[neighbour] = min_node

        # Delete the current min_node from the unvisited dictionary
        del unvisited[min_node]
        # while loop continues until the unvisited dictionary is empty i.e all
            # stations have been visited/boxed

    # Once all nodes have been boxed find the shortest path by going through previous steps

    target_station = end
    # While start station is not equal to the end station
    while target_station != start:
        shortest_path.insert(0, target_station)
        target_station = previous_nodes[target_station]
    shortest_path.insert(0, target_station)

    # Rreturn the shortest path, a list containing the stations visited from the start to end
    return shortest_path


def find_route_lines(linked_list, route):
    """
    Function returns the lines of the stations visited in shortest route
        and the time of the total route

    :arg linked_list: doubly linked list of all stations
    :arg route: shortest path as list containing names of stations visited
    Return: list of lines visited during shortest route and the journey time
    """
    # Set initial variables for algorithm
    train_lines = []          # list of lines visited
    journey_time = []   # journey time in minutes for each station
    line = ""

    # for number in the range of the length of the shortest route
    #   (based on how many stations have been visited)
    for num in range(len(route)):
        # if the number equals the length of the route - 1
        if num == len(route) - 1:
            train_lines.append(line)
        # else, if the number is greater than the length of the shortest route
        elif num < len(route):
            line, minute = linked_list.find_details(route[num], route[num+1])
            train_lines.append(line)
            journey_time.append(minute)
    return train_lines, journey_time


def change_line_info(lines):
    """
    Function returns information for journey summary i.e when the user must change lines

    :arg lines: lines list created from route_lines (list of all station lines visited)
    :return: list of lines for each station that is passed through (instead of station)...
        changes_index returns list of numbers where user must get of line and move to different one
    """
    # set initial variables for algorithm
    first_line = lines[0]   # equal to the first line that is visited during the shortest route
    interchanges = []   # list of specific numbers that explain when the user must change lines

    # for number in the range of the length of the lines visited
    for num in range(len(lines)):
        if lines[num] != first_line:
            lines[num], first_line = first_line, lines[num]
            interchanges.append(num)

    # return the variables lines and interchanges
    return lines, interchanges
