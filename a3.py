import random
import pandas as pd

data = []

for i in range(100):
    row = {
        "NumValence": random.randint(10, 120),
        "MaxDegree": random.randint(1, 4)
    }

    # BERT embeddings
    for j in range(5):
        row[f"BERT_{j}"] = random.uniform(-1, 1)

    data.append(row)

pd.DataFrame(data).to_csv("aash_3.csv", index=False)
print("Aash part 3 done")