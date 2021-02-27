from flask import Flask, send_file, make_response, session
from flask import request, jsonify
import matplotlib.pyplot as plt
import io
from M0_main import code
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)                ## Handled Cross Origin Resource Sharing Policy 

## Define Homepage Route
@app.route('/', methods = ['GET'])
def home():
    return "<h1> Welcome to Homepage </h1>"

## Form Connection and Data Delivery API Route
@app.route('/word', methods = ['GET', 'POST'])
def wordspace():
    if request.method == 'GET':
        place = request.args.get('place')
        data = code(place)                      ## Taking the user keyword and running it for backend
        data = data[0]                          ## Taking dictionary (includes Pie chart information and Word Cloud Information)
        return jsonify(data)                    ## JSON Response Data

app.run()