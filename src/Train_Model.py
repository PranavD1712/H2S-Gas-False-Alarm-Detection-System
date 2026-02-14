import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Loading the Dataset
Data = pd.read_csv("Historical Alarm Cases.csv")

#print('Dataset Shape:', Data.shape)
#print('\nFew Records:')
#print(Data.head())
#print('\nDetails:', Data.info())

# Splitting columns
x = Data.drop('Spuriosity Index(0/1)', axis=1)
y = Data['Spuriosity Index(0/1)']

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Training Logistic Regression Model
lr = LogisticRegression()
lr.fit(x_train_scaled, y_train)


print("\n MODEL TRAINING COMPLETE!")

# Model Evaluation
y_pred = lr.predict(x_test_scaled)

print('\n Model Accuracy :', accuracy_score(y_test, y_pred))
print('\n Classification Report :')
print(classification_report(y_test, y_pred))
print('\n Confusion Matrix :')
print(confusion_matrix(y_test, y_pred))

# Saving Model & Scaler
with open('lr.pkl', 'wb') as f:
    pickle.dump(lr, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print('\n Model & Scaler Saved Successfully..!')