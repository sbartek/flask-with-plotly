from flask import Flask, render_template, request
import pandas as pd

from data_generator import DataReader
from plotly_graph import PlotlyGraph
from config_parser import parse_default_config

from config import DATA_PATH, INDEX_COL_NAME, VALUE_COL_NAME, COLORS


def create_app(config_fn=""):
    app = Flask(__name__)
    app_config = parse_default_config(additional_config_fn=config_fn)
    app.config['app_config'] = app_config
    return app

#app = create_app(config_fn="flask_app_config.yaml")
app = create_app(config_fn="")
    
@app.route('/', methods=['GET', 'POST'])
def brownian_plot():
    config = app.config['app_config']
    df = DataReader().data_frame(config['data_path'])
    if request.method == "POST":
        plot_color = request.form["color"]
    else:
        plot_color = 'blue'

    plotly_graph = PlotlyGraph(
        config['index_col_name'],
        config['value_col_name'],
        plot_color)
    json_graph = plotly_graph.get_json_graph(df)
    return render_template(
        'graph_plot.html',
        plot=json_graph,
        colors=config['colors'],
        plot_color=plot_color)

if __name__ == '__main__':
    app.run()
