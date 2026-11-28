import numpy as np
import matplotlib.pyplot as plt

@dataclass(frozen=True)
class asset():
    spot: array[float]
    vol: float
    risk_free_rate: float
    dividend_yield: float

#  def modify_spot(self, new_spot : float) -> None:
 #   self._spot = new_spot

def simulate(self, times, n_paths, rng) -> np.ndarray: 
    '''times is a list of times when we update the spot price of the underlying.'''
        dt = np.diff(np.concatenate([[0.0], np.asarray(times, dtype=float)])) #The differences in time between observation dates. !dimensional array
        drift = (self.risk_free_rate - self.dividend_yield - 0.5 * self.vol**2) * dt
        diff = self.vol * np.sqrt(dt) * rng.standard_normal((n_paths, len(dt)))
        return self.spot * np.exp(np.cumsum(drift + diff, axis=1))
    

