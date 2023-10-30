from flask import Flask, Blueprint, jsonify
from flask_restful import Api, Resource
import pandas as pd
import os

# Create a Flask application instance
app = Flask(__name__)

#usually refers to the API documentation or specification. 
#This documentation serves as a detailed guide for developers who want to use the API in their applications.
cancer_api = Blueprint('cancer_api', __name__, url_prefix='/api/data')
api = Api(cancer_api)

class CancerDataAPI:
    class _Read(Resource):
        def get(self):
            #determine the directory path of the current Python script or module in which it is placed. 
            #abspath: the absolute path of the current script file. 
            # extract the directory (folder) path from a given file path.
            # using this code enhances portability, maintainability, and collaboration while reducing the risk of errors and security vulnerabilities.
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'cancer.csv')
            data = pd.read_csv(csv_path)
            if data.empty:
                return jsonify({"error": "Data not available"}), 404
            return jsonify(data.to_dict(orient='records'))

    class _Create(Resource):
        def post(self):
            # Here, you can handle the creation of a new entry if needed...this is because we are getting the input from the user(frontend) which is why post is called here and in frontend.
            #create or add new data entries to a resource, such as creating a new object or record in a database.
            # This might involve parsing request data, validating it, and then interacting with a database or performing other relevant operations.
            pass

    class _StateData(Resource):
        def get(self, state_name):
            app_root = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(app_root, 'cancer.csv')
            #reat and get access to the data
            data = pd.read_csv(csv_path)
            #its asking for
            state_data = data[data['State'] == state_name]
            if state_data.empty:
                return jsonify({"error": "State data not found"}), 404
            result = {
                "TotalPopulation": state_data["Total.Population"].values[0],
                "Total amount of death from lung cancer": state_data["Types.Lung.Total"].values[0]
            }
            return jsonify(result)

#This line is defining a route at the root of the API
#This route is typically used to handle POST and GEt requests for creating new data entries.
api.add_resource(CancerDataAPI._Read, '/')
api.add_resource(CancerDataAPI._Create, '/create')
# This dynamic part allows for variable values to be included in the URL
api.add_resource(CancerDataAPI._StateData, '/state/<string:state_name>')

# Register the blueprint with the Flask app
app.register_blueprint(cancer_api)

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode for development
