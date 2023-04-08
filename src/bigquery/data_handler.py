import pandas as pd
from google.cloud import bigquery

def inset_into_bigquery(stock_data: pd.DataFrame, stock_code: str) -> None:
    """
    This function inserts stock data that is formated as data frame into 
    Big Query. If the table for a given stock is not alredy created this 
    function will create the table and then insert the data, otherwise it will
    only insert the data.
    
    Args:
        stock_data (pd.DataFrame) : The structure that holds the stock data

        stock_code (str): Code from the current stock data

    
    """
    client = bigquery.Client()
    project_id = 'your-project-id'

    # Set up the table ID and dataset ID
    table_id = 'your_dataset.your_table'
    dataset_id = stock_code.lower()



    # Check if the table exists
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref, project=project_id, location='US', retry=retry)
    if table.exists():
        print(f'Table {table_id} already exists')
    else:
        # Set up the BigQuery table schema
        schema = [
            bigquery.SchemaField(name, 'STRING') for name in stock_data.columns
        ]
        table = bigquery.Table(table_ref, schema=schema)
        table = client.create_table(table, project=project_id, location='US')
        print(f'Table {table_id} created')

    # Insert the data into the BigQuery table
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = 'WRITE_TRUNCATE'
    job = client.load_table_from_dataframe(stock_data, table_ref, project=project_id, job_config=job_config)
    job.result()
