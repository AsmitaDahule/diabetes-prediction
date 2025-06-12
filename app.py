from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(request.form[key]) for key in request.form]
    input_array = np.asarray(input_data).reshape(1, -1)
    std_data = scaler.transform(input_array)
    prediction = model.predict(std_data)

    if prediction[0] == 0:
        result = 'The person is NOT Diabetic ✅'
    else:
        result = 'The person IS Diabetic ⚠️'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
