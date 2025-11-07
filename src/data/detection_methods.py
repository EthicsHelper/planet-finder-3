# -*- coding: utf-8 -*-
"""
Detection Layer — Informational Earth-Likeness Score (IELS)
Implements a simplified multi-sensor IELS weighting model.
Each method (spectral, magnetic, infrared) modifies D_KL and habitability.
"""

import numpy as np

def detection_score(df):
    """
    Combine multiple detection modalities into one unified IELS score.

    Parameters
    ----------
    df : pandas.DataFrame
        Must contain δJ, vx, vy, vz (velocity or environmental parameters)

    Returns
    -------
    IELS : ndarray
        0–1 score expressing Earth-likeness probability
    """

    # Spectroscopic / photometric coherence
    spectral = np.exp(-np.abs(df["δJ"]) * 1e2)

    # Magnetic field balance proxy (vx component)
    magnetic = np.exp(-np.abs(df["vx"].astype(float)) * 1e-3)

    # Infrared or atmospheric uniformity proxy (vy component)
    infrared = np.exp(-np.abs(df["vy"].astype(float)) * 1e-3)

    # Weighted composite (normalized)
    IELS = 0.33 * (spectral + magnetic + infrared)
    return np.clip(IELS, 0, 1)
