import os
from flask import Flask, Blueprint, jsonify
from flask_restful import Api, Resource
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
# ...

class _StateData(Resource):
    def get(self, state_name):
        app_root = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(app_root, 'cancer.csv')
        # Read and get access to the data
        data = pd.read_csv(csv_path)
        state_data = data[data['State'] == state_name]
        if state_data.empty:
            return jsonify({"error": "State data not found"}), 404

        # Sample data (replace with your actual data)
        totalPopulation = 1000000
        totalLungCancerDeaths = 5000

        # Calculate the number of alive people
        alive = totalPopulation - totalLungCancerDeaths

        # Create a pie chart
        labels = ['Alive', 'Lung Cancer Deaths']
        sizes = [alive, totalLungCancerDeaths]
        colors = ['green', 'red']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')  # Equal aspect ratio ensures that the pie chart is drawn as a circle.

        # Save the chart to a file (optional)
        chart_image_path = os.path.join(app_root, 'static', 'pie_chart.png')
        fig.savefig(chart_image_path)

        result = {
            "TotalPopulation": state_data["Total.Population"].values[0],
            "Total amount of death from lung cancer": state_data["Types.Lung.Total"].values[0],
            "PieChartImage": f"/static/pie_chart.png"  # Link to the chart image
        }
        return jsonify(result)
