from flask import Flask, render_template, jsonify
from multiprocessing import Process, Manager
import random, importlib

import Households

app = Flask(__name__)

def get_live_data():
    print(shared_data["house1"])
    return {
        "house1": shared_data["house1"],
        "house2": shared_data["house2"],
        "house3": shared_data["house3"],
        "house4": shared_data["house4"]
    }

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def data():
    return jsonify(get_live_data())

if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    manager = Manager()
    shared_data = manager.dict({"house1": {}, "house2": {}, "house3": {}, "house4": {}})
    process = Process(target=Households.run, args=(shared_data,))
    process.start()
    
    app.run()
    process.join()