import matplotlib.pyplot as plt
import numpy as np

plt.style.use('willian_origin.mplstyle')

x_data = np.arange(0, 50, 0.01)
y_data = np.sin(x_data)
y_data2 = np.cos(x_data)

plt.plot(x_data, y_data, label='seno')
plt.plot(x_data, y_data2, label='cosseno')
plt.xlabel('tempo')
plt.ylabel('Temperatura')
plt.legend()
plt.show()
