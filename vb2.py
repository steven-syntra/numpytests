import numpy as np

height = [1.71, 1.87, 1.92]
np_height = np.array(height)

weight = [64, 81, 87]
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print(bmi > 23)       # geef een numpy array met boolean values
print(bmi[bmi > 23])  # geef een numpy array met de elementen die groter zijn dan 23
