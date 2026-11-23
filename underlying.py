import numpy as np
import matplotlib.pyplot as plt

@dataclass(frozen=True)
class asset():
    spot: float
    vol: float
    risk_free_rate: float
    dividend_yield: float

#  def modify_spot(self, new_spot : float) -> None:
 #   self._spot = new_spot

  def update(self, times: np.array,) -> np.ndarray:
    Z = np.random.standard_normal()
    S = self._spot*np.exp( (self._rf_rate-self._dividend_yield - self._vol**2/2) * dT + self._vol*np.sqrt(dT)*Z)
    self._spot = S
    

