import pandas as pd
import psycopg2
import os
import json
from dotenv import load_dotenv

load_dotenv()

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv("CVE.csv")
    df = df.rename(columns={
        "CVE-ID": "CVE_ID",
        "CWE-ID": "CWE_ID",
        "Affected Packages": "Affected_Packages"
    })

    # Convert the DataFrame to JSON
    json_data = df.to_json(orient="records")

    URL = os.getenv("DB_URL")
    # ElephantSQL URI
    elephantsql_uri = URL

    # Connect to PostgreSQL
    conn = psycopg2.connect(elephantsql_uri)

    # Create a cursor object
    cur = conn.cursor()

    # Define the PostgreSQL table schema
    table_schema = """
    CREATE TABLE IF NOT EXISTS cve (
        id SERIAL PRIMARY KEY,
        CVE_ID VARCHAR(20),
        Severity VARCHAR(20),
        CVSS FLOAT,
        Affected_Packages VARCHAR(50),
        Description TEXT,
        CWE_ID VARCHAR(20)
    );
    """

    # Execute the SQL query to create the table
    cur.execute(table_schema)

    # Convert JSON data to list of dictionaries
    json_list = json.loads(json_data)

    # Define the SQL query to insert JSON data into the table
    sql = """
    INSERT INTO cve (CVE_ID, Severity, CVSS, Affected_Packages, Description, CWE_ID)
    VALUES (%(CVE_ID)s, %(Severity)s, %(CVSS)s, %(Affected_Packages)s, %(Description)s, %(CWE_ID)s);
    """

    # Execute the SQL query with JSON data as parameter
    try:
        cur.executemany(sql, json_list)
    except psycopg2.Error as e:
        print("Error occurred while executing SQL query:", e)
        raise

    # Commit the transaction
    try:
        conn.commit()
    except psycopg2.Error as e:
        print("Error occurred while committing transaction:", e)
        raise

except (Exception, psycopg2.DatabaseError) as error:
    print("Error occurred:", error)

finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()
