import numpy as np
import pandas as pd

from src.pipeline.processing import get_relative_strength_index


def generate_dummy_stock():
    # Generate mock stock market data for a single stock
    n_days = 100

    dates = pd.date_range('2022-01-01', periods=n_days)
    high = pd.Series(np.random.rand(n_days), index=dates)
    low = pd.Series(np.random.rand(n_days), index=dates)
    close = pd.Series(np.random.rand(n_days), index=dates)
    _open = pd.Series(np.random.rand(n_days), index=dates)

    # Combine the series into a single dataframe
    data = pd.DataFrame(
        {'High': high, 'Low': low, 'Close': close, 'Open': _open}
    )

    # Print the first 5 rows of the data
    return data


stock_data = generate_dummy_stock()


def test_add_positive_numbers():
    result = get_relative_strength_index(stock_data)
    assert result.shape[1] == 5
