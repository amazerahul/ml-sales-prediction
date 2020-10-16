# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
# Load the regression model
classifier = pickle.load(open('sales-prediction.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    tv = int(request.form['tv'])
    radio = int(request.form['tv'])
    newspaper = int(request.form['tv'])
    data = [[tv, radio,newspaper]]
    my_prediction = classifier.predict(data)

    return render_template('index.html', prediction_text='The amount of Sales would be {}'.format(round(my_prediction[0],2)))



if __name__ == "__main__":
    app.run(debug=True)