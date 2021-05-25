#Flask imports
from flask import Flask, render_template, send_file, make_response, url_for, Response

#Pandas and Matplotlib
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#other requirements
import io

#Data imports

#from GetFixtres import ECS_data
ECS_data = pd.read_csv("./data/out.csv")
#from GetFixtures2 import GK_roi
GK_roi = pd.read_csv("./data/out.csv")


app = Flask(__name__)

#Pandas Page
@app.route('/')
@app.route('/pandas', methods=("POST", "GET"))
def GK():
    return render_template('index.html',
                           PageTitle = "Pandas",
                           table=[GK_roi.to_html(classes='data', index = False)], titles= GK_roi.columns.values)


#Matplotlib page
@app.route('/matplot', methods=("POST", "GET"))
def mpl():
    return render_template('matplot.html',
                           PageTitle = "Matplotlib")


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig, ax = plt.subplots(figsize = (6,4))
    fig.patch.set_facecolor('#E8E5DA')

    x = ECS_data["Month"]
    y = ECS_data["Year"]

    ax.bar(x, y, color = "#304C89")

    plt.xticks(rotation = 30, size = 5)
    plt.ylabel("Expected Clean Sheets", size = 5)


    return fig


if __name__ == '__main__':
    app.run(debug = True)

'''
@app.route("/")
def intro():
    return render_template('index.html')

@app.route("/analysis", method=["GET"])
# returns results of analysis, does not take user preferences
# data sent back: correlation, head, more to be added
def analysis():
    pass
@app.route("/data")
'''
# returns data according to the preferences chosen by the user
# includes: feature selection, month selection, department selection, type selection POST
# includes: predicted outcome head or full dataframe or mean, GET
