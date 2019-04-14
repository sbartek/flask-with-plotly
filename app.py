from flask import Flask, render_template

from graph import Graph

app = Flask(__name__)


@app.route('/car_plot')
def car_plot():
    graph = Graph()
    json_plot = graph.get_plot()
    return render_template('index.html', plot=json_plot)

if __name__ == '__main__':
    app.run()
