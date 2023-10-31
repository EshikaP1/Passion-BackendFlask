from flask import Flask, Blueprint, jsonify
from flask_restful import Api, Resource
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__)

cancer_api = Blueprint('cancer_api', __name__, url_prefix='/api/data')
api = Api(cancer_api)

CORS(cancer_api)

class CancerDataAPI:
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

    class _StateData(Resource):
        def get(self, state_name):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'county.csv')  # Update the CSV file name
            data = pd.read_csv(csv_path)
            state_data = data[(data['State'] == state_name) & (data['Year'] == 2022)]  # Filter data for the specified state and year
            if state_data.empty:
                return jsonify({"error": "State data not found"}), 404
            result = {
                "State": state_data['State'].values[0],
                "County": state_data['County'].values[0],
                "Year": state_data['Year'].values[0],
                "Days with AQI": state_data['Days with AQI'].values[0],
                "Good Days": state_data['Good Days'].values[0],
                "Moderate Days": state_data['Moderate Days'].values[0],
                "Unhealthy for Sensitive Groups Days": state_data['Unhealthy for Sensitive Groups Days'].values[0],
                "Unhealthy Days": state_data['Unhealthy Days'].values[0],
                "Very Unhealthy Days": state_data['Very Unhealthy Days'].values[0],
                "Hazardous Days": state_data['Hazardous Days'].values[0],
                "Max AQI": state_data['Max AQI'].values[0],
                "90th Percentile AQI": state_data['90th Percentile AQI'].values[0],
                "Median AQI": state_data['Median AQI'].values[0],
                "Days CO": state_data['Days CO'].values[0],
                "Days NO2": state_data['Days NO2'].values[0],
                "Days Ozone": state_data['Days Ozone'].values[0],
                "Days PM2.5": state_data['Days PM2.5'].values[0],
                "Days PM10": state_data['Days PM10'].values[0]
            }
            return jsonify(result)

api.add_resource(CancerDataAPI._Read, '/')
api.add_resource(CancerDataAPI._Create, '/create')
api.add_resource(CancerDataAPI._StateData, '/state/<string:state_name>')

app.register_blueprint(cancer_api)

if __name__ == "__main__":
    app.run(debug=True)
