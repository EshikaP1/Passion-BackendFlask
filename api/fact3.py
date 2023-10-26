from flask import Flask, Blueprint, jsonify
from flask_restful import Api, Resource
import pandas as pd
import os

# Create a Flask application instance
app = Flask(__name__)

cancer_api = Blueprint('cancer_api', __name__, url_prefix='/api/data')
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

# Register the blueprint with the Flask app
app.register_blueprint(cancer_api)

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode for development
