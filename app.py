import streamlit as st  # Streamlit for web app UI
import numpy as np       # NumPy for numerical calculations
import plotly.graph_objs as go  # Plotly for interactive plots
from black_scholes import black_scholes_price, delta, gamma, vega, theta, rho  # Black-Scholes functions

# --- Page Configuration ---
st.set_page_config(
    page_title="Black-Scholes Visual Explainer",  # Title of the app
    layout="wide",                                # Wide layout for full-screen plots
    initial_sidebar_state="expanded",            # Sidebar open by default
    page_icon="💹"                                # Page icon
)

# --- Sidebar Controls for Input Parameters ---
st.sidebar.title("Controls")
st.sidebar.markdown("---")

# Slider inputs for model parameters
S = st.sidebar.slider("Stock Price (S)", 10, 300, 100, 1)          # Current stock price
K = st.sidebar.slider("Strike Price (K)", 10, 300, 100, 1)         # Strike price
sigma = st.sidebar.slider("Volatility (σ, %)", 1, 100, 20, 1) / 100  # Volatility as decimal
T = st.sidebar.slider("Time to Maturity (T, years)", 1, 365, 30, 1) / 365  # Time in years
r = st.sidebar.slider("Risk-Free Rate (r, %)", 0, 15, 2, 1) / 100  # Risk-free interest rate
option_type = st.sidebar.radio("Option Type", ["call", "put"], horizontal=True)  # Call or put option

st.markdown("---")  # Visual separator

# --- 3D Surface Plot of Option Price vs S & Volatility ---
S_range = np.linspace(10, 300, 40)        # Stock price range
sigma_range = np.linspace(0.01, 1, 40)    # Volatility range
S_grid, sigma_grid = np.meshgrid(S_range, sigma_range)  # Create 2D grids

# Compute Black-Scholes price for each combination
price_grid = black_scholes_price(S_grid, K, T, r, sigma_grid, option_type)

# Create a 3D surface plot
surface = go.Surface(
    x=S_range,
    y=sigma_range * 100,  # Convert to percentage for display
    z=price_grid,
    colorscale='Viridis',
    showscale=True,
    opacity=0.95
)

# Layout styling for 3D plot
layout = go.Layout(
    title=f"{option_type.capitalize()} Price Surface",
    scene=dict(
        xaxis_title='Stock Price (S)',
        yaxis_title='Volatility (%)',
        zaxis_title='Option Price',
        bgcolor='#181818',  # Dark background
    ),
    paper_bgcolor='#181818',
    font=dict(color='white'),
    margin=dict(l=0, r=0, b=0, t=40)
)

fig3d = go.Figure(data=[surface], layout=layout)
st.plotly_chart(fig3d, use_container_width=True)  # Display 3D plot

# --- 2D Plot of Delta vs Stock Price ---
delta_curve = [delta(s, K, T, r, sigma, option_type) for s in S_range]  # Compute delta

fig2d = go.Figure()
fig2d.add_trace(
    go.Scatter(
        x=S_range,
        y=delta_curve,
        mode='lines',
        line=dict(color='#00f2fe', width=4)
    )
)

# Layout styling for 2D plot
fig2d.update_layout(
    title="Delta vs Stock Price",
    xaxis_title="Stock Price (S)",
    yaxis_title="Delta",
    plot_bgcolor='#181818',
    paper_bgcolor='#181818',
    font=dict(color='white'),
    margin=dict(l=40, r=40, b=40, t=40)
)

st.plotly_chart(fig2d, use_container_width=True)  # Display 2D delta plot

# --- Footer ---
st.markdown("""
<div style='text-align:center; color:#888; font-size:1.1em;'>
  <b>Black-Scholes Visual Explainer</b> — Powered by Streamlit, Plotly, NumPy, SciPy
</div>
""", unsafe_allow_html=True)
