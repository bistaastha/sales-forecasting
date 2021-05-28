#Flask imports
'''
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
ECS_data = pd.read_csv("./data/train.csv")
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
    return render_template('index.html',
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

    x = ECS_data["Dept"]
    y = ECS_data["A"]

    ax.bar(x, y, color = "#304C89")

    plt.xticks(rotation = 30, size = 5)
    plt.ylabel("Expected Clean Sheets", size = 5)


    return fig


if __name__ == '__main__':
    app.run(debug = True)


'''
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

#from flask import Flask
#from flask_cors import crossorigin

#app = Flask(__name__)
#CORS(app)
#cors = CORS(app,resources={r"/test": {"origins": "http://localhost:5000"}})
#r"/foo": {"origins": "http://localhost:port"}}
#@app.route('/test', methods=['GET', 'POST'])
#@crossorigin()
#def testfn():    # GET request
#    if request.method == 'GET':
#        message = {'greeting':'Hello from Flask!'}
#        message.headers.add("Access-Control-Allow-Origin", "*")
#        return jsonify(message)  # serialize and use JSON headers    # POST request
#    if request.method == 'POST':
#        print(request.get_json())  # parse as JSON
#        message.headers.add("Access-Control-Allow-Origin", "*")
#        return 'Sucesss', 200

#if __name__ == '__main__':
#   app.run()

'''
REST - The term REST stands for REpresentational State Transfer. It is an architectural style that defines a set of rules in order to create Web Services.
REST is based on the resources which means when we use methods like GET, POST, PUT and DELETE (CRUD operations), we basically create, read, update ond delete a
resource. To perform these actions we use HTTP methods which are REST API methods.
Whenever a client requests some resource via API, it's made available by server in the form of some light weight data form such as JSON, XML etc.
REST API is based on six principles - stateless, client-server, uniform interface, Cacheable, Layered system, Code on demand.
In this code we are going to use the GET and POST methods to read and write the resources using end points as mentioned below -
GET - server will send data to client
POST - server will receive data from client
POST (create a new store with a given name) - http://127.0.0.1:5000/store {"name":"storeName"}
GET (get a store with a given name) - http://127.0.0.1:5000/store/<string:name>
GET (return all the stores) - http://127.0.0.1:5000/store
POST (create an item inside a specific store) - http://127.0.0.1:5000/store/<string:name>/item {name:"name", price:xyz}
GET (get all the items from a specific store) - http://127.0.0.1:5000/store/<string:name>/item
'''


from flask import Flask, jsonify, request
from flask.templating import render_template

app = Flask(__name__)

'''
Normally these resources will be stored in a database but we are using a set of data structures
in our case i.e. list and disctionary.
'''
stores = [
    {
        'name':'My Beutiful Store',
        'items':[
            {
                'name':'My Item',
                'price':15.99
            }
        ]

    }
]


@app.route('/')
def home():
    return render_template('index2.html')


# POST /store data:{"name":"storeName"}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    stores.headers.add("Access-Control-Allow-Origin", "*")
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>') #127.0.0.1:5000/store/someName
def get_store(name):
    '''
    iterate over stores, if the store name matches, return it.
    If no match, return an error message
    '''
    for store in stores:
        if name == store['name']:
            return jsonify(store)
        else:
            return jsonify({'message':'store not found'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


# POST /store/<string:name>/item {name:"name", price:xyz}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify({'message':'store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})


'''
Runs the application to local development server
In your system you will see it as 127.0.0.1 or localhost
'''
app.run(port=5000)
