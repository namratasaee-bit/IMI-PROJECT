import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import *

df = pd.read_csv("final_dataset_updated.csv")

structural = [
    "RingCount","Heteroatoms","FractionSP3","ChiralCenters",
    "DoubleBonds","NumRings","SubstructureCount",
    "AtomCount","BondCount","IsAromatic"
]

fingerprints = [col for col in df.columns if col.startswith("FP_")]
features = structural + fingerprints

X = df[features]
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_prob)

plt.figure()
plt.plot(fpr, tpr)
plt.title("ROC Curve - Random Forest")
plt.xlabel("FPR")
plt.ylabel("TPR")
plt.show()

# Feature Importance Plot
importance = model.feature_importances_
plt.figure()
plt.bar(range(len(importance)), importance)
plt.title("Feature Importance")
plt.show()


# =========================
# CONFUSION MATRIX HEATMAP
# =========================
cm = confusion_matrix(y_test, y_pred)

plt.figure()
plt.imshow(cm)
plt.title("Confusion Matrix - Random Forest")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()