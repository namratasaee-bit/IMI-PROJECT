import random
import pandas as pd

data = []

for i in range(100):
    row = {
        "LipinskiViolations": random.randint(0, 1),
        "Veber": random.randint(0, 1),
        "Solubility": random.uniform(-6, 2)
    }
    data.append(row)

pd.DataFrame(data).to_csv("aash_1.csv", index=False)
print("Aash part 1 done")