## coding: UTF-8#
from xgboost import XGBClassifier


def predict(input):
    xgbmodel_iris = XGBClassifier()                         ##創立xgb分類物件
    xgbmodel_iris.load_model('app/model/xgb_iris.txt')     ##xgb物件載入參數 xgb_iris.json xgb_iris.txt
    pred = xgbmodel_iris.predict(input)[0]
    print(pred)
    return pred


# #way2
# import pickle
# import gzip

# # 載入Model
# with gzip.open('app/model/xgb_iris.pgz', 'r') as f:
#     xgboostModel = pickle.load(f)


# def predict(input):
#     pred=xgboostModel.predict(input)[0]
#     print(pred)
#     return pred
