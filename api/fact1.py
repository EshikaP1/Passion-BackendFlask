from flask import Flask, jsonify, request
import pandas as pd

# class provided by the Flask framework for creating web applications.
app = Flask(__name__)

# Load data from the CSV file
data = pd.read_csv("/home/eneter/vscode/Passion-BackendFlask/api/cancer.csv")

import os

# Get the directory of your Flask app's root
# stores the root directory path of your Flask application.
# This can be useful for various purposes, such as locating templates, static files, or other resources relative to your application's root directory
app_root = os.path.dirname(os.path.abspath(__file__))  # Assuming this code is in your Flask app file

# Create the full path to your CSV file
csv_path = os.path.join(app_root, 'api', 'cancer.csv')

# Load data from the CSV file
data = pd.read_csv(csv_path)


# Define an API endpoint to retrieve data
#when our user promts data, it will redirect here instead of another file. 
@app.route('/api/data', methods=['GET'])
#instead of having a separate file with endpoints, it is creating an enpoint here by using data as a variable
def get_data():
    if data.empty:
        return jsonify({"error": "Data not available"}), 404
    return jsonify(data.to_dict(orient='records'))

# Define an API endpoint to receive state_name from the frontend
@app.route('/backend_endpoint', methods=['POST'])  # Use POST to receive data from the frontend
def process_state_input():
    #since post was used to get data from the frontend, get_json wil retrieve data from the 
    state_data = request.get_json()
    state_name = state_data.get('state_name', '')

    # Perform any processing with state_name here
    # You can use it to filter the data or perform any other task

    # In this example, we'll return a message with the state_name
    return jsonify( "Received state_name:" + (state_name))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8115, debug=True)


