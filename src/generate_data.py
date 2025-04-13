import numpy as np
import pandas as pd
import os

# 1. Parameters
NUM_TRIANGLES = 2000
MIN_LENGTH = 1
MAX_LENGTH = 100

# 2. Generate random side lengths for right triangles
a = np.random.uniform(MIN_LENGTH, MAX_LENGTH, NUM_TRIANGLES)
b = np.random.uniform(MIN_LENGTH, MAX_LENGTH, NUM_TRIANGLES)
c = np.sqrt(a**2 + b**2)  # Hypotenuse using Pythagoras theorem

# 3. Create a DataFrame
df = pd.DataFrame({'a': a, 'b': b, 'c': c})

# 4. Ensure the 'data' folder exists and save to CSV
os.makedirs('data', exist_ok=True)
df.to_csv('data/triangles.csv', index=False)

print("Dataset successfully generated in 'data/triangles.csv'")


