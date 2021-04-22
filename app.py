import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


prediction = []

@app.route('/predict',methods=['POST'])
def predict():   
   p = []
   categorical_parm = []
   a = list(request.form.values())
   
   print(a)
   if a[2] == 'CA0627':
       location_parm = 2
   if a[3] == 'REG':
       earncode_parm = 68
   month_parm = a[0]
   year_parm = a[1]
   categorical_parm.append(month_parm)
   categorical_parm.append(year_parm)
   categorical_parm.append(location_parm)
   categorical_parm.append(earncode_parm)

   print('categorical_parm',categorical_parm)
   p = model.predict([categorical_parm])
  
   return render_template('index.html', prediction_text='Predicted value of earned hours {} '.format(p))
   
if __name__ == "__main__":
    app.run(debug=True)

