"""
Central Tendency
-----------------
Measures of central tendency:
Mean, Median, Mode
"""

import numpy as np              # Mean, Median
from statistics import mode     # Mode (Note: Error when bimodal or multi-modal

# randint() format: lowerMargin, upperMargin, listSize
# Makes a  list (of size 20) of random ints from 5 to 10
rand_list = np.random.randint(5, 10, 20)

# Showing the list and its length
print(rand_list, "Length:", len(rand_list))

# MEAN
print("Mean of the list:\t", np.mean(rand_list))
# MEDIAN
print("Median of the list:\t", np.median(rand_list))
# MODE
print("Mode of the list:\t", mode(rand_list))

"""
Population and Sample
----------------------
Population is the total set of all values of a given field (height of all men in Bangladesh)
Sample is a subset of the population that can be used to represent the whole population.
"""

# Our population data
population = np.random.randint(10, 20, 100)
print("\nPopulation Data:")
print(population)

# Central Tendency
print("Population mean:\t", np.mean(population))
print("Population median:\t", np.median(population))
print("Population mode:\t", mode(population))

# Taking a sample
# choice() format: popArr, sizeOfSample
sample = np.random.choice(population, 20)
print("\nSample Data:")
print(sample)

# Central Tendency
print("Sample mean:\t", np.mean(sample))
print("Sample mean:\t", np.median(sample))
print("Sample mean:\t", mode(sample))
