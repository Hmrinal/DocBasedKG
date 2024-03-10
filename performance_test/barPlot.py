import matplotlib.pyplot as plt
import numpy as np

# Given data for the bar graph with standard deviations
iterations = np.array([200000])
times_per_10k_model_1 = np.array([1.3630])
times_per_10k_model_2 = np.array([1.5120])
times_per_10k_model_3 = np.array([1.1825])

std_dev_model_1 = np.array([0.0010])
std_dev_model_2 = np.array([0.0009])
std_dev_model_3 = np.array([0.0010])

# Calculate positions for each set of bars
bar_width = 0.20
indices = np.arange(len(iterations)) + 0.1  # Offset to create space at the start

# Define limits for the x-axis to create space at the start and end of the bars
x_limits = [indices[0] - bar_width - 0.1, indices[0] + (3 * bar_width) + 0.1]

# Plotting the bar graph with standard deviations
plt.figure(figsize=(8, 6))  # Adjusted figure size for clarity

plt.bar(indices, times_per_10k_model_1, bar_width, yerr=std_dev_model_1, label='Data Model 1', capsize=5, color='blue')
plt.bar(indices + bar_width, times_per_10k_model_2, bar_width, yerr=std_dev_model_2, label='Data Model 2', capsize=5, color='orange')
plt.bar(indices + 2 * bar_width, times_per_10k_model_3, bar_width, yerr=std_dev_model_3, label='Data Model 3', capsize=5, color='green')

# Customize the plot with labels and title
plt.xlabel('Iterations')
plt.ylabel('Time per 10K Queries (s)')
plt.title('Query Time Comparison Between Data Models')

# Adjust the x-axis
plt.xticks(indices + bar_width, iterations)
plt.xlim(x_limits)

# Adding the legend
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()



