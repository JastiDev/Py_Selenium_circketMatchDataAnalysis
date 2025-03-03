import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Secure TiDB Cloud Connection
DATABASE_USER = "Ud6xHKHHCuFbH6f.root"
DATABASE_PASSWORD = "jwl7QF0l1usUQwNi"
DATABASE_HOST = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com"
DATABASE_PORT = 4000
DATABASE_NAME = "Cricket_DATA"

# Create Connection
engine = create_engine(f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}?ssl_verify_cert=false")

# Function to Create Table if Not Exists
def create_table(table_name, df):
    """Automatically creates a table if it doesn't exist"""
    conn = engine.raw_connection()
    cursor = conn.cursor()

    columns = ", ".join([f"{col} TEXT" for col in df.columns])  # All columns as TEXT (modify as needed)
    create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"

    try:
        cursor.execute(create_query)
        conn.commit()
        print(f" Table `{table_name}` checked/created successfully!")
    except Exception as e:
        print(f" Error creating table {table_name}: {e}")
    finally:
        cursor.close()
        conn.close()

# Function for Bulk Insertion in Chunks
def bulk_insert(df, table_name, batch_size=10000):
    """Insert DataFrame into MySQL using batch insertion"""
    conn = engine.raw_connection()
    cursor = conn.cursor()

    cols = ",".join(df.columns)
    placeholders = ",".join(["%s"] * len(df.columns))
    insert_query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"

    # Convert DataFrame into List of Tuples
    data = [tuple(row) for row in df.itertuples(index=False)]

    try:
        for i in range(0, len(data), batch_size):
            batch = data[i:i+batch_size]  # Insert in chunks of batch_size
            cursor.executemany(insert_query, batch)
            conn.commit()
            print(f"Inserted {len(batch)} rows into {table_name}")

    except Exception as e:
        print(f"Error inserting into {table_name}: {e}")
    finally:
        cursor.close()
        conn.close()

# Load and Insert Match Data
match_files = {
    "t20_matches": "D:\\Cricket_DA_Pro\\T20_Match\\t20matches.csv",
    "odi_matches": "D:\\Cricket_DA_Pro\\ODI_Match\\odi_matche.csv",
    "test_matches": "D:\\Cricket_DA_Pro\\TEST_Match\\Test_matches.csv"
}

for table, filepath in match_files.items():
    df = pd.read_csv(filepath)
    create_table(table, df)  # Ensure table exists
    bulk_insert(df, table)   # Insert data
print("T20, ODI, and Test match data inserted into MySQL!")

# Load and Insert Deliveries Data
delivery_files = {
    "t20_deliveries": "D:\\Cricket_DA_Pro\\T20_Match\\deliveriest20.csv",
    "odi_deliveries": "D:\\Cricket_DA_Pro\\ODI_Match\\odi_delivery.csv",
    "test_deliveries": "D:\\Cricket_DA_Pro\\TEST_Match\\Test_deliveries.csv"
}

for table, filepath in delivery_files.items():
    df = pd.read_csv(filepath)
    create_table(table, df)  # Ensure table exists
    bulk_insert(df, table)   # Insert data
print("T20, ODI, and Test deliveries data inserted into MySQL!")
