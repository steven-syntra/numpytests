import numpy as np

# np.random.normal( mean, standarddev, number_of_samples )
height = np.round(np.random.normal( 1.75, 0.20, 30), 2)
weight = np.round(np.random.normal( 60.32, 15, 30), 2)
np_city = np.column_stack((height, weight))

print(np_city)

print( f"Gemiddelde lengte is {np.round(np.mean(np_city[:,0]), 2)}")
print( f"Mediaan lengte is {np.round(np.median(np_city[:,0]), 2)}")
print( f"Standaarddeviatie voor lengte is {np.round(np.std(np_city[:,0]), 2)}")


