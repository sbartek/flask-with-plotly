import plotly
import plotly.graph_objs as go


import pandas as pd
import numpy as np
import json

from data_reader import DataReader

class Graph:

    def __init__(self):
        self.data_reader = DataReader()
        print(self.data_reader.years)
        
    def get_plot(self):

        df = self.data_reader.df()
        trace = go.Scatter(
            x = df["dt"],
            y = df["sales"]
        )
        data = [trace]        
        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON
