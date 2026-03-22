# =========================
# IMPORTS
# =========================
import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv("final_dataset_updated.csv")

# =========================
# SELECT FEATURES
# =========================
features = [col for col in df.columns if col not in ["SMILES", "Target"]]

X = df[features]
y = df["Target"]

# =========================
# TRAIN MODEL (Evaluator)
# =========================
model = RandomForestClassifier(n_estimators=200, max_depth=10)
model.fit(X, y)

# =========================
# GET FEATURE RANGES
# =========================
feature_ranges = {}

for col in X.columns:
    feature_ranges[col] = (X[col].min(), X[col].max())

# =========================
# GENERATE RANDOM CANDIDATE
# =========================
def generate_candidate():
    candidate = []
    
    for col in X.columns:
        low, high = feature_ranges[col]
        val = random.uniform(low, high)
        candidate.append(val)
    
    return candidate

# =========================
# INVERSE DESIGN LOOP
# =========================
results = []
num_iterations = 2000

for _ in range(num_iterations):
    x = generate_candidate()
    
    # FIX: use DataFrame with correct column names
    x_df = pd.DataFrame([x], columns=X.columns)
    
    prob = model.predict_proba(x_df)[0][1]
    
    results.append((prob, x))

# =========================
# SORT BEST CANDIDATES
# =========================
results.sort(reverse=True, key=lambda x: x[0])

# =========================
# PRINT TOP 5 RESULTS
# =========================
print("\nTop Designed Compounds:\n")

for i in range(5):
    score, candidate = results[i]
    
    print(f"Candidate {i+1}")
    print("Drug-likeness Score:", round(score, 4))
    
    for j, col in enumerate(X.columns):
        print(f"{col}: {round(candidate[j], 3)}")
    
    print("-" * 50)
