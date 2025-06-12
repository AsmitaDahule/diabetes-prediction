# diabetes-prediction

# Diabetes Prediction Web App

This project is a **Machine Learning Web Application** that predicts whether a person is diabetic or not based on several health metrics. It uses a Support Vector Machine (SVM) model trained on the PIMA Indian Diabetes dataset.

---

##  Dataset

- **Source:** PIMA Indian Diabetes Dataset
- **Attributes Used:**
  - Pregnancies
  - Glucose
  - BloodPressure
  - SkinThickness
  - Insulin
  - BMI
  - DiabetesPedigreeFunction
  - Age
  - Outcome (0 = Non-diabetic, 1 = Diabetic)

---

##  Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **ML Libraries:** scikit-learn, pandas, numpy

---

##  Project Structure

diabetes-prediction-app/
├── app.py # Flask app
├── train_model.py # ML training & model saving script
├── diabetes.csv # Dataset
├── model.pkl # Trained SVM model (auto-generated)
├── scaler.pkl # StandardScaler object (auto-generated)
├── requirements.txt # Required Python libraries
├── templates/
│ └── index.html # Frontend form interface
├── static/
│ └── style.css # CSS styling
└── README.md # Project documentation




---

##  How to Run the Project

1. Clone the Repository

    git clone https://github.com/your-username/diabetes-prediction-app.git
    cd diabetes-prediction-app


2. Install Required Packages

    pip install -r requirements.txt

3. Train the ML Model

    python train_model.py

 4. Run the Flask Web App

    python app.py

Visit :  http://127.0.0.1:5000

Dummy Input for Testing
Pregnancies	Glucose	BP	Skin	Insulin	BMI	DPF	Age
2	90	66	23	94	28.1	0.167	25


Author
Asmita Arun Dahule
B.Tech CSE | Frontend Developer | ML Enthusiast


