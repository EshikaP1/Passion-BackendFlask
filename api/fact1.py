from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load data from the CSV file
data = pd.read_csv("/home/eneter/vscode/Passion-BackendFlask/api/cancer.csv")

# Define an API endpoint to retrieve data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
