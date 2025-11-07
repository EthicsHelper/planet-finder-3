# -*- coding: utf-8 -*-
"""
Life Probability Function (vΩ_B)
Implements: P_life = exp(-|δJ| / (ħ Ω_A)) × GHZ_weight
"""
import numpy as np
from .omniscientrix_equations import constants_vΩ

def compute_Plife(deltaJ, GHZ):
    """
    Compute the life probability given informational disequilibrium and
    galactic habitable zone weighting.

    Parameters
    ----------
    deltaJ : float or ndarray
        Informational disequilibrium (from δJ = |S/ħ + D_KL - λA|)
    GHZ : float or ndarray
        Galactic Habitable Zone fractal weighting

    Returns
    -------
    P_life : float or ndarray
        Probability (0–1 range) representing informational habitability
    """
    ħ = constants_vΩ["ħ"]
    Ω_A = constants_vΩ["Ω_A"]

    P = np.exp(-np.abs(deltaJ) / (ħ * Ω_A)) * GHZ
    return np.clip(P, 0, 1)
