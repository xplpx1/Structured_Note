import numpy as np
import matplotlib.pyplot as plt

class asset():
  def __init__(self, spot_init: float, vol : float, risk_free_rate : float, dividend_yield : float) -> None:
    self._spot_init = spot_init
    self._spot=spot_init
    self._vol=vol
    self._rf_rate=risk_free_rate
    self._dividend_yield=dividend_yield

  def get_vol(self) -> float:
    return self._vol

  def get_spot_init(self) -> float:
    return self._spot_init

  def get_spot(self) -> float:
    return self._spot

  def get_rf_rate(self) -> float:
    return self._rf_rate

  def get_dividend_yield(self) -> float:
    return self._dividend_yield

#  def modify_spot(self, new_spot : float) -> None:
 #   self._spot = new_spot

  def update(self, dT : int) -> None:
    Z = np.random.standard_normal()
    S = self._spot*np.exp( (self._rf_rate-self._dividend_yield - self._vol**2/2) * dT + self._vol*np.sqrt(dT)*Z)
    self._spot = S

