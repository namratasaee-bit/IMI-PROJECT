import random
import pandas as pd

data = []

for i in range(100):
    row = {
        "HeavyAtoms": random.randint(5, 60),
        "FormalCharge": random.choice([-1, 0, 1]),
        "MolMR": random.uniform(20, 150),
        "AromaticRings": random.randint(0, 6)
    }
    data.append(row)

pd.DataFrame(data).to_csv("darshan_3.csv", index=False)
print("Darshan part 3 done")