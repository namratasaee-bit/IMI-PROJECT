import random
import pandas as pd

data = []

for i in range(100):
    row = {
        "RingCount": random.randint(0, 8),
        "Heteroatoms": random.randint(0, 12),
        "FractionSP3": random.uniform(0, 1)
    }
    data.append(row)

pd.DataFrame(data).to_csv("namrata_1.csv", index=False)
print("Namrata part 1 done")