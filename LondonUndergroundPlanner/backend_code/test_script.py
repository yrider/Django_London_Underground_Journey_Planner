"""
Py file containing unit test classes to test our three main algorithms:
    Dijkstra's algorithm, changing lines algorithm and find route lines
"""
import unittest
import openpyxl
from algorithms import dijkstras_algorithm, change_line_info, find_route_lines
from excel_manipulation import excel_manipulation

# import excel file and create doubly linked lists to to test different outcomes
excel_file = openpyxl.load_workbook(
    'LondonUndergroundPlanner/backend_code/TrainDataWithDLR.xlsx'
)
sheet = excel_file.active

# Creating doubly linked lists used within testing
# Two variables created for tests that are affected or not affected by peak time changes
off_peak_station_dll = excel_manipulation(sheet, False)
peak_station_dll = excel_manipulation(sheet, True)


class TestDijkstrasAlgorithm(unittest.TestCase):
    """
    Unittest class to test different outcomes of Dijkstras Algorithm
    Both off peak and on peak doubly linked lists are tested
    """

    def test_one(self):
        """
        Test one: Perivale station to Oxford Circus
        """
        self.assertEqual(
            dijkstras_algorithm(off_peak_station_dll, 'Perivale', 'Oxford Circus'), [
                'Perivale', 'Hanger Lane', 'North Acton', 'East Acton',
                'White City', "Shepherd's Bush", 'Holland Park', 'Notting Hill Gate',
                'Queensway', 'Lancaster Gate', 'Marble Arch', 'Bond Street',
                'Oxford Circus'
            ]
        )
        self.assertEqual(
            dijkstras_algorithm(peak_station_dll, 'Perivale', 'Oxford Circus'), [
                'Perivale', 'Hanger Lane', 'North Acton', 'East Acton', 'White City',
                "Shepherd's Bush", 'Holland Park', 'Notting Hill Gate', 'Bayswater',
                'Paddington', 'Edgware Road', 'Marylebone', 'Baker Street',
                "Regent's Park", 'Oxford Circus'
            ]
        )

    def test_two(self):
        """
        Test two: Old Street to Neasden
        """
        self.assertEqual(
            dijkstras_algorithm(off_peak_station_dll, 'Old Street', 'Neasden'), [
                'Old Street', 'Angel', "King's Cross St. Pancras", 'Euston Square',
                'Great Portland Street', 'Baker Street', 'Finchley Road', 'West Hampstead',
                'Kilburn', 'Willesden Green', 'Dollis Hill', 'Neasden'
            ]
        )
        self.assertEqual(
            dijkstras_algorithm(peak_station_dll, 'Old Street', 'Neasden'), [
                'Old Street', 'Angel', "King's Cross St. Pancras", 'Euston Square',
                'Great Portland Street', 'Baker Street', 'Finchley Road', 'West Hampstead',
                'Kilburn', 'Willesden Green', 'Dollis Hill', 'Neasden'
            ]
        )

    def test_three(self):
        """
        Test three: Edgware Road to Leyton
        """
        self.assertEqual(
            dijkstras_algorithm(off_peak_station_dll, 'Edgware Road', 'Leyton'), [
                'Edgware Road', 'Baker Street', 'Great Portland Street', 'Euston Square',
                "King's Cross St. Pancras", 'Farringdon', 'Barbican', 'Moorgate',
                'Liverpool Street', 'Bethnal Green', 'Mile End', 'Stratford', 'Leyton'
            ]
        )
        self.assertEqual(
            dijkstras_algorithm(peak_station_dll, 'Edgware Road', 'Leyton'), [
                'Edgware Road', 'Marylebone', 'Baker Street', "Regent's Park",
                'Oxford Circus', 'Tottenham', 'Holborn', 'Chancery Lane',
                "St. Paul's", 'Bank', 'Liverpool Street', 'Bethnal Green',
                'Mile End', 'Stratford', 'Leyton'
            ]
        )

    def test_four(self):
        """
        Test four: Lewisham to Woolwich Arsenal (DLR testing)
        """
        self.assertEqual(
            dijkstras_algorithm(off_peak_station_dll, 'Lewisham', 'Woolwich Arsenal'), [
                'Lewisham', 'Elverson Road', 'Greenwich', 'Cutty Sark', 'Island Gardens',
                'Mudchute', 'Crossharbour', 'South Quay', 'Heron Quays', 'Canary Wharf',
                'North Greenwich', 'Canning Town', 'West Silvertown', 'Pontoon Dock',
                'London City Airport', 'King George V', 'Woolwich Arsenal'
            ]
        )
        self.assertEqual(
            dijkstras_algorithm(peak_station_dll, 'Lewisham', 'Woolwich Arsenal'), [
                'Lewisham', 'Elverson Road', 'Greenwich', 'Cutty Sark', 'Island Gardens',
                'Mudchute', 'Crossharbour', 'South Quay', 'Heron Quays', 'Canary Wharf',
                'North Greenwich', 'Canning Town', 'West Silvertown', 'Pontoon Dock',
                'London City Airport', 'King George V', 'Woolwich Arsenal'
            ]
        )

    def test_five(self):
        """
        Test five: Beckton to Upminster (DLR testing)
        """
        self.assertEqual(
            dijkstras_algorithm(off_peak_station_dll, 'Beckton', 'Upminster'), [
                'Beckton', 'Gallions Reach', 'Cyprus', 'Beckton Park', 'Royal Albert',
                'Prince Regent', 'Custom House', 'Royal Victoria', 'Canning Town',
                'West Ham', 'Plaistow', 'Upton Park', 'East Ham', 'Barking', 'Upney',
                'Becontree', 'Dagenham Heathway', 'Dagenham East', 'Elm Park',
                'Hornchurch', 'Upminster Bridge', 'Upminster'
            ]
        )
        self.assertEqual(
            dijkstras_algorithm(peak_station_dll, 'Beckton', 'Upminster'), [
                'Beckton', 'Gallions Reach', 'Cyprus', 'Beckton Park', 'Royal Albert',
                'Prince Regent', 'Custom House', 'Royal Victoria', 'Canning Town',
                'West Ham', 'Plaistow', 'Upton Park', 'East Ham', 'Barking', 'Upney',
                'Becontree', 'Dagenham Heathway', 'Dagenham East', 'Elm Park',
                'Hornchurch', 'Upminster Bridge', 'Upminster'
            ]
        )

    def test_six(self):
        """
        Test five: Holland Park to Mudchute (DLR testing)
        """
        self.assertEqual(
            dijkstras_algorithm(off_peak_station_dll, 'Holland Park', 'Mudchute'), [
                'Holland Park', 'Notting Hill Gate', 'Queensway', 'Lancaster Gate',
                'Marble Arch', 'Bond Street', 'Green Park', 'Westminster',
                'Waterloo', 'Southwark', 'London Bridge', 'Bermondsey',
                'Canada Water', 'Canary Wharf', 'Heron Quays', 'South Quay',
                'Crossharbour', 'Mudchute'
            ]
        )
        self.assertEqual(
            dijkstras_algorithm(peak_station_dll, 'Holland Park', 'Mudchute'), [
                'Holland Park', 'Notting Hill Gate', 'Bayswater', 'Paddington',
                'Edgware Road', 'Marylebone', 'Baker Street', "Regent's Park",
                'Oxford Circus', 'Piccadilly Circus', 'Charing Cross', 'Embankment',
                'Waterloo', 'Southwark', 'London Bridge', 'Bermondsey',
                'Canada Water', 'Canary Wharf', 'Heron Quays', 'South Quay',
                'Crossharbour', 'Mudchute'
            ]
        )


class TestLineChangingAlgorithm(unittest.TestCase):
    """
    Unittest class to test different outcomes of our line changing algorithm
    """

    def test_one(self):
        """
        Test one: Testing on peak and off lines and travel time from Edgware Road to Epping
        """
        # OFF PEAK TEST
        off_peak_route = dijkstras_algorithm(off_peak_station_dll, 'Edgware Road', 'Epping')
        lines, minutes = find_route_lines(off_peak_station_dll, off_peak_route)
        self.assertEqual(minutes, [3, 2, 2, 2, 4, 1, 2, 2, 3, 2, 4, 3, 2, 2, 2, 3, 2, 3, 2, 3, 3])
        self.assertEqual(lines, ['Circle', 'Metropolitan', 'Circle', 'Circle', 'Circle', 'Circle',
                                 'Circle', 'Circle', 'Central', 'Central', 'Central', 'Central', 'Central', 'Central',
                                 'Central', 'Central', 'Central', 'Central', 'Central', 'Central', 'Central', 'Central'
                                 ]
                         )
        # PEAK TIME TEST
        peak_route = dijkstras_algorithm(peak_station_dll, 'Edgware Road', 'Epping')
        lines, minutes = find_route_lines(peak_station_dll, peak_route)
        self.assertEqual(minutes, [0.5, 1.0, 1.0, 1.0, 1, 2, 1, 2, 2, 2, 3, 2, 4, 3, 2,
                                   2, 2, 3, 2, 3, 2, 3, 3
                                   ]
                         )
        self.assertEqual(lines, ['Bakerloo', 'Bakerloo', 'Bakerloo', 'Bakerloo', 'Central',
                                 'Central', 'Central', 'Central', 'Central', 'Central', 'Central', 'Central',
                                 'Central', 'Central', 'Central', 'Central', 'Central', 'Central', 'Central', 'Central',
                                 'Central', 'Central', 'Central', 'Central'
                                 ]
                         )

    def test_two(self):
        """
        Test two: Testing on peak and off lines and travel time from St. John's Wood to Westminster
        """
        # OFF PEAK TEST
        off_peak_route = dijkstras_algorithm(off_peak_station_dll, "St. John's Wood", 'Westminster')
        lines, minutes = find_route_lines(off_peak_station_dll, off_peak_route)
        self.assertEqual(minutes, [3, 2, 2, 2])
        self.assertEqual(lines, ['Jubilee', 'Jubilee', 'Jubilee', 'Jubilee', 'Jubilee'])
        # PEAK TIME TEST
        peak_route = dijkstras_algorithm(peak_station_dll, "St. John's Wood", 'Westminster')
        lines, minutes = find_route_lines(peak_station_dll, peak_route)
        self.assertEqual(minutes, [3, 1.0, 1.0, 1.0, 1.0, 0.5, 1])
        self.assertEqual(lines, ['Jubilee', 'Bakerloo', 'Bakerloo', 'Bakerloo', 'Bakerloo',
                                 'Bakerloo', 'District', 'District'
                                 ]
                         )

    def test_three(self):
        """
        Test one: Testing on peak and off lines and travel time from Monument to Paddington
        """
        # OFF PEAK TEST
        off_peak_route = dijkstras_algorithm(off_peak_station_dll, 'Monument', 'Paddington')
        lines, minutes = find_route_lines(off_peak_station_dll, off_peak_route)
        self.assertEqual(minutes, [1, 2, 2, 1, 2, 1, 2, 2, 2, 3, 2])
        self.assertEqual(lines, ['Circle', 'Circle', 'Circle', 'Circle', 'Circle', 'District',
                                 'Jubilee', 'Jubilee', 'Jubilee', 'Circle', 'Bakerloo', 'Bakerloo'
                                 ]
                         )
        # PEAK TIME TEST
        peak_route = dijkstras_algorithm(peak_station_dll, 'Monument', 'Paddington')
        lines, minutes = find_route_lines(peak_station_dll, peak_route)
        self.assertEqual(minutes, [1, 2, 2, 1, 2, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0])
        self.assertEqual(lines, ['Circle', 'Circle', 'Circle', 'Circle', 'Circle', 'Bakerloo',
                                 'Bakerloo', 'Bakerloo', 'Bakerloo', 'Bakerloo', 'Bakerloo', 'Bakerloo', 'Bakerloo',
                                 'Bakerloo'
                                 ]
                         )


class TestFindRouteLines(unittest.TestCase):
    """
    Unittest class to test different outcomes to find correct shortest route lines
    """

    def test_one(self):
        """
        Test three: Testing lines and indexes of line changes from Queensway to Oxford Circus
        """
        # OFF PEAK TEST
        off_peak_route = dijkstras_algorithm(off_peak_station_dll, 'Queensway', 'Oxford Circus')
        lines, minutes = find_route_lines(off_peak_station_dll, off_peak_route)
        new_lines, index_for_line_changes = change_line_info(lines)
        self.assertEqual(new_lines, ['Central', 'Central', 'Central', 'Central', 'Central'])
        self.assertEqual(index_for_line_changes, [])
        # PEAK TEST
        peak_route = dijkstras_algorithm(peak_station_dll, 'Queensway', 'Oxford Circus')
        lines, minutes = find_route_lines(peak_station_dll, peak_route)
        new_lines, index_for_line_changes = change_line_info(lines)
        self.assertEqual(new_lines, ['Central', 'Central', 'Central', 'Central', 'Central'])
        self.assertEqual(index_for_line_changes, [])

    def test_two(self):
        """
        Test two: Testing lines and indexes of line changes from Latimer Road to Neasden
        """
        # OFF PEAK TEST
        off_peak_route = dijkstras_algorithm(off_peak_station_dll, 'Latimer Road', 'Neasden')
        lines, minutes = find_route_lines(off_peak_station_dll, off_peak_route)
        new_lines, index_for_line_changes = change_line_info(lines)
        self.assertEqual(new_lines, [
            'Circle', 'Circle', 'Circle', 'Circle', 'Circle',
            'Bakerloo', 'Circle', 'Metropolitan', 'Jubilee',
            'Jubilee', 'Jubilee', 'Jubilee', 'Jubilee'
        ]
                         )
        self.assertEqual(index_for_line_changes, [4, 5, 6, 7])
        # PEAK TEST
        peak_route = dijkstras_algorithm(peak_station_dll, 'Latimer Road', 'Neasden')
        lines, minutes = find_route_lines(peak_station_dll, peak_route)
        new_lines, index_for_line_changes = change_line_info(lines)
        self.assertEqual(new_lines, [
            'Circle', 'Circle', 'Circle', 'Circle', 'Circle',
            'Bakerloo', 'Bakerloo', 'Bakerloo', 'Metropolitan',
            'Jubilee', 'Jubilee', 'Jubilee', 'Jubilee', 'Jubilee'
        ]
                         )
        self.assertEqual(index_for_line_changes, [4, 7, 8])

    def test_three(self):
        """
        Test three: Testing lines and indexes of line changes from Finchley Road to Aldgate
        """
        # OFF PEAK TEST
        off_peak_route = dijkstras_algorithm(off_peak_station_dll, 'Finchley Road', 'Aldgate')
        lines, minutes = find_route_lines(off_peak_station_dll, off_peak_route)
        new_lines, index_for_line_changes = change_line_info(lines)
        self.assertEqual(new_lines, [
            'Metropolitan', 'Metropolitan', 'Metropolitan',
            'Circle', 'Circle', 'Circle', 'Circle', 'Circle',
            'Circle', 'Metropolitan'
        ]
                         )
        self.assertEqual(index_for_line_changes, [2, 8])
        # PEAK TEST
        peak_route = dijkstras_algorithm(peak_station_dll, 'Finchley Road', 'Aldgate')
        lines, minutes = find_route_lines(peak_station_dll, peak_route)
        new_lines, index_for_line_changes = change_line_info(lines)
        self.assertEqual(new_lines, [
            'Metropolitan', 'Metropolitan', 'Bakerloo',
            'Bakerloo', 'Central', 'Central', 'Central',
            'Central', 'Central', 'Central', 'Metropolitan'
        ]
                         )
        self.assertEqual(index_for_line_changes, [1, 3, 9])


if __name__ == "__main__":
    unittest.main()
