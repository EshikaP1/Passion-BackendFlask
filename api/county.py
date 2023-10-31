from flask import Flask, Blueprint, jsonify
from flask_restful import Api, Resource
import pandas as pd
from flask_cors import CORS
import os

# Create a Flask application instance
app = Flask(__name__)

county_api = Blueprint('county_api', __name__, url_prefix='/api/data')
api = Api(county_api)

CORS(county_api)

class CountyDataAPI:
    class _Read(Resource):
        def get(self):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'county.csv')
            data = pd.read_csv(csv_path)
            if data.empty:
                return jsonify({"error": "Data not available"}), 404
            return jsonify(data.to_dict(orient='records'))

    class _CountyData(Resource):
        def get(self, county_name):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'county.csv')
            data = pd.read_csv(csv_path)
            county_data = data[(data['County'] == county_name) & (data['Year'] == 2022)]  # Adjust the year as needed
            if county_data.empty:
                return jsonify({"error": "County data not found"}), 404
            result = {
                "State": county_data["State"].values[0],
                "County": county_data["County"].values[0],
                "Year": county_data["Year"].values[0],
                "Days with AQI": county_data["Days with AQI"].values[0],
                "Good Days": county_data["Good Days"].values[0],
                "Moderate Days": county_data["Moderate Days"].values[0],
                "Unhealthy for Sensitive Groups Days": county_data["Unhealthy for Sensitive Groups Days"].values[0],
                "Unhealthy Days": county_data["Unhealthy Days"].values[0],
                "Very Unhealthy Days": county_data["Very Unhealthy Days"].values[0],
                "Hazardous Days": county_data["Hazardous Days"].values[0],
                "Max AQI": county_data["Max AQI"].values[0],
                "90th Percentile AQI": county_data["90th Percentile AQI"].values[0],
                "Median AQI": county_data["Median AQI"].values[0],
                "Days CO": county_data["Days CO"].values[0],
                "Days NO2": county_data["Days NO2"].values[0],
                "Days Ozone": county_data["Days Ozone"].values[0],
                "Days PM2.5": county_data["Days PM2.5"].values[0],
                "Days PM10": county_data["Days PM10"].values[0],
            }
            return jsonify(result)

api.add_resource(CountyDataAPI._Read, '/')
api.add_resource(CountyDataAPI._CountyData, '/county/<string:county_name>')

app.register_blueprint(county_api)

if __name__ == "__main__":
    app.run(debug=True)
