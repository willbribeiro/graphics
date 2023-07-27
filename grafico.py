import matplotlib.pyplot as plt
import numpy as np

plt.style.use('willian_origin.mplstyle')

# LINE PLOT
# x_data = np.arange(0, 50, 0.01)
# y_data = np.sin(x_data)
# y_data2 = np.cos(x_data)
# plt.plot(x_data, y_data, label='sin')
# plt.plot(x_data, y_data2, label='cos')
# plt.xlabel('time')
# plt.ylabel('Temperature')
# plt.legend()

# SCATTER PLOT
# x_data = [1, 2, 3, 4]
# y_data = [1, 4, 9, 16]
# plt.scatter(x_data, y_data)

# ERRORBAR PLOT
# x = ("NR", "NR/CB", "NR/BIO")
# y = (15.9, 25.4, 15.2)
# y_error = (2, 4, 6)
# plt.errorbar(x, y, y_error)

# HISTOGRAM PLOT
# np.random.seed(19680801)
# mu = 100 # mean of distribution
# sigma = 15 # standard deviation of distribution
# x = mu + sigma * np.random.randn(437)
# plt.hist(x)

# BOXPLOT
# np.random.seed(19680801)
# all_data = [np.random.normal(0, std, size=100) for std in range (1, 4)]
# labels =  ['x1', 'x2', 'x3']
# plt.boxplot(all_data, labels=labels)

plt.show()
