import numpy as np
import matplotlib.pyplot as plt

x = ['0.5','0.75','1.0','1.0(32)','1.5','2.0']
y = [0.89,0.934,0.933,0.936,0.946,0.955]
plt.figure(figsize=(8,4))
plt.plot(x,y,"b--",linewidth=1)
plt.xlabel("model")
plt.ylabel("accuracy")
plt.show()