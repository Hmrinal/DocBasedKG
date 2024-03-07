import matplotlib.pyplot as plt
import numpy as np

# Given data for the bar graph with standard deviations
iterations = np.array([90000, 95000, 100000, 150000, 200000])
times_per_10k_model_1 = np.array([1.3633, 1.3632, 1.3900, 1.3747, 1.3630])
times_per_10k_model_2 = np.array([1.5156, 1.5168, 1.5200, 1.5100, 1.5120])
times_per_10k_model_3 = np.array([1.1856, 1.1758, 1.1730, 1.1793, 1.1825])

std_dev_model_1 = np.array([0.0010, 0.0010, 0.0009, 0.0009, 0.0010])
std_dev_model_2 = np.array([0.0010, 0.0010, 0.0009, 0.0009, 0.0009])
std_dev_model_3 = np.array([0.0009, 0.0009, 0.0010, 0.0009, 0.0010])

# Calculate positions for each set of bars
bar_width = 0.25
indices = np.arange(len(iterations))

# Plotting the bar graph with standard deviations
plt.figure(figsize=(12, 8))

plt.bar(indices, times_per_10k_model_1, bar_width, yerr=std_dev_model_1, label='Data Model 1', capsize=5, color='blue')
plt.bar(indices + bar_width, times_per_10k_model_2, bar_width, yerr=std_dev_model_2, label='Data Model 2', capsize=5, color='orange')
plt.bar(indices + 2 * bar_width, times_per_10k_model_3, bar_width, yerr=std_dev_model_3, label='Data Model 3', capsize=5, color='green')

# Adding labels and title
plt.xlabel('Iterations')
plt.ylabel('Time per 10K Queries (s)')
plt.title('Query Time Comparison Between Data Models')
plt.xticks(indices + bar_width, [f"{num:,}" for num in iterations])
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()



