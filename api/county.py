from flask import Flask, Blueprint, jsonify, request
from flask_restful import Api, Resource
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__)

county_api = Blueprint('county_api', __name__, url_prefix='/api/data')
api = Api(county_api)

CORS(county_api)

class CountyDataAPI:
    class _Read(Resource):
        def get(self):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'county.csv')  # Update the CSV file name
            data = pd.read_csv(csv_path)
            if data.empty:
                return jsonify({"error": "Data not available"}), 404
            return jsonify(data.to_dict(orient='records'))

    class _Create(Resource):
        def post(self):
            # You can handle the creation of a new entry here if needed
            pass

    class _CountyData(Resource):
        def get(self, county_name):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'county.csv')  # Update the CSV file name
            data = pd.read_csv(csv_path)
            county_data = data[(data['County'] == county_name) & (data['Year'] == 2022)]  # Filter data for the specified county and year
            if county_data.empty:
                return jsonify({"error": "County data not found"}), 404
            result = county_data.to_dict(orient='records')[0]
            return jsonify(result)

api.add_resource(CountyDataAPI._Read, '/')
api.add_resource(CountyDataAPI._Create, '/create')
api.add_resource(CountyDataAPI._CountyData, '/county/<string:county_name>')

app.register_blueprint(county_api)

if __name__ == "__main__":
    app.run(debug=True)
