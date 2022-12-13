## coding: UTF-8#
import pickle,gzip

# load model
with gzip.open('app/model/xgb_iris.pgz','r') as f :
    xgbmodel = pickle.load(f)
    
def predict(input):
    pred = xgbmodel.predict(input)[0]
    print(pred)
    return pred