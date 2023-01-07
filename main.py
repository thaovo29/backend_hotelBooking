from flask import Flask 
from flask import request, jsonify
import json


app = Flask(__name__)

def obj_dict(obj):
    return obj.__dict__
    
@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        f = open('accounts.json', 'r')
        print(123)
        data = json.load(f)
        lst = list(data)
        lst.append(
            {
                "username": username,
                "email": email,
                "password": password
            }
        )
        lstObject = json.dumps(lst)
        with open('accounts.json','w') as w:
            w.write(lstObject)
        return jsonify({"response": "success"})
    
@app.route('/getHotelByPlace', methods = ['POST'])
def getHotelById():
    if request.method == 'POST':
        place = request.form["place"]
        f = open('HotelList.json', 'r')
        data = json.load(f)
        for room in data:
            if place in room["address"]:
                return jsonify(room)
        return jsonify({"response": "fall to seek"})
    
    
@app.route('/getResortByPlace', methods = ['POST'])
def getResortById():
    if request.method == 'POST':
        place = request.form["place"]
        f = open('ResortList.json', 'r')
        data = json.load(f)
        for room in data:
            if place in room["address"]:
                return jsonify(room)
        return jsonify({"response": "fall to seek"})
    
@app.route('/getApartmentByPlace', methods = ['POST'])
def getApartmentById():
    if request.method == 'POST':
        place = request.form["place"]
        f = open('ApartmentList.json', 'r')
        data = json.load(f)
        for room in data:
            if place in room["address"]:
                return jsonify(room)
        return jsonify({"response": "fall to seek"})
    
@app.route('/getHomestayByPlace', methods = ['POST'])
def getHomestayById():
    if request.method == 'POST':
        place = request.form["place"]
        f = open('HomestayList.json', 'r')
        data = json.load(f)
        for room in data:
            if place in room["address"]:
                return jsonify(room)
        return jsonify({"response": "fall to seek"})
    
@app.route('/getHotelList', methods = ['GET'])
def getHotelList():
    if request.method == 'GET':
        f = open('HotelList.json', 'r')
        data = json.load(f)
        return jsonify(data)
    
@app.route('/getApartmentList', methods = ['GET'])
def getApartmentList():
    if request.method == 'GET':
        f = open('ApartmentList.json', 'r')
        data = json.load(f)
        return jsonify(data)
    
@app.route('/getResortList', methods = ['GET'])
def getResortList():
    if request.method == 'GET':
        f = open('ResortList.json', 'r')
        data = json.load(f)
        return jsonify(data)
    
@app.route('/getHomestayList', methods = ['GET'])
def getHomestayList():
    if request.method == 'GET':
        f = open('HomestayList.json', 'r')
        data = json.load(f)
        return jsonify(data)
    
@app.route('/getDiscoverList', methods=['GET'])
def getDiscoverList():
    if request.method == 'GET':
        f = open('discoverMoreList.json', 'r')
        data = json.load(f)
        return data


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)