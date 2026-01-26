# black-scholes-hedging
Small financial mathematics side project: BS + Greeks + delta-hedging error analysis

## Project Summary
This repository provides a documented illustration of discrete-time delta hedging for a European call option priced using the Black–Scholes model. The underlying asset is SPY, with historical daily prices used to simulate the hedging path. Volatility is estimated from rolling historical log returns and treated as time-varying, while the option is hedged through daily delta rebalancing. The resulting hedging error is intentionally non-zero, reflecting discrete rebalancing, volatility estimation error, and deviations from Black–Scholes assumptions. The objective is educational: to demonstrate the mechanics and limitations of delta hedging rather than trading performance.
