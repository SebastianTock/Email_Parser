import random
from faker import Faker
import os

# Initialize Faker with a specific seed for consistent random data
fake = Faker()
random.seed(42)  # Set a seed for reproducible random data

# Template for the email
email_template = """
Dear {guest_name},

Thank you for choosing Fake Hotel for your upcoming stay. We are pleased to confirm your reservation details:

Reservation ID: ABC{reservation_id}
Guest's Name: {guest_name}
Arrival Date: {arrival_date}
Departure Date: {departure_date}
Room Type: {room_type}
Number of Guests: {num_guests}
Number of Rooms: {num_rooms}

Reservation Summary:
Total Cost: ${total_cost:.2f}
Room Rate: ${room_rate:.2f}
Taxes and Fees: ${taxes_fees:.2f}
Additional Services: ${additional_services:.2f}

Payment Method:
Credit Card: **** **** **** {credit_card_last_digits}
Expiry Date: {expiry_date}

Hotel Information:
Fake Hotel
Fake Rd
Phone: +1 (123) 456-7890
Email: Fake_Hotel@outlook.com
Website: www.FakeHotel.com

Check-in Instructions:
Check-in time is after 3:00 PM. Please present your confirmation email and a valid photo ID upon arrival.

Cancellation Policy:
You can cancel your reservation up to 48 hours before your arrival date for a full refund. Cancellations made within 48 hours will incur a one-night charge.

Additional Services:
Airport Transfer: {additional_services_date} - ${additional_services:.2f}

Special Requests:
No-smoking room preference noted.

Terms and Conditions:
Please review our terms and conditions on our website at www.hotelname.com/terms.

For any inquiries or assistance, feel free to contact our reservations team at reservations@hotelname.com or call us at +1 (123) 456-7890.

We look forward to welcoming you to [Hotel Name] and providing you with an exceptional experience.

Best regards,
Thomas Riddle
Reservation Manager
Fake Hotel
"""

# Directory to save the generated .eml files
output_directory = 'generated_emails'
os.makedirs(output_directory, exist_ok=True)

# Generate random data

# Generate and save 5 random .eml files
for i in range(5):
    data = {
        "guest_name": fake.name(),
        "reservation_id": random.randint(100, 999),
        "arrival_date": fake.date_this_year().strftime('%B %d, %Y'),
        "departure_date": fake.date_this_year().strftime('%B %d, %Y'),
        "additional_services_date": fake.date_this_year().strftime('%B %d, %Y'),
        "room_type": random.choice(['Standard Room', 'Deluxe Room', 'Suite']),
        "num_guests": f"{random.randint(1, 4)} Adults",
        "num_rooms": random.randint(1, 3),
        "total_cost": random.uniform(500, 1000),
        "room_rate": random.uniform(400, 800),
        "taxes_fees": random.uniform(50, 100),
        "additional_services": random.uniform(50, 100),
        "credit_card_last_digits": random.randint(1000, 9999),
        "expiry_date": f"{random.randint(1, 12)}/{random.randint(23, 30)}",
    }
    # Generate the email content by filling in the template with random data
    email_content = email_template.format(**data)

    # Save the email content to a .eml file
    eml_file_path = os.path.join(output_directory, f'email_{i + 1}.eml')
    with open(eml_file_path, 'w') as eml_file:
        eml_file.write(email_content)

    print(f'Generated {eml_file_path}')

print('Email generation completed.')