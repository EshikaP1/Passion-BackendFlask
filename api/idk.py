from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Get the directory of your Flask app's root
app_root = os.path.dirname(os.path.abspath(__file__))  # Assuming this code is in your Flask app file

# Create the full path to your CSV file in the 'api' directory
csv_path = os.path.join(app_root, 'api', 'cancer.csv')

# Load data from the CSV file
data = pd.read_csv(csv_path)

# Define an API endpoint to retrieve data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
