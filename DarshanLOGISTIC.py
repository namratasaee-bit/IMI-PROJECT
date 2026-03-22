# =========================
# IMPORTS
# =========================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import *

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("final_dataset_updated.csv")

features = [
    "MolWt","LogP","HDonors","HAcceptors","TPSA",
    "RotBonds","HeavyAtoms","FormalCharge","MolMR","AromaticRings"
]

X = df[features]
y = df["Target"]

# SPLIT
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# SCALE
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# TRAIN
model = LogisticRegression()
model.fit(X_train, y_train)

# PREDICT
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

# =========================
# METRICS
# =========================
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

# =========================
# ROC CURVE
# =========================
fpr, tpr, _ = roc_curve(y_test, y_prob)

plt.figure()
plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Logistic Regression")
plt.show()

# =========================
# CONFUSION MATRIX HEATMAP
# =========================
cm = confusion_matrix(y_test, y_pred)

plt.figure()
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()