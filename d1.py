import random
import pandas as pd

data = []

for i in range(100):
    row = {
        "SMILES": f"C{i}",
        "MolWt": random.uniform(100, 700),
        "LogP": random.uniform(-2, 7),
        "HDonors": random.randint(0, 10)
    }
    data.append(row)

pd.DataFrame(data).to_csv("darshan_1.csv", index=False)
print("Darshan part 1 done")