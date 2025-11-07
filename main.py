# -*- coding: utf-8 -*-
"""
Life Finder Map 2.0 — Core Integration
Unifies δJ computation, life probability, GHZ weighting, IELS scoring,
and Horizons + SPICE datasets into one coherent framework.
"""

import pandas as pd
from src.api.horizons_planets import fetch_horizons
from src.api.moons_spice import horizons_fetch
from src.core.omniscientrix_equations import deltaJ_field
from src.core.life_probability import compute_Plife
from src.core.ghz_weight import GHZ_weight
from src.data.detection_methods import detection_score

# === STEP 1: Fetch planetary and moon data ===
print("Fetching NASA Horizons planetary data...")
earth = fetch_horizons("earth", "@sun", "2025-01-01", "2025-02-01", "1 d")
mars = fetch_horizons("mars", "@sun", "2025-01-01", "2025-02-01", "1 d")
europa = horizons_fetch("502", "@jupiter", "2025-01-01", "2025-02-01", "1 d")

# === STEP 2: Compute δJ for each ===
print("Computing informational disequilibrium (δJ)...")
earth["δJ"] = deltaJ_field(S_env=earth["x"], D_KL=abs(earth["vx"]), A_env=abs(earth["vy"]))
mars["δJ"] = deltaJ_field(S_env=mars["x"], D_KL=abs(mars["vx"]), A_env=abs(mars["vy"]))
europa["δJ"] = deltaJ_field(S_env=europa["x"], D_KL=abs(europa["vx"]), A_env=abs(europa["vy"]))

# === STEP 3: Apply GHZ weighting ===
print("Applying GHZ fractal weighting...")
earth["GHZ"] = GHZ_weight(earth["x"], earth["z"])
mars["GHZ"] = GHZ_weight(mars["x"], mars["z"])
europa["GHZ"] = GHZ_weight(europa["x"], europa["z"])

# === STEP 4: Compute Life Probability ===
print("Calculating Life Probability (P_life)...")
earth["P_life"] = compute_Plife(earth["δJ"], earth["GHZ"])
mars["P_life"] = compute_Plife(mars["δJ"], mars["GHZ"])
europa["P_life"] = compute_Plife(europa["δJ"], europa["GHZ"])

# === STEP 5: Compute Informational Earth-Likeness Score (IELS) ===
print("Computing IELS (Informational Earth-Likeness Score)...")
earth["IELS"] = detection_score(earth)
mars["IELS"] = detection_score(mars)
europa["IELS"] = detection_score(europa)

# === STEP 6: Combine datasets ===
combined = pd.concat([earth.assign(body="Earth"),
                      mars.assign(body="Mars"),
                      europa.assign(body="Europa")],
                      ignore_index=True)

# === STEP 7: Export ===
output_path = "data/life_map_combined.csv"
combined.to_csv(output_path, index=False)
print(f"✅ Life Finder Map data exported → {output_path}")

# === STEP 8: Display summary ===
summary = combined.groupby("body")[["P_life", "IELS"]].mean()
print("\nAverage habitability indicators:")
print(summary)
