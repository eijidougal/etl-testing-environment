import psycopg2

def seed_postgres():
    # Define the connection string
    conn = psycopg2.connect(
        dbname="testdb",  # Replace with your database name
        user="user",      # Replace with your PostgreSQL username
        password="password",  # Replace with your PostgreSQL password
        host="localhost",  # Use 'localhost' if running on your local machine
        port="5432"        # Default PostgreSQL port
    )

    try:
        cursor = conn.cursor()

        # Drop the table if it exists to start fresh
        cursor.execute("DROP TABLE IF EXISTS test_table;")

        # Create the table
        cursor.execute("""
            CREATE TABLE test_table (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                value INT
            );
        """)

        # Insert sample data
        sample_data = [
            ('Item 1', 100),
            ('Item 2', 200),
            ('Item 3', 300),
            ('Item 4', 400),
            ('Item 5', 500),
        ]

        # Insert data into the table
        cursor.executemany("INSERT INTO test_table (name, value) VALUES (%s, %s);", sample_data)

        # Commit the transaction
        conn.commit()
        print("PostgreSQL database seeded successfully with sample data.")
    except psycopg2.Error as e:
        print(f"Error seeding PostgreSQL database: {e}")
    finally:
        # Close the connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    seed_postgres()
