import pyodbc

# Azure SQL Database connection details
SERVER = "sentimentanalysis1006.database.windows.net"
DATABASE = "SentimentDB"
USERNAME = "SqlDbAdmin"
PASSWORD = "SqlDbAdmin"
DRIVER = "{ODBC Driver 17 for SQL Server}"

def query_sql():
    # Connect to the database
    conn = pyodbc.connect(
        f"DRIVER={DRIVER};SERVER={SERVER};PORT=1433;DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
    )
    cursor = conn.cursor()

    # Query data
    cursor.execute("SELECT TOP 10 * FROM SentimentResults")
    for row in cursor.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    query_sql()
