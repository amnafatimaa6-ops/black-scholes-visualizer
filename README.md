# black-scholes-visualizer
# Black-Scholes Visual Explainer 

A **visual interactive explorer** for European options using the **Black-Scholes model**.  
This app allows you to explore **option prices and Greeks** with sliders for stock price, strike price, volatility, time to maturity, and risk-free rate. 
## Quick Summary

The **Black-Scholes model** is a mathematical tool used to calculate the **fair price of an option** — a contract that lets you buy or sell a stock at a fixed price in the future.  

- **Call Option:** Right to buy  
- **Put Option:** Right to sell  

This app lets you **see how an option’s price changes** depending on:  
- Stock price  
- Volatility (how much the price jumps up or down)  
- Time until the option expires  
- Interest rates  

It also shows **Greeks** — measures of how sensitive the option is to different market factors.  

Think of it like a **weather map for option prices**: you can watch how different “conditions” affect the value. 🌤️💹

---
## Live Demo
You can interact with the 3D option price surface here:  
[Open the live Streamlit app](https://black-scholes-visualizer-7aqzzbba7xqckn9idywp7w.streamlit.app/)

---

## 🖼 Screenshots

### 3D Option Price Surface


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
