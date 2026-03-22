import random
import pandas as pd

data = []

for i in range(100):
    row = {
        "ChiralCenters": random.randint(0, 4),
        "DoubleBonds": random.randint(0, 6),
        "NumRings": random.randint(0, 8)
    }
    data.append(row)

pd.DataFrame(data).to_csv("namrata_2.csv", index=False)
print("Namrata part 2 done")