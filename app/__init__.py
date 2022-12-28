## coding: UTF-8#
import numpy as np
from flask import Flask,jsonify,request
from flask_cors import CORS
import app.model as model

app = Flask(__name__)
CORS(app)

@app.route('/test',methods=['GET']) #
def getresult():
    input = np.array([[5.5,2.4,2.7,1.]])
    result = model.predict(input)
    return jsonify({'return':str(result)})

@app.route('/predict',methods=['POST'])
def postinput():
    # get front data
    insertValues = request.get_json()   #sepal.length  sepal.width  petal.length  petal.width
   
    x1 = insertValues['sepalLengthCm']
    x2 = insertValues['sepalWidthCm']
    x3 = insertValues['petalLengthCm']
    x4 = insertValues['petalWidthCm']
    
    inputdata = np.array([[x1,x2,x3,x4]], dtype=object)
    result = model.predict(inputdata)
    
    return jsonify({'return':str(result)})
    
    
