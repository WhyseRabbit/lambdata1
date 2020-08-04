"""
Dataframe to test functionality of functions
"""

import pandas as pd
import numpy as np


data = {'date': [
                '7-25-20', '7-26-20', '7-27-20',
                '7-28-20', '7-29-20', '7-30-20'
                ],
        'good_day': [np.NaN, 1, 1, np.NaN, 0, 0],
        'bad_day': [np.NaN, 0, 0, np.NaN, 1, 1]
        }

test = pd.DataFrame(data, columns=['date', 'good_day', 'bad_day'])

print(test)