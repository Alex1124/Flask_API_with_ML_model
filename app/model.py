## coding: UTF-8#
from xgboost import XGBClassifier


xgbmodel_iris = XGBClassifier().load_model('app/model/xgb_iris.json')
    
def predict(input):
    pred = xgbmodel_iris.predict(input)[0]
    print(pred)
    return pred
