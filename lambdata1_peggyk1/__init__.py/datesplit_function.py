"""
Funtion to change to datetime format and split into day/month/year columns
"""

import pandas as pd


def datesplit(df):
    df['date'] = pd.to_datetime(df['date'])

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day

    return df