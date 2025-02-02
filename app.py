from flask import Flask, render_template, jsonify

import random


app = Flask(__name__)

house_data={
    "house1": {
        "1": {"bank": 100.0, "production": 30, "usage": 40, "money": 0.0},
        "2": {"bank": 90.0, "production": 30, "usage": 40, "money": 0.0},
        "3": {"bank": 200.0, "production": 30, "usage": 40, "money": -15.456},
        "4": {"bank": 190.0, "production": 30, "usage": 40, "money": -15.456},
        "5": {"bank": 180.0, "production": 30, "usage": 40, "money": -15.456},
        "6": {"bank": 170.0, "production": 30, "usage": 40, "money": -15.456},
        "7": {"bank": 160.0, "production": 30, "usage": 40, "money": -15.456},
        "8": {"bank": 150.0, "production": 30, "usage": 40, "money": -15.456},
        "9": {"bank": 140.0, "production": 30, "usage": 40, "money": -15.456},
        "10": {"bank": 130.0, "production": 30, "usage": 40, "money": -15.456},
        "11": {"bank": 120.0, "production": 30, "usage": 40, "money": -15.456},
        "12": {"bank": 110.0, "production": 30, "usage": 40, "money": -15.456},
        "13": {"bank": 100.0, "production": 30, "usage": 40, "money": -15.456},
        "14": {"bank": 90.0, "production": 30, "usage": 40, "money": -15.456},
        "15": {"bank": 200.0, "production": 30, "usage": 40, "money": -30.912},
        "16": {"bank": 190.0, "production": 30, "usage": 40, "money": -30.912},
        "17": {"bank": 180.0, "production": 30, "usage": 40, "money": -30.912},
        "18": {"bank": 170.0, "production": 30, "usage": 40, "money": -30.912},
        "19": {"bank": 160.0, "production": 30, "usage": 40, "money": -30.912},
        "20": {"bank": 150.0, "production": 30, "usage": 40, "money": -30.912},
        "21": {"bank": 140.0, "production": 30, "usage": 40, "money": -30.912},
        "22": {"bank": 130.0, "production": 30, "usage": 40, "money": -30.912},
        "23": {"bank": 120.0, "production": 30, "usage": 40, "money": -30.912},
        "24": {"bank": 110.0, "production": 30, "usage": 40, "money": -30.912},
        "25": {"bank": 100.0, "production": 30, "usage": 40, "money": -30.912},
        "26": {"bank": 90.0, "production": 30, "usage": 40, "money": -30.912},
        "27": {"bank": 200.0, "production": 30, "usage": 40, "money": -46.368},
        "28": {"bank": 190.0, "production": 30, "usage": 40, "money": -46.368},
        "29": {"bank": 180.0, "production": 30, "usage": 40, "money": -46.368},
        "30": {"bank": 170.0, "production": 30, "usage": 40, "money": -46.368}
    },
    "house2": {
        "1": {"bank": 100.0, "production": 100, "usage": 10, "money": 0.0},
        "2": {"bank": 190.0, "production": 100, "usage": 10, "money": 0.0},
        "3": {"bank": 160.0, "production": 100, "usage": 10, "money": 15.456},
        "4": {"bank": 250.0, "production": 100, "usage": 10, "money": 15.456},
        "5": {"bank": 110.0, "production": 100, "usage": 10, "money": 45.08},
        "6": {"bank": 200.0, "production": 100, "usage": 10, "money": 45.08},
        "7": {"bank": 185.0, "production": 100, "usage": 10, "money": 58.604},
        "8": {"bank": 275.0, "production": 100, "usage": 10, "money": 58.604},
        "9": {"bank": 365.0, "production": 100, "usage": 10, "money": 58.604},
        "10": {"bank": 455.0, "production": 100, "usage": 10, "money": 58.604},
        "11": {"bank": 545.0, "production": 100, "usage": 10, "money": 58.604},
        "12": {"bank": 635.0, "production": 100, "usage": 10, "money": 58.604},
        "13": {"bank": 565.0, "production": 100, "usage": 10, "money": 79.212},
        "14": {"bank": 535.0, "production": 100, "usage": 10, "money": 94.668},
        "15": {"bank": 625.0, "production": 100, "usage": 10, "money": 94.668},
        "16": {"bank": 715.0, "production": 100, "usage": 10, "money": 94.668},
        "17": {"bank": 805.0, "production": 100, "usage": 10, "money": 94.668},
        "18": {"bank": 895.0, "production": 100, "usage": 10, "money": 94.668},
        "19": {"bank": 985.0, "production": 100, "usage": 10, "money": 94.668},
        "20": {"bank": 1075.0, "production": 100, "usage": 10, "money": 94.668},
        "21": {"bank": 1005.0, "production": 100, "usage": 10, "money": 115.276},
        "22": {"bank": 1095.0, "production": 100, "usage": 10, "money": 115.276},
        "23": {"bank": 1185.0, "production": 100, "usage": 10, "money": 115.276},
        "24": {"bank": 1275.0, "production": 100, "usage": 10, "money": 115.276},
        "25": {"bank": 1365.0, "production": 100, "usage": 10, "money": 115.276},
        "26": {"bank": 1455.0, "production": 100, "usage": 10, "money": 115.276},
        "27": {"bank": 1425.0, "production": 100, "usage": 10, "money": 130.732},
        "28": {"bank": 1410.0, "production": 100, "usage": 10, "money": 144.256},
        "29": {"bank": 1340.0, "production": 100, "usage": 10, "money": 164.864},
        "30": {"bank": 1430.0, "production": 100, "usage": 10, "money": 164.864}
    },
    "house3": {
        "1": {"bank": 100.0, "production": 30, "usage": 50, "money": 0.0},
        "2": {"bank": 80.0, "production": 30, "usage": 50, "money": 0.0},
        "3": {"bank": 60.0, "production": 30, "usage": 50, "money": 0.0},
        "4": {"bank": 40.0, "production": 30, "usage": 50, "money": 0.0},
        "5": {"bank": 250.0, "production": 30, "usage": 50, "money": -29.624},
        "6": {"bank": 230.0, "production": 30, "usage": 50, "money": -29.624},
        "7": {"bank": 210.0, "production": 30, "usage": 50, "money": -29.624},
        "8": {"bank": 190.0, "production": 30, "usage": 50, "money": -29.624},
        "9": {"bank": 170.0, "production": 30, "usage": 50, "money": -29.624},
        "10": {"bank": 150.0, "production": 30, "usage": 50, "money": -29.624},
        "11": {"bank": 130.0, "production": 30, "usage": 50, "money": -29.624},
        "12": {"bank": 110.0, "production": 30, "usage": 50, "money": -29.624},
        "13": {"bank": 250.0, "production": 30, "usage": 50, "money": -50.232},
        "14": {"bank": 230.0, "production": 30, "usage": 50, "money": -50.232},
        "15": {"bank": 210.0, "production": 30, "usage": 50, "money": -50.232},
        "16": {"bank": 190.0, "production": 30, "usage": 50, "money": -50.232},
        "17": {"bank": 170.0, "production": 30, "usage": 50, "money": -50.232},
        "18": {"bank": 150.0, "production": 30, "usage": 50, "money": -50.232},
        "19": {"bank": 130.0, "production": 30, "usage": 50, "money": -50.232},
        "20": {"bank": 110.0, "production": 30, "usage": 50, "money": -50.232},
        "21": {"bank": 250.0, "production": 30, "usage": 50, "money": -70.84},
        "22": {"bank": 230.0, "production": 30, "usage": 50, "money": -70.84},
        "23": {"bank": 210.0, "production": 30, "usage": 50, "money": -70.84},
        "24": {"bank": 190.0, "production": 30, "usage": 50, "money": -70.84},
        "25": {"bank": 170.0, "production": 30, "usage": 50, "money": -70.84},
        "26": {"bank": 150.0, "production": 30, "usage": 50, "money": -70.84},
        "27": {"bank": 130.0, "production": 30, "usage": 50, "money": -70.84},
        "28": {"bank": 110.0, "production": 30, "usage": 50, "money": -70.84},
        "29": {"bank": 250.0, "production": 30, "usage": 50, "money": -91.448},
        "30": {"bank": 230.0, "production": 30, "usage": 50, "money": -91.448}
    },
    "house4": {
        "1": {"bank": 100.0, "production": 30, "usage": 50, "money": 0.0},
        "2": {"bank": 95.0, "production": 30, "usage": 50, "money": 0.0},
        "3": {"bank": 90.0, "production": 30, "usage": 50, "money": 0.0},
        "4": {"bank": 85.0, "production": 30, "usage": 50, "money": 0.0},
        "5": {"bank": 80.0, "production": 30, "usage": 50, "money": 0.0},
        "6": {"bank": 75.0, "production": 30, "usage": 50, "money": 0.0},
        "7": {"bank": 175.0, "production": 30, "usage": 50, "money": -13.524},
        "8": {"bank": 170.0, "production": 30, "usage": 50, "money": -13.524},
        "9": {"bank": 165.0, "production": 30, "usage": 50, "money": -13.524},
        "10": {"bank": 160.0, "production": 30, "usage": 50, "money": -13.524},
        "11": {"bank": 155.0, "production": 30, "usage": 50, "money": -13.524},
        "12": {"bank": 150.0, "production": 30, "usage": 50, "money": -13.524},
        "13": {"bank": 145.0, "production": 30, "usage": 50, "money": -13.524},
        "14": {"bank": 140.0, "production": 30, "usage": 50, "money": -13.524},
        "15": {"bank": 135.0, "production": 30, "usage": 50, "money": -13.524},
        "16": {"bank": 130.0, "production": 30, "usage": 50, "money": -13.524},
        "17": {"bank": 125.0, "production": 30, "usage": 50, "money": -13.524},
        "18": {"bank": 120.0, "production": 30, "usage": 50, "money": -13.524},
        "19": {"bank": 115.0, "production": 30, "usage": 50, "money": -13.524},
        "20": {"bank": 110.0, "production": 30, "usage": 50, "money": -13.524},
        "21": {"bank": 105.0, "production": 30, "usage": 50, "money": -13.524},
        "22": {"bank": 100.0, "production": 30, "usage": 50, "money": -13.524},
        "23": {"bank": 95.0, "production": 30, "usage": 50, "money": -13.524},
        "24": {"bank": 90.0, "production": 30, "usage": 50, "money": -13.524},
        "25": {"bank": 85.0, "production": 30, "usage": 50, "money": -13.524},
        "26": {"bank": 80.0, "production": 30, "usage": 50, "money": -13.524},
        "27": {"bank": 75.0, "production": 30, "usage": 50, "money": -13.524},
        "28": {"bank": 175.0, "production": 30, "usage": 50, "money": -27.048},
        "29": {"bank": 170.0, "production": 30, "usage": 50, "money": -27.048},
        "30": {"bank": 165.0, "production": 30, "usage": 50, "money": -27.048}
    }
}

day=0
def get_live_data():
    global day
    day+=1
    return [
        house_data["house1"][str(day)],
        house_data["house2"][str(day)],
        house_data["house3"][str(day)],
        house_data["house4"][str(day)]
    ]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def data():
    return jsonify(get_live_data())

if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
 