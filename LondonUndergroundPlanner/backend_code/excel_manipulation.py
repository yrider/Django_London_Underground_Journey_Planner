"""
Py file containing function for manipulating excel file with station information
"""
# When running code in Python, the below full-stop after 'from' must be removed
# When running Django, the below import full-stop must be kept i.e from .linked_lists... 
from .linked_lists import DoublyLinkedList

# Below function manipulates excel file that has been edited with DLR information
#  file is saved as LondonUndergroundDataDLR.xlsx


def excel_manipulation(sheet, peak_time):
    """
    Params
    ------
    sheet: sheet is the Excel file manipulated through openpyxl library
    peak_time: boolean value that determines whether the user is
        travelling at a peak time or not
    """
    linked_list = DoublyLinkedList()        # Set initial linked_list to insert data

    # first for loop inserts station information to create nodes for doubly linked list
    # importing Excel file as sheet
    for row in sheet.iter_rows(min_row=1, min_col=1, max_row=901, max_col=2):

        # for the cell value within each row
        for cell in row:
            # repeated initially set to False
            repeated = False
            # check that the value of a cell has information in it and not empty
            if cell.value is not None:
                # loop through the linked list iteration
                for node in linked_list.iterate_dll():
                    # check whether the value of the excel cell is equal to the station name
                    if cell.value == node[0]:
                        # if true then repeated is set to True
                        repeated = True
                # if the value has not been repeated i.e it's unique
                if not repeated:
                    # add value into doubly linked list as a node
                    # cell.value is equal to the station name
                    linked_list.insert_dll_node(cell.value)

    # Second for loop now saves connection information into each doubly linked list node

    # loop through the iteration of the current doubly linked list
    for station in linked_list.iterate_dll():
        # row format is the same as excel format (train line, station one, station two, time)
        for row in sheet.iter_rows(min_row=25, min_col=1, max_row=901, max_col=4):
            # check that the value of row 2 (station two) is not empty
            if row[2].value is not None:
                # if station station one in excel sheet equals the station name
                #   of the doubly linked list node
                if row[1].value == station[0]:
                    # if the user is travelling at a peak time and through the Bakerloo line
                    if peak_time and row[0].value == 'Bakerloo':
                        # then values for the line need to be halved
                        #   i.e trains run at double the speed
                        time = row[3].value / 2
                        # finally insert the singly linked list information
                        #   into the doubly linked list
                        linked_list.insert_connections(row[1].value, row[2].value, time, row[0].value)
                        linked_list.insert_connections(row[2].value, row[1].value, time, row[0].value)
                    # else the user is travelling out of peak times
                    #  i.e the Bakerloo line runs at normal speed
                    else:
                        linked_list.insert_connections(row[1].value, row[2].value, row[3].value, row[0].value)
                        linked_list.insert_connections(row[2].value, row[1].value, row[3].value, row[0].value)

    # return the doubly linked list which now contains all train information
    return linked_list
