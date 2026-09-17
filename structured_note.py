class Structured_Note:
  def __init__(self, notional: int, time_end: int, obs_numb: int, current_t: int, coup_barrier: int, autocall: int, knock_in: int, coupon_rate: int, underlying: asset):
    self.N = notional
    self.T= time_end
    self.n=obs_numb
    self.C=coup_barrier
    self.A=autocall
    self.B=knock_in
    self.c=coupon_rate
    self.t = current_t

  def check_coupon(self):
    if asset_value
    
