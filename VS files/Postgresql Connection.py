import psycopg2
import pandas as pd

# PostgreSQL connection details
db_params = {
    "dbname": "Netflix",  # Your database name
    "user": "postgres",  # Your PostgreSQL username
    "password": "Paras@123",  # Your PostgreSQL password
    "host": "localhost",  # Change if different
    "port": "5432"  # Default PostgreSQL port
}

# Load CSV file
file_path = r"E:\Personal Resources_DA\SQL\Project\Netflix Dataset\Dataset\Netflix Dataset (Raw).csv"
df = pd.read_csv(file_path)

# Connect to PostgreSQL
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Insert data row by row
for index, row in df.iterrows():
    cur.execute("""
        INSERT INTO netflix (show_id, category, title, director, cast_members, country, release_date, rating, duration, type, description) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (show_id) DO NOTHING;
    """, (row["Show_Id"], row["Category"], row["Title"], row["Director"], 
          row["Cast_members"], row["Country"], row["Release_Date"], row["Rating"], 
          row["Duration"], row["Type"], row["Description"]))


# Commit and close
conn.commit()
cur.close()
conn.close()

print("CSV data inserted successfully!")
