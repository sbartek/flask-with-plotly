from flask import Flask, render_template, request
import pandas as pd

from data_generator import DataReader
from plotly_graph import PlotlyGraph

from config import DATA_PATH, INDEX_COL_NAME, VALUE_COL_NAME, COLORS

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def brownian_plot():

    df = DataReader().data_frame(DATA_PATH)
    if request.method == "POST":
        plot_color = request.form["color"]
    else:
        plot_color = 'blue'

    plotly_graph = PlotlyGraph(INDEX_COL_NAME, VALUE_COL_NAME, plot_color)
    json_graph = plotly_graph.get_json_graph(df)
    return render_template(
        'graph_plot.html',
        plot=json_graph,
        colors=COLORS,
        plot_color=plot_color)

if __name__ == '__main__':
    app.run()
