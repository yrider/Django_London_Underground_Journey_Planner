"""
Py file for first page form. Takes input from user (station one, two and the time of travel)
"""
import datetime as dt
import pandas as pd
from django import forms

# Creating dataframe for unique station list to pass into station_choices
df = pd.read_excel('LondonUndergroundPlanner/backend_code/TrainDataWithDLR.xlsx')

# creating a list with unique station values to return to the user on first page
unique_station_list = df['Station One'].unique()
unique_station_list.sort()

# Setting initial variables to input into form class
STATION_CHOICES = []
TIME_CHOICES = []

# looping through unique station list and appending values as tuples (required for Django forms)
for station in unique_station_list:
    STATION_CHOICES.append((station, station))

# Creating list of hours for required time range and appending values to new list as tuple pairs
hours = [(dt.time(i).strftime('%I%p')) for i in range(5, 24)]
for hour in hours:
    TIME_CHOICES.append((hour, hour))


class JourneyForm(forms.Form):
    """
    Class creates a form that is passed into the first page template to handle the user's journey information
    """
    first_station = forms.CharField(
        label='From Station:',
        widget=forms.Select(
            choices=STATION_CHOICES,
            attrs={'placeholder': 'From',
                   'class':'form-control'
            }
        )
    )
    second_station = forms.CharField(
        label='To Station:',
        widget=forms.Select(
            choices=STATION_CHOICES,
            attrs={'placeholder': 'To',
                   'class': 'form-control'
            }
        )
    )
    time = forms.CharField(
        label="Select a time:",
        widget=forms.Select(
            choices=TIME_CHOICES
        )
    )
