import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
import pickle

# Load dataset
df = pd.read_csv('diabetes.csv')
X = df.drop(columns='Outcome', axis=1)
Y = df['Outcome']

# Preprocessing
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

# Train/Test split
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=2)

# Model training
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Save model and scaler
pickle.dump(classifier, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

print("✅ Model and scaler saved successfully!")
