# black-scholes-visualizer
# Black-Scholes Visual Explainer 

A **visual interactive explorer** for European options using the **Black-Scholes model**.  
This app allows you to explore **option prices and Greeks** with sliders for stock price, strike price, volatility, time to maturity, and risk-free rate.  

---
## Live Demo
You can interact with the 3D option price surface here:  
[Open the live Streamlit app](https://black-scholes-visualizer-7aqzzbba7xqckn9idywp7w.streamlit.app/)

---

## 🖼 Screenshots

### 3D Option Price Surface
![3D Plot](3d_plot.png)

### Delta vs Stock Price
*(Add screenshot of delta plot here if you have one)*

---

##  Features

- **Interactive 3D Price Surface:** Stock price vs Volatility vs Option price  
- **2D Greeks plots:** Delta, Gamma, Vega, Theta, Rho  
- Adjust parameters in real-time using sliders:  
  - Stock Price (S)  
  - Strike Price (K)  
  - Volatility (σ)  
  - Time to Maturity (T)  
  - Risk-Free Rate (r)  
  - Option Type (Call / Put)  

---
##  Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/your-username/black-scholes-visualizer.git
cd black-scholes-visualizer
pip install streamlit numpy scipy plotly
