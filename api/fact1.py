from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Load data from the CSV file
csv_file_path = os.environ.get("CSV_FILE_PATH", "cancer.csv")

try:
    data = pd.read_csv(csv_file_path)
except FileNotFoundError:
    data = pd.DataFrame()  # Handle the case where the file is not found

# Define an API endpoint to retrieve data
@app.route('/api/data', methods=['GET'])
def get_data():
    if data.empty:
        return jsonify({"error": "Data not available"}), 404
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

