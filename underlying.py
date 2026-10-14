import numpy as np
import matplotlib as plt

class asset():
  def __init__(self, spot_init: float, vol : float, risk-free-rate : float, dividend_yield : float) -> None:
    self._spot_init = spot_init
    self._spot=spot_init
    self._vol=vol
    self._rf_rate=risk-free-rate
    self._dividend_yield=dividend_yield

  def get_vol(self) -> float:
    return vol

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

  def update(self, T : int) -> None:
    rng = np.random.default_rng(1)
    Z = rng.standard_normal(1000)
    S = self._spot_init*np.exp( (self._rf_rate-self._dividend_yield - self._vol**2/2) * T + self._vol*np*sqrt(T)*Z)
    self._spot = S.mean()

test = asset(100,0.3,0.05,0.02)
Time = np.array(i for i in range(1000))
Y = np.array()
Y[0]=test.get_spot()
for i in range(1,1000):
  test.update(i)
  Y[i]=test.get_spot()
plt.plot(Time, Y)
plt.grid()
plt.show()

