import pandas as pd

def load_and_process_data(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    df['Price Range'] = df['High'] - df['Low']

    df_resampled = df.resample('M').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum',
        'Price Range': 'mean'
    })

    return df_resampled
