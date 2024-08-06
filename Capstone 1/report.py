# Define the list of bookings
bookings = [
    {'BookingID': '001', 'Hotel': 'Hotel California', 'TourAgency': 'BestTours', 'Commission': 100.0},
    {'BookingID': '002', 'Hotel': 'The Grand Budapest', 'TourAgency': 'TravelExperts', 'Commission': 150.0},
    {'BookingID': '003', 'Hotel': 'Shangri-La', 'TourAgency': 'HolidayPlanners', 'Commission': 200.0},
]

# Function to print and write the report
def print_and_write_report(bookings, filename='Report.txt'):
    header = 'BookingID\tHotel\t\t\tTourAgency\t\tCommission\n'
    separator = '------------------------------------------------------------\n'

    # Print the header and separator to the terminal
    print(header, end='')
    print(separator, end='')

    # Open the file in write mode
    with open(filename, 'w') as file:
        # Write the header and separator to the file
        file.write(header)
        file.write(separator)

        # Process each booking
        for booking in bookings:
            line = f"{booking['BookingID']}\t\t{booking['Hotel']}\t{booking['TourAgency']}\t\t{booking['Commission']}\n"
            
            # Print the line to the terminal
            print(line, end='')

            # Write the line to the file
            file.write(line)

# Call the function
print_and_write_report(bookings)
