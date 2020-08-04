"""
Function to Report NaN Values
"""

import pandas as pd
import numpy as np


def report_NaN(df):
    results = df.isnull().sum()

    print(results)