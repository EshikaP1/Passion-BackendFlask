from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/pie-chart-data', methods=['GET'])
def get_pie_chart_data():
    # Read the CSV file
    data = pd.read_csv('construction_spending.csv')
    # Perform any data processing as needed
    # For simplicity, let's assume you want to retrieve data for a specific year (e.g., 2002).
    year_data = data[data['time.year'] == 2002]

    # Format the data as needed for the pie chart
    # You need to extract data relevant to the pie chart and format it properly.
    pie_chart_data = {
        'labels': ['Category 1', 'Category 2', 'Category 3'],  # Example labels
        'data': [100, 200, 300]  # Example data
    }

    return jsonify(pie_chart_data)

if __name__ == '__main__':
    app.run()
