import plotly
import plotly.graph_objs as go


import pandas as pd
import numpy as np
import json

from data_reader import DataReader

class Graph:

    def __init__(self):
        self.data_reader = DataReader()
        
    def get_plot(self, year=1967):

        df = self.data_reader.df(year=year)
        trace = go.Scatter(
            x = df["dt"],
            y = df["sales"]
        )
        data = [trace]        
        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    @property
    def years(self):
        return list(self.data_reader.years)
