# Email Parser

An email parser is a program that is designed to extract specific information or data from email messages. It automates the process of extracting relevant content from emails, such as text, attachments, and metadata, and transforms it into structured data that can be easily processed and used in various applications or systems.

This project is an replication of what I did during my internship, emails are randomly generated using an python script. Do note that this was created for a very specific use case.

## Outlook to Excel

Creating an email parser that collects sales data from Outlook and stores it into Excel using Python and SQL involves several steps. Here's a outline of the process:

1.  **Setting Up Environment:**
    
    -   Install required libraries using `pip install`.

2.  **Accessing Outlook Emails:**
    
    -   Copy and paste the emails (.eml files) into a file
    -   Retrieve email content.
   
3.  **Parsing Sales Data:**
    
    -   Implement a parser to extract sales-related information from the email content using regular expressions or other techniques.
    
4.  **Storing Data in SQL:**
    
    -   Set up a SQL database (SQLite, MySQL, etc.).
    -   Use a Python SQL library (e.g., `sqlite3` for SQLite) to connect to the database.

5.  **Storing Data in Excel:**
    
    -   Use the `openpyxl` library to create or open an Excel workbook.
    -   Write the extracted sales data to a specific sheet in the workbook.

6.  **Putting It All Together:**
    
    -   Loop through the retrieved emails.
    -   For each email, parse the sales data and insert it into the SQL database.
    -   Simultaneously, insert the same data into the Excel sheet.

## Features

-   Automatically extracts hotel reservation sales data from email bodies.
-   Parses key reservation details such as Reservation ID, Guest's Name, Arrival Date, Departure Date, etc.
-   Stores the extracted data in an SQLite database.
-   Generates random hotel reservation confirmation emails for testing purposes.
-   Exports data from the database to an Excel file.

### Getting Started

1.  **Prerequisites:**
    
    -   Python (3.x recommended)
    -   `sqlite3`, `pandas`, `faker` libraries (Install using `pip install sqlite3 pandas faker`)
    - 
2.  **Setup:**
    
    -   Clone this repository to your local machine.

3.  **Usage:**
    
    -   Run the `generate_random_emails.py` script to generate random reservation confirmation emails.
    -   Modify the template and data generation in the script according to your needs.
    -   Run the `parse_emails_and_store_db.py` script to parse emails and store data in the SQLite database.
    -   Modify the email parsing logic and data transformation as required.
   
4.  **Exporting Data:**
    
    -   Use the `export_database_to_excel.py` script to export data from the SQLite database to an Excel file.
    -   The exported Excel file will be saved as `sales_data_export.xlsx`.