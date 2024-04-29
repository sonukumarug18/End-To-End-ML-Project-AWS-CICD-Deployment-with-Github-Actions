from flask import Flask, render_template, url_for,request
from flask import Flask,request,jsonify,render_template
# from sklearn.preprocessing import StandardScaler

import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') 


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 

@app.route('/predict',methods =['GET','POST'])
def predict():
    Cement = float(request.form["Cement"])
    Blast_Furnace_Slag =float(request.form['Blast Furnace Slag'])
    Fly_Ash= float(request.form['Fly Ash'])
    Water=float(request.form['Water'])
    Superplasticizer = float(request.form['Superplasticizer'])
    Coarse_Aggregate  = float(request.form['Coarse Aggregate'])
    Fine_Aggregate= float(request.form['Fine Aggregate'])
    Age=float(request.form['Age'])


    total = [[Cement, Blast_Furnace_Slag, Fly_Ash, Water,Superplasticizer,Coarse_Aggregate,Fine_Aggregate,
               Age]]
    obj = PredictionPipeline()
    prediction = obj.predict(total)
    # prediction = model.predict(scaler.transform(total))


    return render_template('index.html',predict='The value predicted is {:.2f}'.format(prediction[0]))
   


if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0", port = 8080)

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0" , port=8070)


