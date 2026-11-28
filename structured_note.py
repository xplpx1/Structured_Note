@dataClass(frozen=True)
class AutocallNote:
    notional: float
    maturity: float          # years
    n_obs: int
    coupon_trigger: float    # as fraction of S0, e.g. 0.70
    autocall_trigger: float  # e.g. 1.00
    knock_in_barrier: float  # e.g. 0.65
    coupon_rate: float       # per period, on notional

@property
def check_coupon(self, ti : int) -> bool:
  if self.underlying.spot>self.coupon_trigger:
      return True
    return False

@property
def check_autocall(self, ti : int) -> bool:
  if self.underlying.spot>self.coupon_trigger:
      return True
    return False
