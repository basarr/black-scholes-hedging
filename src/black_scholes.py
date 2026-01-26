import math


def _norm_cdf(x: float) -> float:
    """Standard normal CDF using error function."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _d1(S: float, K: float, r: float, sigma: float, T: float) -> float:
    return (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))


def _d2(S: float, K: float, r: float, sigma: float, T: float) -> float:
    return _d1(S, K, r, sigma, T) - sigma * math.sqrt(T)


def bs_call_price(S: float, K: float, r: float, sigma: float, T: float) -> float:
    """
    Black–Scholes European call price.
    Inputs:
      S: spot
      K: strike
      r: continuously-compounded risk-free rate
      sigma: annualized volatility
      T: time to maturity in years
    """
    if T <= 0:
        return max(S - K, 0.0)
    if sigma <= 0:
        # deterministic limit: discounted intrinsic under risk-neutral drift is not modeled here;
        # use intrinsic as a simple guardrail for the illustration.
        return max(S - K, 0.0)

    d1 = _d1(S, K, r, sigma, T)
    d2 = _d2(S, K, r, sigma, T)
    return S * _norm_cdf(d1) - K * math.exp(-r * T) * _norm_cdf(d2)


def bs_call_delta(S: float, K: float, r: float, sigma: float, T: float) -> float:
    """Black–Scholes European call delta."""
    if T <= 0:
        return 1.0 if S > K else 0.0
    if sigma <= 0:
        return 1.0 if S > K else 0.0

    d1 = _d1(S, K, r, sigma, T)
    return _norm_cdf(d1)
