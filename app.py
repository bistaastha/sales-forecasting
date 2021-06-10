import os
import pandas as pd
from flask import Response, Flask, send_file, request
from flask.templating import render_template

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

import dataframe_image as dfi

from matplotlib.figure import Figure
matplotlib.use('Agg')

app = Flask(__name__)
out = pd.read_csv('./data/out.csv')

@app.route('/')
def show_template():
    return render_template('index.html')

@app.route('/dataframe')
def display_frame():
    out_head = out.head()
    datapath = os.path.join(os.getcwd() + '/static/img')
    dfi.export(
        out_head,
        os.path.join(datapath, 'out.png')
    )
    return render_template('dataframe.html')

@app.route('/heatmap.png')
def plot_png():
    datapath = os.path.join(os.getcwd() + '/public', 'out.png')
    return send_file(datapath, mimetype='image/png')

@app.route('/data', methods = ["POST"])
def data():
    if request.method == 'POST':
        print(request.data, flush=True)
        processing()
        return 'OK', 200
    
if __name__ == "__main__":
    app.run(port=5000, debug = True)
