import pandas as pd


class MyDataFrame(pd.MyDataFrame):
    """ Reports number of cells """
    def num_cells(self):
        return self.shape[0] * self.shape[1]