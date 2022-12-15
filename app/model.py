## coding: UTF-8#
from xgboost import XGBClassifier


def predict_class(input):
    xgbmodel_iris = XGBClassifier()                         ##創立xgb分類物件
    xgbmodel_iris.load_model('app/model/xgb_iris.json')     ##xgb物件載入參數
    pred = xgbmodel_iris.predict(input)[0]
    print(pred)
    return pred

