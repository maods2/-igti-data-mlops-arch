import os
import json
from utils.logger import MyLogger
from rest.call import get_stock_data
from pipeline.processing import generate_indicators
from bigquery.data_handler import inset_into_bigquery
from postgres.data_handler import query_stocks_available

logger = MyLogger().logger

def data_pipeline(request):
    """
    HTTP Cloud Function that returns the value of FOO.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """

    logger.info('Handler Started!')
    request_body = request.get_data()
    request_body_str = request_body.decode('utf-8')
    request_body_dict = json.loads(request_body_str)
    property_value = request_body_dict.get('pipeline_type')

    if property_value == "Daily":
        result = start_daily_pipeline()
    
    elif property_value == "Weekly":
        result = start_weekly_pipeline() 

    else:
        return "error", 500

    logger.info(f'The value of response is {result}')
    return result





def start_daily_pipeline() -> bool:
    """ This function is responsible for run the datapipeline
    """
    # list_of_stocks = ["EGIE3.SA"]
    list_of_stocks = query_stocks_available()

    for stock_code in list_of_stocks:
        data = get_stock_data(stock_code)
        data = generate_indicators(data)
        inset_into_bigquery(data)
    
    return True


def start_weekly_pipeline() -> bool:
    """ This function is responsible for run the datapipeline
    """
    pass


