from flask import Flask, render_template, request

from graph import Graph

app = Flask(__name__)


@app.route('/car_plot', methods=['GET', 'POST'])
def car_plot():

    graph = Graph()	
    years = graph.years

    if request.method == "POST":
        year = int(request.form["year"])
    else:
        year = years[0]
        
    json_plot = graph.get_plot(year=year)
    return render_template('graph_plot.html', plot=json_plot, years=years, current_year=year)

        
if __name__ == '__main__':
    app.run()
