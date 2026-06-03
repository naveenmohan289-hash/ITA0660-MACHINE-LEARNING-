from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# -------------------------------
# 1. LOAD DATASET (IRIS)
# -------------------------------
dataset = load_iris()
X = dataset.data
y = dataset.target

# -------------------------------
# 2. SPLIT DATA
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# -------------------------------
# 3. CREATE KNN MODEL
# -------------------------------
k = 3
model = KNeighborsClassifier(n_neighbors=k)

# -------------------------------
# 4. TRAIN MODEL
# -------------------------------
model.fit(X_train, y_train)

# -------------------------------
# 5. TEST MODEL
# -------------------------------
y_pred = model.predict(X_test)

# -------------------------------
# 6. ACCURACY
# -------------------------------
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# -------------------------------
# 7. PREDICT NEW SAMPLE
# -------------------------------
sample = [[5.1, 3.5, 1.4, 0.2]]   # Example input
prediction = model.predict(sample)

print("Predicted Class:", prediction[0])
print("Class Name:", dataset.target_names[prediction[0]])
