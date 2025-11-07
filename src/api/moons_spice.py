# -*- coding: utf-8 -*-
"""
Moons and SPICE Integration Module
Fetches major moon ephemerides (Europa, Titan, Ganymede, etc.)
and converts them into compatible dataframes for the Life Finder Map 2.0.
"""

import requests
import pandas as pd

def horizons_fetch(target="502", center="@sun",
                   start="2025-01-01", stop="2025-12-31",
                   step="1 d", format_type="VECTORS"):
    """
    Wrapper around NASA JPL Horizons API for moons.
    Uses NAIF ID codes (e.g., 502=Europa, 606=Titan).

    Parameters
    ----------
    target : str
        NAIF ID for moon (e.g., "502" Europa, "504" Io)
    center : str
        Reference body ("@sun", "@jupiter", etc.)
    start, stop : str
        Date range (YYYY-MM-DD)
    step : str
        Step interval
    format_type : str
        Data format ("VECTORS" or "OBSERVER")

    Returns
    -------
    df : pandas.DataFrame
        Columns: [datetime, x, y, z, vx, vy, vz]
    """

    url = (
        "https://ssd.jpl.nasa.gov/api/horizons.api"
        f"?format=text&TABLE_TYPE={format_type}"
        f"&COMMAND='{target}'&CENTER='{center}'"
        f"&START_TIME='{start}'&STOP_TIME='{stop}'&STEP_SIZE='{step}'"
        "&OUT_UNITS=KM-S&VEC_TABLE=3"
    )

    r = requests.get(url, timeout=60)
    text = r.text

    lines = []
    in_data = False
    for line in text.splitlines():
        if "$$SOE" in line:
            in_data = True
            continue
        if "$$EOE" in line:
            break
        if in_data:
            lines.append(line.strip())

    data = []
    for l in lines:
        parts = [p for p in l.split() if p.replace(".", "", 1).replace("-", "", 1).isdigit()]
        if len(parts) >= 6:
            data.append([float(p) for p in parts[:6]])

    df = pd.DataFrame(data, columns=["x", "y", "z", "vx", "vy", "vz"])
    df["datetime"] = pd.date_range(start=start, periods=len(df), freq="D")
    return df
