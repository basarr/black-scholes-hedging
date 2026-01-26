
# Black–Scholes Pricing and Discrete-Time Delta Hedging

## Overview
This repository implements a discrete-time Black–Scholes delta-hedging simulation using historical market data.  
The project was developed as a self-directed extension of my university coursework ("Introduction to Python") to deepen my understanding of option pricing, Greeks, and replication in practice.

Historical price data are sourced from Stooq, and the methodology follows standard delta-replication arguments discussed in academic and practitioner references (e.g. Quant StackExchange).  
The focus is on illustrating how discrete rebalancing, time-varying volatility estimates, and finite hedging intervals generate observable hedging errors relative to the continuous-time Black–Scholes model.

The objective is to show how continuous-time hedging theory translates to practice with discrete rebalancing, estimated volatility, and real price paths.

---

## Model and Assumptions

We consider a **European call option** priced using the Black–Scholes model with the following assumptions:

- Log-normal underlying price dynamics
- Constant risk-free interest rate
- Volatility estimated from historical data
- No dividends or transaction costs
- Discrete-time (daily) delta rebalancing

Estimate volatility using a rolling window of daily log returns, annualized over 252 trading days.

---

## Data

- **Underlying:** SPY (S&P 500 ETF)
- **Frequency:** Daily close prices
- **Source:** Stooq (public CSV download)

Use the closing price as the spot price. Store all raw and processed simulation data in the repository for reproducibility.

---

## Methodology

1. **Volatility Estimation**  
   Compute rolling historical volatility from log returns and treat it as time-varying.

2. **Option Specification**  
   - European call
   - At-the-money at inception
   - Fixed maturity (30 trading days)
   - Constant illustrative risk-free rate

3. **Delta Computation**  
   The Black–Scholes delta is computed analytically at each time step using the current spot price, the remaining time to maturity, and the estimated volatility.

4. **Discrete-Time Delta Hedging**  
   Hedge a short call by buying the Black–Scholes delta in shares, rebalancing the hedge daily, and tracking the cash account with interest.  
   At maturity, the hedging portfolio's value is compared with the option's payoff. The difference represents the hedging error.

---

## Multi-Start Hedging Experiment

Repeat the hedging simulation for multiple start dates, using the same hedge horizon. Show the resulting distribution of hedging errors to highlight discrete rebalancing effects, volatility estimation error, and model misspecification versus realized prices.

The resulting histogram shows that hedging errors are non-zero and spread out, even with textbook delta hedging.

---

## Results and Outputs

The repository provides plots of spot prices, rolling volatility, option prices versus portfolio values, delta over time, cash and share positions, a histogram of hedging errors by start date, and CSV files for all paths and simulation results.

All outputs are generated reproducibly and included in the repository.

---

## Interpretation

This project intentionally produces **non-zero hedging errors**. These errors are not failures, but an explicit illustration of the gap between continuous-time theory and discrete-time implementation with estimated inputs.

The goal is clarity about concepts, not predictive power or trading performance.

---

## Repository Structure
data/
raw/                # raw downloaded price data
processed/          # processed paths and hedging results
figures/              # generated plots
notebooks/01_bs_delta_hedging.ipynb
src/black_scholes.py    # Black–Scholes price and delta functions
---

## Notes

- This project is **educational** and **non-advisory**.
- No trading strategy or performance claims are made.
- The focus is on financial mathematics and risk mechanics.

---

## License
MIT License
