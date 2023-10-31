from flask import Flask, Blueprint, jsonify
from flask_restful import Api, Resource
import pandas as pd
from flask_cors import CORS
import os

# Create a single Flask application
app = Flask(__name__)

# Create a blueprint for the first API
county_api = Blueprint('county_api', __name__, url_prefix='/api/data/county')
api_county = Api(county_api)

CORS(county_api)

class CountyDataAPI:
    class _Read(Resource):
        def get(self):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'county.csv')
            data_county = pd.read_csv(csv_path)
            if data_county.empty:
                return jsonify({"error": "Data not available"}), 404
            return jsonify(data_county.to_dict(orient='records'))

    class _Create(Resource):
        def post(self):
            # Handle the creation of a new entry here if needed
            pass

    class _CountyData(Resource):
        def get(self, county_name):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'county.csv')
            data_county = pd.read_csv(csv_path)
            county_data = data_county[(data_county['County'] == county_name) & (data_county['Year'] == 2022)]
            if county_data.empty:
                return jsonify({"error": "County data not found"}), 404
            result = county_data.to_dict(orient='records')[0]
            return jsonify(result)

# Define routes for the first API under the same application
api_county.add_resource(CountyDataAPI._Read, '/county')
api_county.add_resource(CountyDataAPI._Create, '/county/create')
api_county.add_resource(CountyDataAPI._CountyData, '/county/<string:county_name>')

# Create a blueprint for the second API
cancer_api = Blueprint('cancer_api', __name__, url_prefix='/api/data/cancer')
api_cancer = Api(cancer_api)

CORS(cancer_api)

class CancerDataAPI:
    class _Read(Resource):
        def get(self):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'cancer.csv')
            # Modify your route for the Cancer API's state data as follows:
            api_cancer.add_resource(CancerDataAPI._StateData, '/state/<string:state_name>')
            data_cancer = pd.read_csv(csv_path)
            if data_cancer.empty:
                return jsonify({"error": "Data not available"}), 404
            return jsonify(data_cancer.to_dict(orient='records'))

    class _Create(Resource):
        def post(self):
            # Handle the creation of a new entry here if needed
            pass

    class _StateData(Resource):
        def get(self, state_name):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'cancer.csv')
            data_cancer = pd.read_csv(csv_path)
            state_data = data_cancer[data_cancer['State'] == state_name]
            if state_data.empty:
                return jsonify({"error": "State data not found"}), 404
            result = {
                "TotalPopulation": state_data["Total.Population"].values[0],
                "Total amount of death from lung cancer": state_data["Types.Lung.Total"].values[0],
            }
            return jsonify(result)

# Define routes for the second API under the same application
api_cancer.add_resource(CancerDataAPI._Read, '/cancer')
api_cancer.add_resource(CancerDataAPI._Create, '/cancer/create')
api_cancer.add_resource(CancerDataAPI._StateData, '/cancer/state/<string:state_name>')

# Register both blueprints with the same Flask app
app.register_blueprint(county_api)
app.register_blueprint(cancer_api)

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Run the combined app on the same port
