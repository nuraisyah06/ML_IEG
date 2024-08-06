def create_services_file(filename='services.txt'):
    data = [
        {'ServiceID': 'H001', 'ServiceName': 'Hotel California', 'CommissionPerDay': 50, 'AgentName': 'Alice Johnson'},
        {'ServiceID': 'H002', 'ServiceName': 'The Grand Budapest', 'CommissionPerDay': 60, 'AgentName': 'Bob Smith'},
        {'ServiceID': 'H003', 'ServiceName': 'Shangri-La', 'CommissionPerDay': 70, 'AgentName': 'Charlie Brown'},
        {'ServiceID': 'T001', 'ServiceName': 'City Tour', 'CommissionPerDay': 30, 'AgentName': 'Daisy Ridley'},
        {'ServiceID': 'T002', 'ServiceName': 'Mountain Adventure', 'CommissionPerDay': 40, 'AgentName': 'Ethan Hunt'},
        {'ServiceID': 'T003', 'ServiceName': 'Beach Relaxation', 'CommissionPerDay': 50, 'AgentName': 'Fiona Apple'},
        {'ServiceID': 'H004', 'ServiceName': 'Ocean View Inn', 'CommissionPerDay': 55, 'AgentName': 'George Lucas'},
        {'ServiceID': 'H005', 'ServiceName': 'Desert Oasis', 'CommissionPerDay': 65, 'AgentName': 'Harrison Ford'},
        {'ServiceID': 'T004', 'ServiceName': 'Historical Walk', 'CommissionPerDay': 35, 'AgentName': 'Ivy League'},
        {'ServiceID': 'T005', 'ServiceName': 'Wildlife Safari', 'CommissionPerDay': 45, 'AgentName': 'Jack Sparrow'},
    ]

    with open(filename, 'w') as file:
        file.write('ServiceID|ServiceName|CommissionPerDay|AgentName\n')
        for entry in data:
            line = f"{entry['ServiceID']}|{entry['ServiceName']}|{entry['CommissionPerDay']}|{entry['AgentName']}\n"
            file.write(line)

    print(f"{filename} has been created with dummy data using | separator and updated format.")

# Function to read and print the content of services.txt
def read_and_print_services_file(filename='services.txt'):
    with open(filename, 'r') as file:
        lines = file.readlines()

    headers = lines[0].strip().split('|')
    data = [line.strip().split('|') for line in lines[1:]]
    
    # Print header
    header_line = "|".join(f"{header:<15}" for header in headers)
    print(header_line)
    print("-" * len(header_line))

    # Print data rows
    for row in data:
        print("|".join(f"{item:<15}" for item in row))

# Create and print the services.txt file
create_services_file()
print("Contents of services.txt:")
read_and_print_services_file()
