# manual_linear_regression_wine_quality
Manual calculation of Linear Regression to predict wine quality
This script doesn't not use any module to calculate the Linear Regression. We will be calculating it based on the
formula: y = mx + b. Where y is th predicted variable which is our data is "quality", x is the known variable which is
"density" in the data, m is the slope and b is the intercept

# Usage
`python predict_wine_quality.py`

# Data
https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/

# Citation
Data provided by
P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

# Analysis
The script generates a column that represents that predicted wine quality. Below is an example of the data set with
the prediction column
|fixed acidity  |volatile acidity  |citric acid  |residual sugar  |chlorides  |free sulfur dioxide  |total sulfur dioxide  |density    |pH  |sulphates|alcohol  |quality  |predicted_quality|
|--------------:|-----------------:|------------:|---------------:|----------:|--------------------:|---------------------:|----------:|---:|--------:|--------:|--------:|----------------:|
|            7.0|              0.27|         0.36|            20.7|      0.045|   45.0              |   170.0   		   |	1.0010 |3.00|     0.45|8.8      |  6      |     5.243802    |
|            6.3|              0.30|         0.34|             1.6|      0.049|   14.0              |   132.0              |0.9940     |3.30|     0.49|9.5      |  6      |     5.880399    |
|            8.1|              0.28|         0.40|             6.9|      0.050|  30.0               |   97.0               |0.9951     |3.26|     0.44|10.1     |   6     |      5.780362   |
|            7.2|              0.23|         0.32|             8.5|      0.058|   47.0              |   186.0              |0.9956     |3.19|     0.40|9.9      |  6      |     5.734891    |
|            7.2|              0.23|         0.32|             8.5|      0.058|   47.0              |   186.0              |0.9956     |3.19|     0.40|9.9      |  6      |     5.734891    |

The Squared Residuals (RSS is the square of residuals which is the distance between each prediction and the actual value) is
**3478.68946969**

The Standard error is (The standard error lets us quickly determine how good or bad a linear model)
**0.842921491036**

what percentage of actual y values are within 1 standard error of the predicted y value?
**0.684565128624**

what percentage of actual y values are within 2 standard errors of the predicted y value?
**0.935688035933**

what percentage of actual y values are within 3 standard errors of the predicted y value?
**0.993670886076**




