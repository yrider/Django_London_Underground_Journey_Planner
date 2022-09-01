"""
Py file containing DoublyLinkedList and SinglyLinkedList classes for saving train data
"""

class SinglyLinkedList:
    """
    SinglyLinkedList contains information on a station's connections
    Main station is saved as a DoublyLinkedList Node
    """
    class Node:
        """
        Nested node class containing singly linked list information
        """
        def __init__(self, station, time, line):
            """
            :param station: name of connecting train station as a string
            :param time: time in minutes between train stations
            :param line: name of train line as a string
            """
            self._station = station
            self._time = time
            self._line = line
            self._next_node = None

    def __init__(self):
        """
        Class initialiser for SinglylinkedList
        """
        self._head = None

    def insert_sll_node(self, station, data, line):
        """
        method takes train information and stores it within SinglyLinkedList
        """
        # if the list is empty, insert new node at start of list
        if self._head is None:
            new_node = self.Node(station, data, line)
            self._head = new_node
        else:
            # else the list is not empty, iterate through nodes until end of list
            new_node = self.Node(station, data, line)
            temp_node = self._head
            while temp_node._next_node:
                temp_node = temp_node._next_node
            # insert new node as the next node value of the current last node
            temp_node._next_node = new_node
            # the next node of the newly entered node is now set to none (end of list)
            new_node._next_node = None

    def find_connections(self):
        """
        Method iterates through singly linked list and finds connection info
        """
        # set initial value as head of list
        temp_node = self._head
        connections = []
        # while the current node is not none, continue to iterate through list
        while temp_node:
            # insert the current stations connection information into list
            connections.append([temp_node._station, temp_node._time])
            temp_node = temp_node._next_node
        # return list of full connections for each station
        return connections

    def print_sll_info(self):
        """
        Method iterates through singly linked list and prints all information
        """
        # set initial value as head of list
        temp_node = self._head
        # while the current node is not none, continue to iterate through list
        while temp_node:
            print(f'Connection: {temp_node._station} {temp_node._time} {temp_node._line}')
            temp_node = temp_node._next_node

    def train_details(self, station):
        """
        Method iterates through list and returns details for a specific train
        param station: string of specific station to find details for it
        """
        # set initial value as head of list
        temp_node = self._head
        # while next node is a node and the current station not equal to station param
        while temp_node._next_node is not None and temp_node._station != station:
            # continue through list
            temp_node = temp_node._next_node
        # return information for the current station
        return temp_node._line, temp_node._time


class DoublyLinkedList:
    """
    DoublyLinkedList contains information for each main station in excel file
    Contains SinglyLinkedList which contains connection information
    """
    class Node:
        """
        Nested node class containing singly linked list information
        """
        def __init__(self, station):
            """
            :param station: name of the current station as a string
            """
            self._station = station
            self._connections = SinglyLinkedList()
            self._next_node = None
            self._prev_node = None

    def __init__(self):
        """
        Class initialiser for DoublyLinkedList
        """
        self._head = None


    def insert_dll_node(self, station):
        """
        method takes current station name and creates node with value
        """
        # if the list is empty, insert new node at start of list
        if self._head is None:
            new_node = self.Node(station)
            # new node is head of list so prev_node = None
            new_node._prev_node = None
            self._head = new_node
        else:
            # else the list is not empty, iterate through nodes until end of list
            new_node = self.Node(station)
            # set temp node equal to start of list for iterating
            temp_node = self._head
            while temp_node._next_node:
                temp_node = temp_node._next_node
            # insert new node as the next node value of the current last node
            temp_node._next_node = new_node
            # prev_node now equal to the previous last node
            new_node._prev_node = temp_node
            new_node._next_node = None

    def iterate_dll(self):
        """
        Method iterates through linked list and yields its information
        """
        temp_node = self._head
        # while not at end of list
        while temp_node:
            # yield station name and information for each connection
            # variable equal to list of lists containing station names and travel time
            yield temp_node._station, temp_node._connections.find_connections()
            # update temp and continue until at end of dll
            temp_node = temp_node._next_node

    def print_dll_info(self):
        """
        Method iterates through singly linked list and prints all information
        """
        # set initial value as head of list
        temp_node = self._head
        # while not at end of list
        while temp_node:
            print(temp_node._station)
            # print info for the station's connections through singly linked list
            temp_node._connections.print_sll_info()
            # update temp and continue until at end of dll
            temp_node = temp_node._next_node

    def find_details(self, station, next_station):
        """
        Method iterates through doubly linked list Until current station is equal to param station
        Then returns information for this station
        Method used in function to find full list of lines for journey

        param station:
        param next_station:
        """
        # set initial node as head of dll
        temp_node = self._head
        # while current station not equal to station param
        while temp_node._station != station:
            # update value and continue through list
            temp_node = temp_node._next_node
        # set variables
        lines, times = temp_node._connections.train_details(next_station)
        # return line and time information from the singly linked list
        return lines, times

    def insert_connections(self, station, connection, time, line):
        """
        Method is used to insert singly linked lists (connection info)
            into each doubly linked list node

        param station: station name as a string
        param connection: the connecting station from the first station as a string
        param time: time in minutes to get from first to second station
        param line: the line as a string which has both stations on it
        """
        # set inital node as head of dll
        temp_node = self._head
        # if the current node's next node is not a node
        if temp_node._next_node is None:
            # insert connection values into sll
            temp_node._connections.insert_sll_node(connection, time, line)
        # else the next node is already a node
        else:
            # iterate through until end of dll or the current station equals the station param
            while temp_node._next_node is not None and temp_node._station != station:
                temp_node = temp_node._next_node
            # insert singly linked list node at
            temp_node._connections.insert_sll_node(connection, time, line)
