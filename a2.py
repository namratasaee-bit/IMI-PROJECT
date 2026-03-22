import random
import pandas as pd

data = []

for i in range(100):
    row = {
        "Permeability": random.uniform(-2, 7),
        "GIAbsorption": random.randint(0, 1),
        "BBB": random.randint(0, 1)
    }
    data.append(row)

pd.DataFrame(data).to_csv("aash_2.csv", index=False)
print("Aash part 2 done")