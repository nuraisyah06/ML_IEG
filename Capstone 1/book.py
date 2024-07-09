import random
import faker            #pip install faker
from datetime import datetime, timedelta

# Initialize Faker
fake = faker.Faker()

# Number of customers to generate
num_bookings = 15

# Function to generate customer data
def generate_customers(num_bookings):
    bookings = []
    for _ in range(num_bookings):
        custname = fake.name()
        custphone = fake.phone_number()
        brand = fake.company()
        plate_number = fake.license_plate()
        seats = random.choice([4, 5, 7, 9])
        rental_rate = round(random.uniform(50, 200), 2)
        drivername = fake.name()
        driverphone = fake.phone_number()
        
        start_date = fake.date_between(start_date='-30d', end_date='today')
        end_date = start_date + timedelta(days=random.randint(1, 14))
        rental_fee = rental_rate * (end_date - start_date).days

        booking = {
            "Customer": custname,
            "Customer Phone Number": custphone,
            "Brand": brand,
            "Plate Number": plate_number,
            "Seats": seats,
            "Rental Rate": rental_rate,
            "Driver": drivername,
            "Driver Phone Number": driverphone,
            "Start Date": start_date,
            "End Date": end_date,
            "Rental Fee (RM)": rental_fee
        }
        
        bookings.append(booking)
    
    return bookings

# Generate customer data
bookings = generate_customers(num_bookings)

# Print customer data
for booking in bookings:
    print(booking)
