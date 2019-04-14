import datetime

import pandas as pd

class DataReader:

    def df(self, year=1967):
        data = self.get_data()
        query = f"dt >= '{year}' and dt < '{year + 1}'"
        return data.query(query)

    def get_data(self):
        data = pd.read_csv("data/monthly-car-sales-in-quebec-1960.csv")[:-1]
        data["dt"] = data["Month"].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m'))
        data =  data.rename({"Monthly car sales in Quebec 1960-1968": "sales"}, axis=1)\
            [['dt', "sales"]]
        return data

    @property
    def years(self):
        data = self.get_data()
        return data['dt'].apply(lambda x: x.year).unique()
