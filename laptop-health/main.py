import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Assuming you have collected some sensor data and labeled it as healthy (0) or unhealthy (1)
# This is just a dummy dataset for demonstration purposes
# Replace this with your actual data
sensor_data = np.random.rand(100, 5)  # 100 samples, 5 features
labels = np.random.randint(2, size=100)  # Binary labels: 0 for healthy, 1 for unhealthy

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(sensor_data, labels, test_size=0.2, random_state=42)

# Train a random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict labels for the test set
y_pred = clf.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Now you can use this trained model to predict the health status of new laptop sensor data
# For example:
new_sensor_data = np.random.rand(1, 5)  # New sensor data from the laptop
predicted_label = clf.predict(new_sensor_data)
if predicted_label == 0:
    print("The laptop is healthy.")
else:
    print("The laptop is unhealthy.")
