"""
Py file containing view functions to render templates to the user and handle backend functionality
"""
import datetime as dt
import calendar
import openpyxl
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import JourneyForm
from .backend_code.excel_manipulation import excel_manipulation
from .backend_code.algorithms import dijkstras_algorithm, find_route_lines, change_line_info

# Importing Excel file and using openpyxl to manipulate it

# Excel import below for edited dataset with DLR line:
excel_file = openpyxl.load_workbook(
    'LondonUndergroundPlanner/backend_code/TrainDataWithDLR.xlsx'
)
sheet = excel_file.active  # activating Excel file (required with openpyxl)

# Setting global variable required to show information to user on results page
global RESULTS_CONTEXT

# List of off-peak hours appending to list
off_peak_hours = [(dt.time(i).strftime('%I%p')) for i in range(9, 16)]
for i in range(19, 24):
    off_peak_hours.append((dt.time(i).strftime('%I%p')))


class HomeView(TemplateView):
    """
    Class renders the home_page.html template to the user and handles their get & post requests
    """
    template_name = 'home_page.html'

    def get(self, request):
        """
        Get method handles user request and renders home_page on browser with form
        """
        # Form instance created from forms.py (so user can choose input in combo boxes)
        form = JourneyForm()
        # Context dict renders form and title on head of browser to the user
        context = {
            'form': form,
            'title': 'Home'
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """
        Post method handles user information for second page
        """
        # User has sent a post request which is saved to form
        form = JourneyForm(request.POST)

        # if user has inputted correct information
        if form.is_valid():

            # create variables from user input
            station_one = form.cleaned_data.get('first_station')
            station_two = form.cleaned_data.get('second_station')
            journey_time = form.cleaned_data.get('time')

            # if stations inputted are the same returns error message at top of page
            if station_one == station_two:
                messages.error(
                    request,
                    f'You are already at {station_two}'
                    '. Please select another station'
                )
                return redirect('home')

            # Loop checks whether the user is travelling during a peak time or not
            off_peak = False
            for hour in off_peak_hours:
                # if the user's travel time is in off_peak_hours
                if journey_time == hour:
                    # off_peak is true i.e Bakerloo runs at normal speed
                    off_peak = True

            # calling functions from other files to find shortest path from start to end station
            station_dll = excel_manipulation(sheet, off_peak)  # var for dlr doubly_linked_list

            # call algorithms to find the shortest route from input and the lines of the route
            shortest_route = dijkstras_algorithm(station_dll, station_one, station_two)
            train_lines, minutes = find_route_lines(station_dll, shortest_route)

            # variables set to calculate the total journey time for user and render through template
            travel_times = [0, ]
            total_travel_time = 0

            # Loop through range of the length of the minutes variable (created on line 71)
            for minute in range(len(minutes)):
                # This section adds an additional minute per station due to stopping for that time
                total_travel_time = minutes[minute] + 1 + total_travel_time
                travel_times.append(total_travel_time)

            # creating new variables to show journey summary
            main_lines, change_lines_index = change_line_info(train_lines)

            # create variables to output journey summary to user e.g when to stop and change lines
            prev_station = 0
            from_station_change_list = []
            to_station_change_list = []
            line_change_list = []

            # Loop updates above variables which are looped through in home_page.html
            for value in change_lines_index:
                line_change_list.append(main_lines[value])
                from_station_change_list.append(shortest_route[prev_station])
                to_station_change_list.append(shortest_route[value])
                prev_station = value

            # setting global variable which is used to render journey information to user
            global RESULTS_CONTEXT
            # RESULTS CONTEXT contains all variables that are rendered to the user
            #   through results function below
            RESULTS_CONTEXT = {
                # Next three lines render user's input on results page
                'station_one': station_one,
                'station_two': station_two,
                'time': journey_time,
                # Next three lines tell the user the day and month of their travel
                'weekday': dt.datetime.today().strftime('%A'),
                'weekday_int': dt.datetime.today().strftime('%d'),
                'month': calendar.month_name[dt.datetime.today().month],
                # Variables below are all for rendering train information to the user
                # rendered with Python in templates/results_page.html
                'last_line': main_lines[-1],
                'last_from_station': shortest_route[prev_station],
                'last_station': shortest_route[-1],
                'shortest_route': shortest_route,
                'train_lines': train_lines,
                'minutes': minutes,
                'total': travel_times,
                'total_sum': total_travel_time,
                'from_station_change_list': from_station_change_list,
                'to_station_change_list': to_station_change_list,
                'line_change_list': line_change_list,
            }

        # All algorithms completed, now redirect to results page and render journey variables
        return redirect('results')


def results_page(request):
    """
    Function handles get request from user to render final journey information
    """
    global RESULTS_CONTEXT

    # adding additional context to show on html file
    RESULTS_CONTEXT['title'] = 'Your Journey Results'

    return render(request, 'results_page.html', RESULTS_CONTEXT)
