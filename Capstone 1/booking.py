import random
import faker

# Initialize Faker
fake = faker.Faker()

# Number of customers to generate
num_bookings = 15
'''
Customer| Customer Phone Number | Brand| Plate Number | Seats | Rental Rate | Driver              
| Driver Phone Number | Start Date | End Date | Rental Fee (RM)
'''
# Function to generate customer data
def generate_customers(num_bookings):
    bookings = []
    for _ in range(num_bookings):
        custname = fake.name()
        custemail = fake.email()
        custphone = fake.phone_number()
        drivername = fake.name()
        driverpnone = fake.phone_number()
        hotel_index = random.randint(0, 9)
        chose_tour_guide = random.choice([True, False])
        tour_guide_index = random.randint(0, 9) if chose_tour_guide else None
        
        booking = {
            "name": custname,
            "email": custemail,
            "phone": custphone,
            "hotel_index": hotel_index,
            "chose_tour_guide": chose_tour_guide,
            "tour_guide_index": tour_guide_index
        }
        
        bookings.append(booking)
    
    return bookings

# Generate customer data
bookings = generate_customers(num_bookings)

# Print customer data
for booking in bookings:
    print(booking)
