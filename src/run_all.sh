#!/bin/bash
# Life Finder Map 2.0 — full pipeline runner

echo "🔭 Starting Life Finder Map vΩ pipeline..."

# Step 1 — compute δJ, P_life, GHZ, IELS
echo "⚙️  Running main integration..."
python3 main.py

# Step 2 — launch Flask API for visualization
echo "🌍  Launching data server at http://127.0.0.1:8080/data"
python3 src/visual/server.py
