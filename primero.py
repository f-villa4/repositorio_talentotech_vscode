print('Hello World')
data = [23, 25, 30, 22, 28, 35, 40, 27, 33, 21, 29, 31, 26, 34, 38, 24, 32, 36, 39, 20, 37, 41, 45, 19, 42]

# Importing libraries for data analysis and visualization
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as stats
import statistics as sta

# Calculating descriptive statistics
n = len(data)
print(f"Number of elements: {n}")
mean = sta.mean(data)
print(f"Mean: {mean}")
median = sta.median(data) 
print(f"Median: {median}")
mode = sta.mode(data)
print(f"Mode: {mode}")
variance = sta.variance(data)
print(f"Variance: {variance}")
stdev = sta.stdev(data)
print(f"Standard Deviation: {stdev}")
skewness = stats.skew(data)
print(f"Skewness: {skewness}")
kurtosis = stats.kurtosis(data)
print(f"Kurtosis: {kurtosis}")
iqr = stats.iqr(data)
print(f"IQR: {iqr}")
min_value = min(data)
print(f"Minimum: {min_value}")
max_value = max(data)
print(f"Maximum: {max_value}")
range_value = max_value - min_value
print(f"Range: {range_value}")
q1 = np.percentile(data, 25)
print(f"Q1: {q1}")
q3 = np.percentile(data, 75)
print(f"Q3: {q3}")
cv = (stdev / mean) * 100
print(f"Coefficient of Variation: {cv}%")

# Looking for outliers using IQR method
outliers = [x for x in data if x < (q1 - 1.5 * iqr) or x > (q3 + 1.5 * iqr)]
print(f"Outliers: {outliers}")

# Plotting a histogram
# Calculating the number of bins using Sturges' formula
bins = int(1+3.322 * np.log10(n))  # Sturges' formula for bin count
print(f"Number of bins (Sturges' formula): {bins}")
# Plotting the histogram with the calculated number of bins
plt.figure(figsize=(10, 6))
plt.hist(data, bins=bins, edgecolor='black', color='pink', density=True)
sns.kdeplot(data, fill=True, color="black")
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid()
plt.show()

# Plotting a boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='pink', color='black'), medianprops=dict(color='black'))
plt.xlabel('Value')
plt.title('Boxplot')
plt.grid()
plt.show()

