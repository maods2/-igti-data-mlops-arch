import logging

import pandas as pd

# from utils.logger import MyLogger

ERROR_MESSAGE = "Data does not have 'Close' attribute."
# logger = MyLogger().logger
logger = logging


def generate_indicators(stock_data: pd.DataFrame) -> pd.DataFrame:
    """
    This function is responsable for extract some finance indicators based on the
    give stock data.

    args:
      stock_data: pd.DataFrame = Stock data.

    returns:
      this function returns the original dataframe appended with the finance
      indicators calculated based on the given stock data.
    """
    logger.info('Calculating indicator...')
    data = get_moving_average(stock_data)
    data = get_exponential_moving_average(data)
    data = get_relative_strength_index(data)
    data = get_moving_average_convergence_divergence(data)
    data = get_bollinger_bands(data)
    return data


def get_moving_average(data: pd.DataFrame):
    """
    This function calculates moving averages

    Args:
      data (pd.DataFrame): Dataframe with stock data.

    Returns:
      pd.DataFrame: Data frame added the moving averages indicator

    """
    assert 'Close' in data.columns, ERROR_MESSAGE
    data['MA10'] = data['Close'].rolling(window=10).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()
    return data


def get_exponential_moving_average(data: pd.DataFrame):
    """
    This function calculates exponential moving averages

    Args:
      data (pd.DataFrame): Dataframe with stock data.

    Returns:
      pd.DataFrame: Data frame added the exponential moving averages indicator

    """
    assert 'Close' in data.columns, ERROR_MESSAGE
    data['EMA10'] = data['Close'].ewm(span=10, adjust=False).mean()
    data['EMA50'] = data['Close'].ewm(span=50, adjust=False).mean()
    return data


def get_relative_strength_index(data: pd.DataFrame):
    """
    This function calculates relative strength index (RSI)

    Args:
      data (pd.DataFrame): Dataframe with stock data.

    Returns:
      pd.DataFrame: Data frame added the RSI indicator

    """
    assert 'Close' in data.columns, ERROR_MESSAGE
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data


def get_moving_average_convergence_divergence(data: pd.DataFrame):
    """
    This function calculates moving average convergence divergence (MACD)

    Args:
      data (pd.DataFrame): Dataframe with stock data.

    Returns:
      pd.DataFrame: Data frame added the moving average convergence divergence (MACD) indicator

    """
    assert 'Close' in data.columns, ERROR_MESSAGE
    data['EMA12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()
    return data


def get_bollinger_bands(data: pd.DataFrame):
    """
    This function calculates Bollinger Bands

    Args:
      data (pd.DataFrame): Dataframe with stock data.

    Returns:
      pd.DataFrame: Data frame added the Bollinger Bands indicator

    """
    assert 'Close' in data.columns, ERROR_MESSAGE
    data['20MA'] = data['Close'].rolling(window=20).mean()
    data['Upper'] = data['20MA'] + 2 * data['Close'].rolling(window=20).std()
    data['Lower'] = data['20MA'] - 2 * data['Close'].rolling(window=20).std()
    return data
