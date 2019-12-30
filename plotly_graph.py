import json

import plotly
import plotly.graph_objs as go

class PlotlyGraph:

    def __init__(self, x_col_name, y_col_name, color='blue'):
        self.x_col_name = x_col_name
        self.y_col_name = y_col_name
        self.color = color

    def get_plotly_data(self, df):
        trace = go.Scatter(
            x = df[self.x_col_name],
            y = df[self.y_col_name],
            line={'color': self.color}
        )
        return [trace]        
        
    def get_json_graph(self, df):
        data = self.get_plotly_data(df)
        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

