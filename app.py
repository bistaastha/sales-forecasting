import os
from botocore.history import get_global_history_recorder
import pandas as pd
from flask import Response, Flask, send_file, request, jsonify, make_response
from flask.templating import render_template
import sys
import os
import project.utils.processing as prc
import dataframe_image as dfi

pd.set_option('display.max_rows', 15)

app = Flask(__name__)
out = pd.read_csv('./data/out.csv')

@app.route('/')
def show_template():
    return render_template('index.html')

@app.route('/dataframe')
def display_frame():
    return render_template('dataframe.html')

@app.route('/data', methods = ["POST"])
def data():
    if request.method == 'POST':
        print(request.data, flush=True)
        html_er, desc = prc.d_processing(request.data, out)
        datapath = os.path.join(os.getcwd() + '/static/img')
        dfi.export(
            desc,
            os.path.join(datapath, 'out.png')
        )
        print(html_er, flush = True)
        global er_html
        er_html = html_er
        return 'OK', 200



@app.route('/result')
def result():
    d = {"html_er": er_html}
    return jsonify(d)

if __name__ == "__main__":
    app.run(port=5000, debug = True)
