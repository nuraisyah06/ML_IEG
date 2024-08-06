# Function to create and write the dummy data to bookservices.txt
def create_bookservices_file(filename='bookservices.txt'):
    data = [
        {'BookingID': '001', 'CategoryID': 'H001', 'ServiceName': 'Hotel California', 'CommissionPerDay': 50, 'TotalCommission': 200},
        {'BookingID': '002', 'CategoryID': 'H002', 'ServiceName': 'The Grand Budapest', 'CommissionPerDay': 60, 'TotalCommission': 240},
        {'BookingID': '003', 'CategoryID': 'H003', 'ServiceName': 'Shangri-La', 'CommissionPerDay': 70, 'TotalCommission': 280},
        {'BookingID': '004', 'CategoryID': 'T001', 'ServiceName': 'City Tour', 'CommissionPerDay': 30, 'TotalCommission': 120},
        {'BookingID': '005', 'CategoryID': 'T002', 'ServiceName': 'Mountain Adventure', 'CommissionPerDay': 40, 'TotalCommission': 160},
        {'BookingID': '006', 'CategoryID': 'T003', 'ServiceName': 'Beach Relaxation', 'CommissionPerDay': 50, 'TotalCommission': 200},
        {'BookingID': '007', 'CategoryID': 'H004', 'ServiceName': 'Ocean View Inn', 'CommissionPerDay': 55, 'TotalCommission': 220},
        {'BookingID': '008', 'CategoryID': 'H005', 'ServiceName': 'Desert Oasis', 'CommissionPerDay': 65, 'TotalCommission': 260},
        {'BookingID': '009', 'CategoryID': 'T004', 'ServiceName': 'Historical Walk', 'CommissionPerDay': 35, 'TotalCommission': 140},
        {'BookingID': '010', 'CategoryID': 'T005', 'ServiceName': 'Wildlife Safari', 'CommissionPerDay': 45, 'TotalCommission': 180},
    ]

    with open(filename, 'w') as file:
        file.write('BookingID|CustomerID|CategoryID|ServiceName|CommissionPerDay|TotalCommission\n')
        for entry in data:
            line = f"{entry['BookingID']}|{entry['CategoryID']}|{entry['ServiceName']}|{entry['CommissionPerDay']}|{entry['TotalCommission']}\n"
            file.write(line)

    print(f"{filename} has been created with dummy data using | separator and updated CategoryID format.")

# Function to read and print the content of bookservices.txt
def read_and_print_bookservices_file(filename='bookservices.txt'):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)

# Create the file
create_bookservices_file()

# Read and print the file content
read_and_print_bookservices_file()
