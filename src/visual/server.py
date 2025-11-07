# -*- coding: utf-8 -*-
"""
Simple API Server for Life Finder Map 2.0
Serves computed data (P_life, IELS, δJ, GHZ) to a front-end visualization.
"""

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/data")
def get_data():
    """Return the combined CSV as JSON for visualization."""
    df = pd.read_csv("data/life_map_combined.csv")
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    print("🌍 Serving Life Finder Map data at http://127.0.0.1:8080/data")
    app.run(port=8080, debug=False)
