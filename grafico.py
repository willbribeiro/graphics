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

# CONTOUR PLOTS
# delta = 0.025
# x = np.arange(-3.0, 3.0, delta)
# y = np.arange(-2.0, 2.0, delta)
# X, Y = np.meshgrid(x, y)
# Z1 = np.exp(-X**2 - Y**2)
# Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
# Z = (Z1 - Z2) * 2

# fig, ax = plt.subplots()
# CS = ax.contour(X, Y, Z)
# ax.clabel (CS, inline=True)
# ax.set_title('Simplest default with labels')

# LATEX
# Enter raw data
# aluminum = np.array([6.4e-5, 3.01e-5, 2.36e-5, 3.0e-5, 7.0e-5, 4.5e-5, 3.8e-5, 4.2e-5, 2.62e-5, 3.6e-5])
# copper = np.array([4.5e-5, 1.97e-5, 1.6e-5, 1.97e-5, 4.0e-5, 2.4e-5, 1.9e-5, 2.41e-5, 1.85e-5, 3.3e-5])
# steel = np.array([3.3e-5, 1.2e-5, 0.9e-5, 1.2e-5, 1.3e-5, 1.6e-5, 1.4e-5, 1.58e-5, 1.32e-5, 2.1e-5])

# Calculate the average
# aluminum_mean = np.mean(aluminum)
# copper_mean = np.mean(copper)
# steel_mean = np.mean(steel)

# Calculate the standard deviation
# aluminum_std = np.std(aluminum)
# copper_std = np.std(copper)
# steel_std = np.std(steel)

# Create lists for the plot
# materials = ['Aluminum', 'Copper $\\alpha$', 'Steel r$\sum_{i=0}^\infty x_i$']
# x_pos = np.arange(len(materials))
# CTEs = [aluminum_mean, copper_mean, steel_mean]
# error = [aluminum_std, copper_std, steel_std]

# Build the plot
# fig, ax = plt.subplots()
# ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
# ax.set_ylabel('Coefficient of Thermal Expansion ($\degree C^{-1}$)')
# ax.set_xticks(x_pos)
# ax.set_xticklabels(materials)
# ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
# ax.yaxis.grid(True)

plt.show()
