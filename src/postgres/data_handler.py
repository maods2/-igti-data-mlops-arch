import os

import pandas as pd
import psycopg2


def query_stocks_available():
    # Establish a connection to the PostgreSQL database
    # db_password = os.environ.get('DB_PASSWORD')
    db_password = "senha@123"
    conn = psycopg2.connect(
        database='finance_db',
        user='admin',
        password=db_password,
        host='35.188.18.214',
        port='5432',
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a SELECT statement to retrieve data from a table
    cur.execute(
        'SELECT stock_code, stock_name, status FROM mlops.stock_data'
    )

    # Fetch all rows of the result
    rows = cur.fetchall()

    # Convert the result to a pandas DataFrame
    df = pd.DataFrame(rows, columns=['stock_code', 'stock_name', 'status'])

    # Close the cursor and the connection
    cur.close()
    conn.close()

    # Return the result as a pandas DataFrame
    return df['stock_code'][df['status'] == 'True'].values
