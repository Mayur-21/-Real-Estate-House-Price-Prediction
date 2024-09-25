from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_locations_names', methods=['GET'])
def get_locations_names():
    util.load_saved_artifacts()
    response = jsonify({
        'locations': util.get_locations_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    util.load_saved_artifacts()
    util.get_locations_names()
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = float(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting python flask ")
    app.run()
