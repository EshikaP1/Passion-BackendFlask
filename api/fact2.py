from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import pandas as pd
import os
import requests

cancer_api = Blueprint('cancer_api', __name__,
                       url_prefix='/api/data')

api = Api(cancer_api)

class CancerDataAPI:
    class _Read(Resource):
        def get(self):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'cancer.csv')
            data = pd.read_csv(csv_path)
            if data.empty:
                return jsonify({"error": "Data not available"}), 404
            return jsonify(data.to_dict(orient='records'))

    class _Create(Resource):
        def post(self):
            # Here, you can handle the creation of a new entry if needed
            pass

    class _StateData(Resource):
        def get(self, state_name):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'cancer.csv')
            data = pd.read_csv(csv_path)
            state_data = data[data['State'] == state_name]
            if state_data.empty:
                return jsonify({"error": "State data not found"}), 404
            result = {
                "TotalPopulation": state_data["Total.Population"].values[0],
                "LungTotal": state_data["Types.Lung.Total"].values[0]
            }
            return jsonify(result)

api.add_resource(CancerDataAPI._Read, '/')
api.add_resource(CancerDataAPI._Create, '/create')
api.add_resource(CancerDataAPI._StateData, '/state/<string:state_name>')

if __name__ == "__main__":
    # Modify your test code as needed
    server = "https://cancer0.stu.nighthawkcodingsociety.com/"  # Replace with your server URL
    url = server + "/api/data"
    responses = []  # Responses list

    # Test code
    # Modify the following code according to your test scenario
    responses.append(
        requests.get(url)  # Read cancer data
    )
    responses.append(
        requests.post(url + "/create")  # Create new data (if needed)
    )

    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("Unknown error")