
# Function to read and print the content of bookservices.txt
def read_and_print_bookservices_file(filename='bookservices1.txt'):
    with open(filename, 'r') as file:
        lines = file.readlines()

    headers = lines[0].strip().split('|')
    data = [line.strip().split('|') for line in lines[1:]]
    
    # Print header
    header_line = "|".join(f"{header:<13}" for header in headers)
    print(header_line)
    print("-" * len(header_line))

    # Print data rows
    for row in data:
        print("|".join(f"{item:<13}" for item in row))

# Function to read booking.txt and return its content
def read_booking_file(filename='booking.txt'):
    with open(filename, 'r') as file:
        lines = file.readlines()

    headers = lines[0].strip().split('|')
    data = [line.strip().split('|') for line in lines[1:]]
    
    return headers, data

# Function to match and print combined table
def match_and_print_combined_table():
    # Read booking.txt file
    booking_headers, booking_data = read_booking_file()

    # Read bookservices.txt file
    with open('bookservices1.txt', 'r') as file:
        lines = file.readlines()

    service_headers = lines[0].strip().split('|')
    service_data = [line.strip().split('|') for line in lines[1:]]
    
    # Create a dictionary of services indexed by BookingID
    service_dict = {service[0]: service for service in service_data}

    # Create a combined list of dictionaries based on BookingID
    combined_data = []
    for booking in booking_data:
        booking_id = booking[0]
        if booking_id in service_dict:
            service = service_dict[booking_id]
            combined_entry = service + booking[1:]  # Combine service and booking data
            combined_data.append(combined_entry)


    # Combined headers
    combined_headers = service_headers + booking_headers[1:]

    # Print combined table
    header_line = "|".join(f"{header:<13}" for header in combined_headers)
    print(header_line)
    print("-" * len(header_line))

    for row in combined_data:
        print("|".join(f"{item:<13}" for item in row))

# Print the content of bookservices.txt
print("Contents of bookservices.txt:")
read_and_print_bookservices_file()

# Print the combined table
print("\nCombined table:")
match_and_print_combined_table()
