"""
black_scholes.py
----------------
Pricing and Greeks calculations for European options using the Black-Scholes model.
"""

import numpy as np
from scipy.stats import norm  # Normal distribution for CDF/PDF


# --- Helper functions for Black-Scholes ---
def d1(S, K, T, r, sigma):
    """
    Computes d1 used in Black-Scholes formulas.
    """
    S = np.array(S, dtype=float)           # Ensure S is a float array
    sigma = np.maximum(sigma, 1e-10)       # Prevent zero volatility
    T = np.maximum(T, 1e-10)               # Prevent zero time

    return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))


def d2(S, K, T, r, sigma):
    """
    Computes d2 used in Black-Scholes formulas.
    """
    return d1(S, K, T, r, sigma) - sigma * np.sqrt(T)


# --- Option Price ---
def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    """
    Returns European call or put option price.
    """
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)

    if option_type == 'call':
        return S * norm.cdf(D1) - K * np.exp(-r * T) * norm.cdf(D2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-D2) - S * norm.cdf(-D1)


# --- Greeks ---

def delta(S, K, T, r, sigma, option_type='call'):
    """
    Measures sensitivity of option price to stock price.
    """
    D1 = d1(S, K, T, r, sigma)
    if option_type == 'call':
        return norm.cdf(D1)        # Call delta: 0 → 1
    else:
        return norm.cdf(D1) - 1    # Put delta: -1 → 0


def gamma(S, K, T, r, sigma):
    """
    Measures rate of change of delta with stock price.
    """
    D1 = d1(S, K, T, r, sigma)
    return norm.pdf(D1) / (S * sigma * np.sqrt(T))


def vega(S, K, T, r, sigma):
    """
    Measures sensitivity of option price to volatility (per 1% change).
    """
    D1 = d1(S, K, T, r, sigma)
    return S * norm.pdf(D1) * np.sqrt(T) / 100


def theta(S, K, T, r, sigma, option_type='call'):
    """
    Measures time decay of option price (per day).
    """
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)

    first_term = -S * norm.pdf(D1) * sigma / (2 * np.sqrt(T))  # Impact of volatility

    if option_type == 'call':
        second_term = -r * K * np.exp(-r * T) * norm.cdf(D2)   # Impact of interest rate
    else:
        second_term = r * K * np.exp(-r * T) * norm.cdf(-D2)

    return (first_term + second_term) / 365  # Convert to daily decay


def rho(S, K, T, r, sigma, option_type='call'):
    """
    Measures sensitivity of option price to risk-free interest rate (per 1% change).
    """
    D2 = d2(S, K, T, r, sigma)

    if option_type == 'call':
        return K * T * np.exp(-r * T) * norm.cdf(D2) / 100
    else:
        return -K * T * np.exp(-r * T) * norm.cdf(-D2) / 100
