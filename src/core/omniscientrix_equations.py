# -*- coding: utf-8 -*-
"""
Omniscientrix Core Equations (vΩ)
Defines constants and fundamental δJ computation used across all modules.
"""

import numpy as np

# === Fundamental constants ===
constants_vΩ = {
    "ħ": 1.054e-34,     # Reduced Planck constant (J·s)
    "λ": 1e-36,         # Awareness coupling constant (baseline)
    "Ω_A": 7.83,        # Schumann-like awareness frequency (Hz)
}

# === Core δJ (informational disequilibrium) ===
def deltaJ_field(S_env, D_KL, A_env, λ=None, ħ=None):
    """
    Computes informational disequilibrium:
        δJ = |S_env/ħ + D_KL - λ·A_env|

    Parameters
    ----------
    S_env : float or array
        Environmental action term (energy/awareness field)
    D_KL : float or array
        Informational divergence between observed and equilibrium states
    A_env : float or array
        Environmental awareness / coherence index
    λ : float
        Awareness coupling constant (defaults to constants_vΩ["λ"])
    ħ : float
        Planck constant (defaults to constants_vΩ["ħ"])

    Returns
    -------
    δJ : float or ndarray
        Magnitude of informational disequilibrium
    """
    if λ is None:
        λ = constants_vΩ["λ"]
    if ħ is None:
        ħ = constants_vΩ["ħ"]

    return np.abs(S_env / ħ + D_KL - λ * A_env)
