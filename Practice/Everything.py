import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Dataset
X = np.array([[1,20000],
              [3,35000],
              [5,50000],
              [7,65000]])

y = np.array(['Junior','Junior','Senior','Senior'])

# Train model
model = RandomForestClassifier(n_estimators=10, random_state=0)
model.fit(X, y)

# Predict for new data
prediction = model.predict([[4,40000]])

print("Predicted Job Level:", prediction)