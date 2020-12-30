# textprobar.py

import time
scale = 100
print("-------执行开始-------")
s = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = i
    print("\r{:^3.0f}%[{}>>{}]".format(c,a,b),end="")
    time.sleep(0.1)
    e = time.perf_counter()
    t=e-s
    print("{}s".format(t))
print("\n--------执行结束--------")