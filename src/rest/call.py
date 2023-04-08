import datetime
import yfinance as yf
import pandas as pd
from utils.logger import MyLogger

logger = MyLogger().logger

def get_stock_data(stock_code: str, time_frame: str="5m") -> pd.DataFrame:
  """
  This function is responsible to return the stock data for the given stock from
  da last work day.

  args:
    stock_code: str -> stock code that will be used to invoke yahoo finance rest
    api.
    time_frame: str -> timeframe in which is desired to retrieve the stock data.
    Default value is "5m".
  returns:
    pd.DataFrame
  """

  today = datetime.date.today()
  yesterday = today - datetime.timedelta(days=1)
  data = yf.download(stock_code, start=yesterday,end=today, interval = time_frame)
  logger.info(f'Retrieving data from {stock_code} stock...')
  logger.info(f'Data shape: {data.shape}.')
  return data