import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    classification_report
)

# Load Iris Dataset

print("=" * 50)
print("PROJECT 2 : DATA CLASSIFICATION USING AI")
print("=" * 50)

iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Loaded Successfully!")

print("\nDataset Information")
print("-" * 30)
print("Total Samples :", X.shape[0])
print("Total Features:", X.shape[1])
print("Classes       :", iris.target_names)

print("\nFeature Names:")
for feature in iris.feature_names:
    print("-", feature)


# PROCESS
# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTrain-Test Split")
print("-" * 30)
print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))


scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\nFeature Scaling Applied Successfully")


# KNN Model
k = 5

model = KNeighborsClassifier(n_neighbors=k)

print("\nKNN Model")
print("-" * 30)
print("K Value Used :", k)

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')

print("\nModel Performance")
print("-" * 30)
print(f"Accuracy : {accuracy:.2%}")
print(f"F1 Score : {f1:.4f}")

# Classification Report
print("\nClassification Report")
print("-" * 30)

print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)

# Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

disp.plot(cmap="Blues")

plt.title("Confusion Matrix - Iris Classification")

# Save image
plt.savefig("confusion_matrix.png")

plt.show()

print("\nConfusion Matrix saved as 'confusion_matrix.png'")

print("\nProject Completed Successfully!")