from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

# Load data from the CSV file
<<<<<<< HEAD
data = pd.read_csv("/home/eneter/vscode/Passion-BackendFlask/api/cancer.csv")
#get the input from frontend
data = request.get_json()
state_name = data.get('state_name', '')

column_data = data[state_name]
=======
csv_file_path = os.environ.get("CSV_FILE_PATH", "cancer.csv")

try:
    data = pd.read_csv(csv_file_path)
except FileNotFoundError:
    data = pd.DataFrame()  # Handle the case where the file is not found

>>>>>>> 7cb285f12a64ad129bb6f1c62dd8d68190adef93
# Define an API endpoint to retrieve data
@app.route('/api/data', methods=['GET'])
def get_data():
    if data.empty:
        return jsonify({"error": "Data not available"}), 404
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000, debug=True)
=======
    app.run(debug=True)
>>>>>>> 7cb285f12a64ad129bb6f1c62dd8d68190adef93

