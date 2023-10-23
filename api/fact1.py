from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load data from the CSV file
data = pd.read_csv("/home/eneter/vscode/Passion-BackendFlask/api/cancer.csv")
#get the input from frontend
data = request.get_json()
state_name = data.get('state_name', '')

column_data = data[state_name]
# Define an API endpoint to retrieve data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

