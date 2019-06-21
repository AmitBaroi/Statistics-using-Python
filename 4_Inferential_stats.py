"""
Inferential Statistics
----------------------
Inferring unknown data based on known values.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# SciPy for finding critical value
import scipy.stats as stats

# Generating random data
population = np.random.randint(1, 80, 1000)

# Skew & Kurt
print("Skewness =", pd.Series(population).skew())
print("Kurtosis =", pd.Series(population).kurt())

plt.hist(population, bins=50)
plt.show()

# Dunno why we're doing this
np.random.seed(10)

# List to store the different sample means
estimates = []

# We will take 200 sample
for each in range(200):
    # Each sample will be of size 100
    sample = np.random.choice(population, 100)
    estimates.append(sample.mean())

# Showing the population mean & estimated mean (from average of 200 samples)
print("Population mean", "\t"*3, "=", np.mean(population))
print("Average of 200 sample means  =", np.mean(estimates))

# Making a density plot of our 200 sample means
pd.DataFrame(estimates).plot(kind="density")
plt.show()

"""
--------------------
POINT OF ESTIMATIONS
--------------------

CONFIDENCE INTERVALS
--------------------
Confidence interval = from (sample mean - margin of error) to (sample mean + margin of error)
In between this lower limit and upper limit we will find 95% of our data. 

MARGIN OF ERROR:
----------------
marginOfError = (criticalValue)*(SD/√(sampleSize))
"""

# Finding critical value (needed to calculate margin of error)
z_critical = stats.norm.ppf(q=0.975)        # Percent point function
t_critical = stats.t.ppf(q=0.975, df=24)    # df is degrees of freedom (sample size -1)
print("Z-Critical value =", z_critical)
print("T-Critical value =", t_critical)

# Computing margin of error
margin_of_error = z_critical * (np.std(estimates)/np.sqrt(200))
print("Margin of error =", margin_of_error)

# Lower limit
low_lim = np.mean(estimates) - margin_of_error
# Upper limit
up_lim = np.mean(estimates) + margin_of_error
print("Confidence Interval:", low_lim, "to", up_lim)
