import sqlite3
import pandas as pd

# Connect to the SQLite database
db_connection = sqlite3.connect('sales_database.db')

# Query data from the sales_data table
query = 'SELECT * FROM sales_data'
df = pd.read_sql_query(query, db_connection)

# Disconnect from the database
db_connection.close()

# Export data to Excel
excel_output_path = 'sales_data_export.xlsx'
df.to_excel(excel_output_path, index=False)

print(f'Data exported to {excel_output_path}')