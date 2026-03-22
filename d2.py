import random
import pandas as pd

data = []

for i in range(100):
    row = {
        "HAcceptors": random.randint(0, 15),
        "TPSA": random.uniform(20, 200),
        "RotBonds": random.randint(0, 15)
    }
    data.append(row)

pd.DataFrame(data).to_csv("darshan_2.csv", index=False)
print("Darshan part 2 done")