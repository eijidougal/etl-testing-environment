import pyodbc

def seed_mssql():
    # Define the connection string
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=127.0.0.1,1433;"  # Use '127.0.0.1' or 'mssql'
        "DATABASE=master;"
        "UID=sa;"
        "PWD=YourStrong@Passw0rd;"
        "TrustServerCertificate=yes;"
        "timeout=30;"
    )

    try:
        cursor = conn.cursor()

        # Drop the table if it exists to start fresh
        cursor.execute("IF OBJECT_ID('dbo.test_table', 'U') IS NOT NULL DROP TABLE dbo.test_table;")

        # Create the table
        cursor.execute("""
            CREATE TABLE dbo.test_table (
                id INT PRIMARY KEY,
                name NVARCHAR(100),
                value INT
            );
        """)

        # Insert sample data
        sample_data = [
            (1, 'Item 1', 100),
            (2, 'Item 2', 200),
            (3, 'Item 3', 300),
            (4, 'Item 4', 400),
            (5, 'Item 5', 500),
        ]

        # Insert data into the table
        for item in sample_data:
            cursor.execute("INSERT INTO dbo.test_table (id, name, value) VALUES (?, ?, ?);", item)

        # Commit the transaction
        conn.commit()
        print("MSSQL database seeded successfully with sample data.")
    except Exception as e:
        print(f"Error seeding MSSQL database: {e}")
    finally:
        # Close the connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    seed_mssql()
