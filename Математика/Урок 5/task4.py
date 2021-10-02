import numpy as np
import itertools

for p in itertools.product("0123456789",repeat = 666):
    print(f"да, будет не быстро :D {''.join(p)}")