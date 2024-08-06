import datetime

# Read booking.txt
with open('booking.txt', 'r') as booking_file:
    booking_lines = booking_file.readlines()

# Read services.txt
with open('services.txt', 'r') as services_file:
    services_lines = services_file.readlines()

# Parse booking.txt data
booking_data = []
for line in booking_lines[1:]:  # Skip header
    parts = line.strip().split(' | ')
    booking_id = parts[0]
    car = parts[1]
    customer = parts[2]
    driver = parts[3]
    start_day = datetime.datetime.strptime(parts[4], "%d/%m/%Y")
    end_day = datetime.datetime.strptime(parts[5], "%d/%m/%Y")
    duration = (end_day - start_day).days + 1  # Including both start and end day
    booking_data.append((booking_id, customer, duration))

print("BookingData",booking_data)

print("Parsed booking data:")
for booking in booking_data:
    print(booking)

# Parse services.txt data
services_data = {}
for line in services_lines[1:]:  # Skip header
    parts = line.strip().split(' | ')
    service_id = parts[0]
    service_name = parts[1]
    commission_per_day = float(parts[2])
    services_data[service_id] = (service_name, commission_per_day)

print("\nParsed services data:")
for service_id, service_info in services_data.items():
    print(service_id, service_info)

# Assuming that we have a mapping of bookings to services
booking_to_service = {
    'ID001': 'H001',
    'ID002': 'H002',
    'ID003': 'H003',
    'ID004': 'H004',
    'ID005': 'H005',
    'ID006': 'T001',
    'ID007': 'T002',
    'ID008': 'T003',
    'ID009': 'T004',
    'ID010': 'T005',
}

# Combine data and calculate total commission
bookservices_data = []
for booking in booking_data:
    booking_id, customer, duration = booking
    service_id = booking_to_service.get(booking_id)
    if service_id and service_id in services_data:
        service_name, commission_per_day = services_data[service_id]
        total_commission = duration * commission_per_day
        bookservices_data.append((booking_id, customer, duration, service_id, service_name, commission_per_day, total_commission))

print("\nCombined data for bookservices.txt:")
for data in bookservices_data:
    print(data)
    
print(bookservices_data)

# Write to bookservices.txt
with open('bookservices.txt', 'w') as bookservices_file:
    bookservices_file.write("BookingID | Customer | Duration | ServiceID | ServiceName | CommissionPerDay | TotalCommission\n")
    for data in bookservices_data:
        line = " | ".join(map(str, data))
        bookservices_file.write(line + "\n")

print("\nbookservices.txt has been created successfully.")
