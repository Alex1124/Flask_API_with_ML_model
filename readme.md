#機器學習API

使用鳶尾花資料 進行'xgboost'分類模型訓練，

使用Flask建置API介面提供輸入值預測。最後部署到Render平台

#模型說明-Boosting

Bagging 通過隨機抽樣的方式生成每一棵樹，使每棵樹彼此獨立並無關聯，隨機森林就是 Bagging 的一個實例。

Boosting 則是透過序列的方式生成樹，後面生成的樹會與前一棵樹相關。

XGBoost 是 Boosting 方法的一種實例，每棵樹的生成都改善了前一棵樹學習不好的地方，因此 Boosting 模型通常比 Bagging 更精準。


部署網址:

https://py-flask-api-ml-xgb-iris.onrender.com/


類別:

0:setosa
1:versicolor
2:virginica


test:


route:/predict

 {
 "sepalLengthCm":5.2,
  "sepalWidthCm":2.7,
  "petalLengthCm":3.9,
  "petalWidthCm":1.4
  }

![image](https://user-images.githubusercontent.com/26739923/233819536-ffa96a04-2d48-4efe-acfe-901569d63c0c.png)


![image](https://user-images.githubusercontent.com/26739923/233819474-2e306e12-3e8a-4580-b157-209b776575dc.png)


![image](https://user-images.githubusercontent.com/26739923/233819514-fcd6c8bd-6de9-4ff8-aaf5-3e2a3d81bc10.png)
