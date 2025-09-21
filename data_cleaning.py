import pandas as pd

def load_and_clean_data(path='../data/covid_data.csv'):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna(subset=['total_cases', 'total_deaths'])
    return df
