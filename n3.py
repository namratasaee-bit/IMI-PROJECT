import random
import pandas as pd

data = []

for i in range(100):
    row = {
        "SubstructureCount": random.randint(1, 25),
        "AtomCount": random.randint(5, 60),
        "BondCount": random.randint(5, 60),
        "IsAromatic": random.randint(0, 1)
    }

    # fingerprints
    for j in range(5):
        row[f"FP_{j}"] = random.randint(0, 1)

    data.append(row)

pd.DataFrame(data).to_csv("namrata_3.csv", index=False)
print("Namrata part 3 done")