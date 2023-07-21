import pyodbc

# Replace the following variables with your SQL Server connection details
server = 'localhost'
database = 'api_test'

# Create the connection string
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

try:
    # Establish the connection
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Example: Execute a query
    cursor.execute('SELECT TOP 5 * FROM dbo.api_test_table')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    connection.close()

except pyodbc.Error as ex:
    print('Error:', ex)
    print('Error code:', ex.args[0])
    print('Error message:', ex.args[1])
