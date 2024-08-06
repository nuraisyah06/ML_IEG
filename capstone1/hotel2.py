from os.path import exists
from tabulate import tabulate
from datetime import datetime
from prettytable import PrettyTable

def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if(value.strip() == ""):
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    
    return value
#---------------------------------------------------------------------------------------- read from booking.txt
def get_booking_by_id(booking_id, input_file_path):
    with open(input_file_path, 'r') as file:
        # Skip the header line
        headers = file.readline().strip()
        booking_headers = "BookingID|Customer|StartDay|EndDay"
        
        # Read the lines and find the matching booking
        for line in file:
            columns = line.strip().split('|')
            if columns[0] == booking_id:
                booking_info = [columns[0], columns[2], columns[4], columns[5]]
                return booking_headers, booking_info
        else:
            print(f"BookingID {booking_id} not found.")
            return booking_headers, None    
#---------------------------------------------------------------------------------------- read from service.txt
def get_service_by_id(service_id, input_file_path):
    with open(input_file_path, 'r') as file:
        # Skip the header line
        headers = file.readline().strip()
        service_headers = "ServiceID|ServiceName|Price|CommissionPerDay(%)"
        
        # Read the lines and find the matching service
        for line in file:
            columns = line.strip().split('|')
            if columns[0] == service_id:
                service_info = [columns[0], columns[1], columns[2], columns[3]]
                return service_headers, service_info
        else:
            print(f"ServiceID {service_id} not found.")
            return service_headers, None
#---------------------------------------------------------------------------------------- calculate duration
def calculate_duration(start_day, end_day):
    start_date = datetime.strptime(start_day, '%d/%m/%Y')
    end_date = datetime.strptime(end_day, '%d/%m/%Y')
    duration = (end_date - start_date).days
    return duration
#---------------------------------------------------------------------------------------- write information into bookservice.txt
def combine_booking_service(booking_id, service_id):
    # Check if BookingID already exists in bookservices.txt 
    with open('bookservices.txt', 'r') as check_file:
        for line in check_file:
            if line.startswith(booking_id):
                print(f"BookingID {booking_id} already exists in bookservices.txt. Process cancelled.")
                return
    
    # Get booking and service data
    booking_headers, booking_info = get_booking_by_id(booking_id, 'booking.txt')
    service_headers, service_info = get_service_by_id(service_id, 'services.txt')
    
    if not booking_info or not service_info:
        print("Unable to find the specified BookingID or ServiceID.")
        return
    
    # Call calculate duration
    duration = calculate_duration(booking_info[2], booking_info[3])
    
    # Calculate total commission
    price_per_day = float(service_info[2])
    commission_percent = float(service_info[3])
    total_price = price_per_day * duration
    total_commission = total_price * commission_percent
    
    # Combine headers
    combined_headers = f"BookingID|Customer|ServiceID|ServiceName|PricePerDay(RM)|Duration|TotalPrice(RM)|CommissionPercent(%)|TotalCommission(RM)"
    
    # Combine data
    combined_info = f"{booking_info[0]}|{booking_info[1]}|{service_info[0]}|{service_info[1]}|{price_per_day:.2f}|{duration}|{total_price:.2f}|{service_info[3]}|{total_commission:.2f}"
    
    with open('bookservices.txt', 'a') as output_file:
        # If the file is empty, write the headers
        if output_file.tell() == 0:
            output_file.write(combined_headers + '\n')
        
        # Write the combined information
        output_file.write(combined_info + '\n')
    
    print("Data have been successfully added into bookservices.txt!")
#---------------------------------------------------------------------------------------- print information in bookservices.txt to terminal


########################################## Choice 1 - BOOK SERVICES FOR CUSTOMERS #######################################
def print_combined_output(file_path):
    with open(file_path, 'r') as file:
        # Read the header and strip newline character
        headers = file.readline().strip().split('|')
        
        # Initialize a list to hold rows of data
        rows = []
        
        # Read each line and add it as a row of data
        for line in file:
            data = line.strip().split('|')
            rows.append(data)
        
        # Print the table using tabulate
        print(tabulate(rows, headers=headers, tablefmt='pretty'))
#---------------------------------------------------------------------------------------- print booking
def print_booking_details(file_path):
    # Initialize a PrettyTable object
    table = PrettyTable()

    # Define the columns
    table.field_names = ["BookingID", "Customer", "StartDay", "EndDay"]

    # Read the file and add rows to the table
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:  # Skip the header
        fields = line.strip().split('|')
        booking_id = fields[0]
        customer = fields[2]
        start_day = fields[4]
        end_day = fields[5]
        table.add_row([booking_id, customer, start_day, end_day])

    # Print the formatted table
    print(table)
#---------------------------------------------------------------------------------------- print services
def print_service_details(file_path):
    # Initialize a PrettyTable object
    table = PrettyTable()

    # Define the columns
    table.field_names = ["ServiceID", "ServiceName", "PricePerDay"]

    # Read the file and add rows to the table
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:  # Skip the header
        fields = line.strip().split('|')
        service_id = fields[0]
        service_name = fields[1]
        price_per_day = fields[2]
        table.add_row([service_id, service_name, price_per_day])

    # Print the formatted table
    print(table)
#---------------------------------------------------------------------------------------- to book a service 
def book_service(booking_id, booking_file_path='booking.txt', service_file_path='services.txt', service_booking_file='bookservices.txt'):
    if not booking_id:
        return "Invalid booking_id or service_id."
    
    # Read the booking file and find the corresponding booking
    with open(booking_file_path, 'r') as file:
        lines = file.readlines()

    # Find the booking with the given booking_id
    booking_found = False
    booking_line = None
    for line in lines[1:]:  # Skip the header
        fields = line.strip().split('|')
        if fields[0] == booking_id:
            booking_found = True
            booking_line = fields
            customer = fields[2]
            start_day = fields[4]
            end_day = fields[5]
            break

    if not booking_found:
        return f"Booking ID: {booking_id} not found."
    
    # Allow user to enter the service_id
    print(f"Booking ID: {booking_id} - Customer: {customer}")
    print_service_details(service_file_path)
    service_id = input("Enter Service ID: ")
    if not service_id:
        return "Invalid service_id."

    # Get service details from service file
    with open(service_file_path, 'r') as service_file:
        lines = service_file.readlines()

    service_found = False
    for line in lines:
        fields = line.strip().split('|')
        if fields[0] == service_id:
            service_name = fields[1]
            price_per_day = fields[2]
            commission_percent = fields[3]
            service_found = True
            break

    if not service_found:
        return f"Service ID: {service_id} not found."

    print(f"Booking ID: {booking_id} has been successfully booked for Service ID: {service_id} - Service Name: {service_name}")

    # Calculate total price and total commission
    duration = calculate_duration(start_day, end_day)
    total_price = float(price_per_day) * duration
    total_commission = total_price * float(commission_percent)

    # Append the new booking to bookservise.txt
    with open(service_booking_file, 'a') as sb_file:
        sb_file.write(f"{booking_id}|{customer}|{service_id}|{service_name}|{price_per_day}|{duration}|{total_price}|{commission_percent}|{total_commission}\n")
    
    return "Booking successful."

def edit_booking(service_booking_file='bookservise.txt'):
    # Prompt user for booking ID to edit
    booking_id = input("Enter the Booking ID to edit: ").strip()
    found = False
    updated_lines = []

    try:
        
        with open(service_booking_file, 'r') as sb_file:
            lines = sb_file.readlines()

        for line in lines:
            fields = line.strip().split('|')
            if fields[0] == booking_id:
                found = True
                current_customer = fields[1]
                current_service_id = fields[2]
                current_service_name = fields[3]
                current_price_per_day = fields[4]
                current_duration = fields[5]
                current_total_price = fields[6]
                current_commission_per_day = fields[7]
                current_total_commission = fields[8]

                print(f"\nCurrent Customer: {current_customer}")
                print(f"Current Service ID: {current_service_id}")
                print(f"Current Service Name: {current_service_name}")
                print(f"Current Price per Day (RM): {current_price_per_day}")
                print(f"Current Duration: {current_duration} days")
                print(f"Current Total Price (RM): {current_total_price}")
                print(f"Current Commission per Day (%): {current_commission_per_day}")
                print(f"Current Total Commission (RM): {current_total_commission}")

                # Prompt for new values
                new_customer = input("\nEnter new Customer Name (or press Enter to keep current): ")
                new_service_id = input("Enter new Service ID (or press Enter to keep current): ")
                new_service_name = input("Enter new Service Name (or press Enter to keep current): ")
                new_price_per_day = input("Enter new Price per Day (RM) (or press Enter to keep current): ")
                new_duration = input("Enter new Duration (days) (or press Enter to keep current): ")
                new_total_price = input("Enter new Total Price (RM) (or press Enter to keep current): ")
                new_commission_per_day = input("Enter new Commission per Day (%) (or press Enter to keep current): ")
                new_total_commission = input("Enter new Total Commission (RM) (or press Enter to keep current): ")

                # Use current values if new values are not provided
                new_customer = new_customer if new_customer else current_customer
                new_service_id = new_service_id if new_service_id else current_service_id
                new_service_name = new_service_name if new_service_name else current_service_name
                new_price_per_day = new_price_per_day if new_price_per_day else current_price_per_day
                new_duration = new_duration if new_duration else current_duration
                new_total_price = new_total_price if new_total_price else current_total_price
                new_commission_per_day = new_commission_per_day if new_commission_per_day else current_commission_per_day
                new_total_commission = new_total_commission if new_total_commission else current_total_commission

                # Construct updated line
                updated_line = f"{booking_id}|{new_customer}|{new_service_id}|{new_service_name}|{new_price_per_day}|{new_duration}|{new_total_price}|{new_commission_per_day}|{new_total_commission}\n"
                updated_lines.append(updated_line)

            else:
                updated_lines.append(line)

        if not found:
            return f"Booking ID: {booking_id} not found."

        # Write updated bookings back to bookservise.txt
        with open(service_booking_file, 'w') as sb_file:
            sb_file.writelines(updated_lines)

        return "Booking updated successfully."

    except FileNotFoundError:
        return "The file 'bookservise.txt' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"
  

def delete_booking():
    # Prompt user for booking ID to delete
    booking_id = input("Enter the Booking ID to delete: ")
    found = False
    updated_lines = []

    try:
        with open('bookservices.txt', 'r') as sb_file:
            lines = sb_file.readlines()
            for line in lines:
                fields = line.strip().split('|')
                
                if fields[0] == booking_id:
                    found = True
                    print(f"\nBooking ID: {fields[0]}")
                    print(f"Customer: {fields[1]}")
                    print(f"Service ID: {fields[2]}")
                    print(f"Service Name: {fields[3]}")
                    print(f"Price per Day (RM): {fields[4]}")
                    print(f"Duration: {fields[5]} days")
                    print(f"Total Price (RM): {fields[6]}")
                    print(f"Commission per Day (%): {fields[7]}")
                    print(f"Total Commission (RM): {fields[8]}")

                    # Prompt for confirmation
                    confirm = input("\nAre you sure you want to delete this booking? (yes/no): ").strip().lower()
                    if confirm == 'yes':
                        print(f"Deleting Booking ID: {booking_id}")
                        print(f"\n\033[32mBooking ID {booking_id} deleted successfully.\033[0m")
                    else:
                        print("\n\033[31mBooking deletion canceled.\033[0m")
                        updated_lines.append(line)  # Add the line back to updated_lines (not deleting)

                else:
                    updated_lines.append(line)

        if not found:
            return f"Booking ID: {booking_id} not found."

        # Write updated bookings back to bookservise.txt
        with open('bookservices.txt', 'w') as sb_file:
            sb_file.writelines(updated_lines)

        return "Booking deleted successfully."

    except FileNotFoundError:
        return "The file 'bookservise.txt' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

############################################### Choice 2 - MANAGE SERVICES ##############################################
#---------------------------------------------------------------------------------------- print service 
def print_services(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
       
    # Create a PrettyTable instance
    table = PrettyTable()
    
    # Set table headers
    headers = lines[0].strip().split('|')
    table.field_names = [header.strip() for header in headers]
    
    # Add rows to the table
    for line in lines[1:]:
        service = line.strip().split('|')
        table.add_row([data.strip() for data in service])
    
    # Print the table
    print(table)
        
#---------------------------------------------------------------------------------------- add service 
def add_service():
    service_id = input("\nEnter new Service ID (H - Hotel & T - Tour Guide Agency): ")
    service_name = input("Enter new Service Name: ")
    price_per_day = input("Enter Price per Day for the Service: ")
    commission_percent = input("Enter Commision Percentage(%) for the Service: ")
    agent_name = input("Enter Agent Name for the Service: ")
    
    with open('services.txt', 'a') as file:
        file.write(f"{service_id}|{service_name}|{price_per_day}|{commission_percent}|{agent_name}\n")
    
    print(f"\n\033[32mService {service_name} added successfully.\033[0m")
#---------------------------------------------------------------------------------------- edit service 
def edit_service():
    service_id = input("Enter the Service ID to edit: ")
    found = False
    services = []

    try:
        with open('services.txt', 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if parts[0] == service_id:
                    found = True
                    current_service_name = parts[1]
                    current_price_per_day = parts[2]
                    current_commission_percent = parts[3]
                    current_agent_name = parts[4]
                    
                    print(f"\nCurrent Service Name: {current_service_name}")
                    print(f"Current Price per Day: {current_price_per_day}")
                    print(f"Current Commission Percentage: {current_commission_percent}")
                    print(f"Current Agent Name: {current_agent_name}")
                    
                    new_service_name = input("\nEnter new Service Name (or press Enter to keep current): ")
                    new_price_per_day = input("Enter new Price per Day (or press Enter to keep current): ")
                    new_commission_percent = input("Enter new Commission Percentage (or press Enter to keep current): ")
                    new_agent_name = input("Enter new Agent Name (or press Enter to keep current): ")
                    
                    new_service_name = new_service_name if new_service_name else current_service_name
                    new_price_per_day = new_price_per_day if new_price_per_day else current_price_per_day
                    new_commission_percent = new_commission_percent if new_commission_percent else current_commission_percent
                    new_agent_name = new_agent_name if new_agent_name else current_agent_name
                    
                    services.append(f"{service_id}|{new_service_name}|{new_price_per_day}|{new_commission_percent}|{new_agent_name}\n")
                else:
                    services.append(line)
        
        if not found:
            print(f"\nService ID {service_id} not found.")
        else:
            with open('services.txt', 'w') as file:
                file.writelines(services)
            print(f"\n\033[32mService ID {service_id} updated successfully.\033[0m")
    
    except FileNotFoundError:
        print("The file 'services.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
#---------------------------------------------------------------------------------------- delete service 
def delete_service():
    service_id = input("Enter the Service ID to delete: ")
    found = False
    services = []

    try:
        with open('services.txt', 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                
                if parts[0] == service_id:
                    found = True
                    print(f"\nService ID: {parts[0]}")
                    print(f"Service Name: {parts[1]}")
                    print(f"Price per Day: {parts[2]}")
                    print(f"Commission Percentage: {parts[3]}")
                    print(f"Agent Name: {parts[4]}")
                    confirm = input("\nAre you sure you want to delete this service? (yes/no): ").lower()
                    if confirm == 'yes':
                        print(f"Deleting Service: {parts[1]}")
                        print(f"\n\033[32mService ID {service_id} deleted successfully.\033[0m")
                    else:
                        print("\n\033[31mService deletion cancelled.\033[0m")
                        services.append(line)
                else:
                    services.append(line)

        if not found:
            print(f"Service ID {service_id} not found.")
        else:
            with open('services.txt', 'w') as file:
                file.writelines(services)
    
    except FileNotFoundError:
        print("The file 'services.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
#================================================  SERVICES MENU ================================================
def ManageServices():
    print()
    print("\t\t     \033[1m\033[44m\033[37m AVAILABLE SERVICES OF HOTEL & TOUR GUIDE AGENCY \033[0m\t\t")

    print_services('services.txt')
    choice = -1
    while choice != 0:
        print() 
        print()
        print("\t\t****************************************")
        print("\t\t:                                      :")
        print("\t\t:    🔙 0 - Return to Main Menu        :")
        print("\t\t:    ➕ 1 - Add Service                :")
        print("\t\t:    ✏️  2 - Edit Service               :")
        print("\t\t:    ❌ 3 - Delete Service             :")
        print("\t\t:    📋 4 - Available Service          :")
        print("\t\t:                                      :")
        print("\t\t****************************************")
        print()
        
        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be an integer")
        
        if choice == 0:
            print("\nReturning to Main Menu ...\n")
        elif choice == 1:
            add_service()
            print()
        elif choice == 2:
            print()
            edit_service()
        elif choice == 3:
            print()
            delete_service()
        elif choice == 4:
            print()
            print_services('services.txt')
        else:
            print("Invalid choice. Please try again.")


############################################ Choice 3 - REPORT ON THE COMMISSION ######################################
def read_bookings():
    bookings = []
    file_path = 'bookservices.txt'
    with open(file_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            data = line.strip().split('|')
            booking = dict(zip(headers, data))
            bookings.append(booking)
    return bookings
# ---------------------------------------------------------------------------------- Total Commission Received
def calculate_total_commission(bookings):
    total_commission = sum(float(booking['TotalCommission(RM)']) for booking in bookings)
    return total_commission
#----------------------------------------------------------------------------------- Top 3 highest commission
def find_top_commissions(bookings, top_n=3):
    sorted_bookings = sorted(bookings, key=lambda booking: float(booking['TotalCommission(RM)']), reverse=True)
    return sorted_bookings[:top_n]
def print_top_commissions(top_commissions):
    table = PrettyTable()
    table.field_names = ["Customer Name", "Service Name", "Total Commission (RM)"]
    table.align["Customer Name"] = "l"
    table.align["Service Name"] = "l"
    table.align["Total Commission (RM)"] = "r"

    for booking in top_commissions:
        table.add_row([booking['Customer'], booking['ServiceName'], f"{booking['TotalCommission(RM)']}"])

    print("\n\t\tTop 3 Highest Commission Bookings:")
    print(table)
#----------------------------------------------------------------------------------- ServiceName and it's total commission
def calculate_service_commissions(bookings):
    service_commissions = {}
    for booking in bookings:
        service_name = booking['ServiceName']
        commission = float(booking['TotalCommission(RM)'])
        if service_name in service_commissions:
            service_commissions[service_name] += commission
        else:
            service_commissions[service_name] = commission
    return service_commissions
#----------------------------------------------------------------------------------- Print and sort commission from services
def print_service_commissions(service_commissions):
    
    # Sort service_commissions dictionary by Total Commission (RM) in descending order
    sorted_commissions = sorted(service_commissions.items(), key=lambda x: x[1], reverse=True)

    table = PrettyTable()
    table.field_names = ["Service Name", "Total Commission (RM)"]
    table.align["Service Name"] = "l"
    table.align["Total Commission (RM)"] = "r"

    for service_name, total_commission in service_commissions.items():
        table.add_row([service_name, f"{total_commission:.2f}"])

    print("\nTotal Commission Received by Each Service: ")
    print(table)
#================================================= REPORT MENU ==================================================
def ReportMenu(bookings):
    choice = -1
    
    while choice != 0:
        print() 
        print()
        print("\t\t*********************************************")
        print("\t\t:                                           :")
        print("\t\t:    🔙 0 - Return to Main Menu             :")
        print("\t\t:    💰 1 - Total Commission Received       :")
        print("\t\t:    🏆 2 - Top 3 Highest Commission        :")
        print("\t\t:    📄 3 - List of Service and Commission  :")
        print("\t\t:                                           :")
        print("\t\t*********************************************")
        print()
        
        choice = keyboardInput(int, "Choice [0, 1, 2, 3]: ", "Choice must be an integer\n")
        
        if choice == 0:
            print("\nReturning to Main Menu ...\n")
        elif choice == 1:
            total_commission = calculate_total_commission(bookings)
            print()
            print("\t      +-------------------------------+---------------+")
            print(f"\t      |   Total Commission Received   |   \033[32mRM {total_commission:.2f}\033[0m   |")
            print("\t      +-------------------------------+---------------+")
        elif choice == 2:
            top_commissions = find_top_commissions(bookings)
            print_top_commissions(top_commissions)
        elif choice == 3:
            service_commissions = calculate_service_commissions(bookings)
            print_service_commissions(service_commissions)
        else:
            print("Invalid choice. Please try again.")
#--------------------------------------------------------------------------------------------------------------------------------
def BookedServices(file_path):
    table = PrettyTable()

    # Define the columns
    table.field_names = ["BookingID","CustomerName","ServiceID", "ServiceName", "PricePerDay"]

    # Read the file and add rows to the table
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:  # Skip the header
        fields = line.strip().split('|')
        booking_id = fields[0]
        customer = fields[1]
        service_id = fields[2]
        service_name = fields[3]
        total_price = fields[6]
        table.add_row([booking_id, customer, service_id, service_name, total_price])

    # Print the formatted table
    print(table)


################################################### MAIN MENU ####################################################
def MainMenu():
    #bold = "\033[1m"  # ANSI escape sequence for bold text
    #reset = "\033[0m"  # ANSI escape sequence to reset text attributes
    print()
    print("\n\033[1m\033[44m\033[37m---------------------<< Welcome To Hotel and Tour Booking System >>--------------------\033[0m\n")

    choice = -1
    while choice != 0:
        print("\t\t\t******************************************")
        print("\t\t\t:               \033[1m\033[46m MAIN MENU \033[0m              :")
        print("\t\t\t:                                        :")
        print("\t\t\t:     ❌ 0 - Exit                        :")
        print("\t\t\t:     📅 1 - Book a service              :")
        print("\t\t\t:     📅 2 - Edit Booked Service         :")
        print("\t\t\t:     📅 3 - Delete Booked Service       :")
        print("\t\t\t:     🛠️  4 - Manage Services             :")
        print("\t\t\t:     📋 5 - Current Booked Services     :")
        print("\t\t\t:     🖨️  6 - Print Report                :")
        print("\t\t\t:                                        :")
        print("\t\t\t******************************************")
        print()
        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be integer")
        if (choice == 0):
            print("Thank You for using our system")
        elif (choice == 1):
            print_booking_details('booking.txt')
            booking_id = input("Choose a booking ID to add Hotel or Tour booking: ")
            result = book_service(booking_id)
            print(result)
            #combine_booking_service(booking_id, service_id)
        elif (choice == 2):
            edit_booking()
        elif (choice == 3):
            delete_booking()
        elif (choice == 4):
            ManageServices()
        elif (choice == 5):
            BookedServices('bookservices.txt')
        elif (choice == 6):
            bookings = read_bookings()
            ReportMenu(bookings)
            
MainMenu()