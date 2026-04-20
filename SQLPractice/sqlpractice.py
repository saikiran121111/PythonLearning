import sqlite3
# Connect to a database (creates the file if it doesn't exist)
con = sqlite3.connect('practice.db') # To connect Database no file exists creates a file

# Create a cursor — this is what runs SQL queries
cursor = con.cursor()# Used to run queries

print('Db Connected')

con.close() # Closes the connection