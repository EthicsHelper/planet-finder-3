# -*- coding: utf-8 -*-
"""
Fractal Galactic Habitable Zone (GHZ) Weighting Function
Implements: A_F(R, z) = exp[-(R/D)^D_f - (|z|/H)^D_f]
"""

import numpy as np

def GHZ_weight(R, z, D=8.0, H=0.3, D_f=1.8):
    """
    Computes the fractal weighting of the Galactic Habitable Zone (GHZ)
    based on radial distance (R) and vertical distance (z).

    Parameters
    ----------
    R : float or ndarray
        Radial distance from galactic center (kpc)
    z : float or ndarray
        Vertical distance from galactic plane (kpc)
    D : float
        Characteristic galactic radius (kpc) — ~8 for Milky Way
    H : float
        Scale height of galactic disk (kpc)
    D_f : float
        Fractal dimension (1.6–2.0 typical for stellar distributions)

    Returns
    -------
    A_F : float or ndarray
        GHZ weighting factor (0–1 range)
    """
    R = np.asarray(R, dtype=float)
    z = np.asarray(z, dtype=float)
    return np.exp(-((R / D) ** D_f) - ((np.abs(z) / H) ** D_f))
