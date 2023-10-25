from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

# Get the directory of your Flask app's root
app_root = os.path.dirname(os.path.abspath(__file__))

# Create the full path to your CSV file
csv_path = os.path.join(app_root, 'cancer.csv')

# Load data from the CSV file
data = pd.read_csv(csv_path)

# Define an API endpoint to retrieve data
@app.route('/api/data', methods=['GET'])
def get_data(): 
    if data.empty:
        return jsonify({"error": "Data not available"}), 404
    return jsonify(data.to_dict(orient='records'))

# Define an API endpoint to receive state_name from the frontend
@app.route('/backend_endpoint', methods=['POST'])
def process_state_input():
    state_data = request.get_json()
    state_name = state_data.get('state_name', '')

    # Perform any processing with state_name here
    # You can use it to filter the data or perform any other task

    # In this example, we'll return a message with the state_name
    return jsonify({"message": "Received state_name: " + state_name})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8115, debug=True)
