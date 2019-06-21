import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

data_size = 100
df1 = pd.DataFrame(dict(id=range(data_size), age=np.random.randint(18, 31, data_size), weight=np.random.randint(40, 80, data_size)))
df1.set_index("id", inplace=True)

print("DataSet:")
print(df1)

# Central tendency
print("\nMean of age =", df1.age.mean())
print("Mean of DataFrame:")
print(df1.mean())
print("\nMedian of age =", df1.age.median())
print("Median of DataFrame:")
print(df1.median())
# pd.DataFrame.mode() returns a Series of one or more modes
print("\nMode(s) of Age:")
print(df1.age.mode())
print("Mode(s) of DataFrame:")
print(df1.mode())

# Measure of spread
print("\nRange of age =", df1.age.max()-df1.age.min())
print("Variance of age =", df1.age.var())
print("Standard deviation of age =", df1.age.std())


"""
SKEWNESS & KURTOSIS
-------------------

Skewness describes the symmetry of the distribution.
----------------------------------------------------
Normal distribution : skewness = 0 (Bell curve)
Positively skewed   : skewness > 0 (Tail to the right)
Negatively skewed   : skewness < 0 (Tail to the left)


Kurtosis describes how pointy or how flat the distribution is.
--------------------------------------------------------------
Mesokurtic  : kurtosis = 0  (Bell curve)
Leptokurtic : kurtosis > 0  (Sharp peak distribution)
Platykurtic : kurtosis < 0  (Flattened)
"""

print("Skewness of data:", df1["age"].skew())
print("Kurtosis of data:", df1["age"].kurt())

plt.hist(df1["age"])
plt.title("Histogram of age data")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
