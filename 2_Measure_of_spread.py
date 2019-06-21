"""
Measure of spread / dispersion
------------------------------
Gives us the variability of the data.
Measures of spread: Range, Quartile/Percentile, Variance, Standard Deviation
"""
import numpy as np

# Making a random DataSet
data = np.random.randint(1, 10, 20)
# Showing data in ascending order
print(np.sort(data))

"""
np.sort() does not change the original data order.
It returns a new array that is sorted (default = ascending). 
"""
# Showing the unsorted data
print(data)

#######################################
# RANGE = MaxValue - MinValue
print("Range =", data.max() - data.min())   # Note: data (an NdArray of numpy) also has mean, median, min, max methods

#######################################
# QUARTILE
# Q1 (25th percentile), Q2 (50th percentile), Q3 (75th percentile) Note: Q2 = Median
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)
print("Q1 =", Q1, ", Q2 =", Q2, ", Q3 =", Q3)
print("Inter-quartile range =", Q3 - Q1)


# New data for population
pop = np.random.randint(1, 100, 100)
print("\nPopulation data:")
print(pop)

sample = np.random.choice(pop, 30)
print("\nSample data:")
print(sample)

#######################################
# VARIANCE = (SUM[1:N](x - mean)^2) / N
# for sample divide by n-1
# Variance is a measure of distance from the mean
print("\nPopulation variance =\t", np.var(pop))
print("Sample variance \t=\t", np.var(sample))

#######################################
# STANDARD DEVIATION = √VARIANCE
# A better/exact measure of distance from the mean
print("Population SD   =\t", np.std(pop))
print("Sample SD   \t=\t", np.std(sample))
