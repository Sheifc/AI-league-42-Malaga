# 🚀 Linear Regression Project - 42 Málaga Artificial Intelligence League 🤖

Welcome to the repository of the exciting linear regression project by the 42 Málaga Artificial Intelligence League! Here you'll find implementations of both simple and multiple linear regression, along with detailed explanations and code in notebooks.

## 📚 Notebooks

- [Simple Linear Regression](Regresion_Lineal_Simple.ipynb): Discover how to perform simple linear regression step by step!
- [Multiple Linear Regression](Regresion_Lineal_Multiple.ipynb): Learn how to implement multiple linear regression and explore its advantages!

## 📊 Conclusions

### Multiple Linear Regression

#### 🎯 Model Accuracy:
- My model has a good level of accuracy, with an \( R^2 \) of 0.737, indicating that approximately 73.7% of the variability in the number of "households" can be explained by the predictor variables I've used.

#### ❌ Errors:
- The MAE and RMSE values indicate a margin of error in the predictions. Although the RMSE is considerably higher than the MAE, suggesting some larger errors in the predictions.

#### 📊 Comparison with Simple Models:
- The RAE and RSE show that my model is significantly better than a trivial model (such as always predicting the mean), which is a positive sign.

#### 💡 Model Efficiency:
- The adjusted \( R^2 \) is very close to the \( R^2 \), suggesting that the predictors I've chosen are adding value to the model and there is no overfitting.

### Simple Linear Regression

#### 🎯 Model Accuracy:
- My model has a moderate level of accuracy, with an \( R^2 \) of 0.399, suggesting that approximately 39.9% of the variability in "median_income" can be explained by "median_house_value".

#### ❌ Errors:
- The MAE and RMSE values indicate significant errors in the predictions. The RMSE is considerably higher than the MAE, suggesting the presence of large errors in the predictions.

#### 📊 Comparison with Simple Models:
- The RAE and RSE indicate that my model is only somewhat better than a trivial model, suggesting that the relationship between "median_house_value" and "median_income" may not be very strong or that important variables are missing in my model.
