import os
import email
import re
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import sqlite3

# Create a GUI window for selecting a directory
root = tk.Tk()
root.withdraw()  # Hide the main window

# Prompt the user to select a directory
eml_directory = filedialog.askdirectory(title="Select the directory containing .eml files")

if not eml_directory:
    print("No directory selected. Exiting...")
    exit()

def extract_sales_data_from_email(email_path):
    with open(email_path, 'rb') as eml_file:
        msg = email.message_from_binary_file(eml_file)
        email_body = ""

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    email_body = part.get_payload(decode=True).decode('utf-8')
                    break
        else:
            email_body = msg.get_payload(decode=True).decode('utf-8')

        # Extract data using regular expressions
        reservation_id = re.search(r'Reservation ID: (.+)', email_body)
        guests_name = re.search(r"Guest's Name: (.+)", email_body)
        arrival_date = re.search(r'Arrival Date: (.+)', email_body)
        departure_date = re.search(r'Departure Date: (.+)', email_body)
        room_type = re.search(r'Room Type: (.+)', email_body)
        num_guests = re.search(r'Number of Guests: (.+)', email_body)
        num_rooms = re.search(r'Number of Rooms: (.+)', email_body)
        total_cost = re.search(r'Total Cost: (.+)', email_body)
        room_rate = re.search(r'Room Rate: (.+)', email_body)
        taxes_fees = re.search(r'Taxes and Fees: (.+)', email_body)
        additional_services = re.search(r'Additional Services: (.+)', email_body)

        data = {
            "Reservation ID": reservation_id.group(1) if reservation_id else None,
            "Guest's Name": guests_name.group(1) if guests_name else None,
            "Arrival Date": arrival_date.group(1) if arrival_date else None,
            "Departure Date": departure_date.group(1) if departure_date else None,
            "Room Type": room_type.group(1) if room_type else None,
            "Number of Guests": num_guests.group(1) if num_guests else None,
            "Number of Rooms": num_rooms.group(1) if num_rooms else None,
            "Total Cost": total_cost.group(1) if total_cost else None,
            "Room Rate": room_rate.group(1) if room_rate else None,
            "Taxes and Fees": taxes_fees.group(1) if taxes_fees else None,
            "Additional Services": additional_services.group(1) if additional_services else None
        }

        return data

data_list = []

for eml_file_name in os.listdir(eml_directory):
    eml_file_path = os.path.join(eml_directory, eml_file_name)
    data = extract_sales_data_from_email(eml_file_path)
    data_list.append(data)


db_connection = sqlite3.connect('sales_database.db')
db_cursor = db_connection.cursor()

# Create a table to store sales data
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales_data (
        reservation_id TEXT PRIMARY KEY,
        guests_name TEXT,
        arrival_date TEXT,
        departure_date TEXT,
        room_type TEXT,
        num_guests TEXT,
        num_rooms TEXT,
        total_cost TEXT,
        room_rate TEXT,
        taxes_fees TEXT,
        additional_services TEXT
    )
''')

db_connection.commit()

for eml_file_name in os.listdir(eml_directory):
    eml_file_path = os.path.join(eml_directory, eml_file_name)
    data = extract_sales_data_from_email(eml_file_path)

    # Insert data into the database (replace if reservation_id already exists)
    db_cursor.execute('''
        INSERT OR REPLACE INTO sales_data (
            reservation_id, guests_name, arrival_date, departure_date,
            room_type, num_guests, num_rooms, total_cost,
            room_rate, taxes_fees, additional_services
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data["Reservation ID"], data["Guest's Name"], data["Arrival Date"],
        data["Departure Date"], data["Room Type"], data["Number of Guests"],
        data["Number of Rooms"], data["Total Cost"], data["Room Rate"],
        data["Taxes and Fees"], data["Additional Services"]
    ))

    db_connection.commit()

db_connection.close()

print(f"Data exported to sales_database.db")