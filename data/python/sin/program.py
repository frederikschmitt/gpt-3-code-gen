import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 4 * np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y, color=np.random.rand(3,))
plt.show()