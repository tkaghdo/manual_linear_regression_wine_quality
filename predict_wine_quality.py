
"""
Manual calculation of Linear Regression to predict wine quality
This script doesn't not use any module to calculate the Linear Regression. We will be calculating it based on the
formula: y = mx + b.Where y is th predicted variable which is our data is "quality", x is the known variable which is
"density" in the data, m is the slope and b is the intercept

Usage:
python predict_wine_quality.py

"""
import pandas as pd
import numpy as np
import sys

__author__ = "Tamby Kaghdo"


def predict(x, slope, intercept):
    """
    calculated the predicted value based on the linear regression function: y = mx + b
    :param x: the known variable
    :param slope: the m in the formula
    :param intercept: the b in the formula
    :return: the predicted value y
    """

    y = (slope * x) + intercept
    return y


def within_standard_error(y, predicted_y, standard_error, error_margin):
    """
    calculates the percentage of actual y values that are within [error_margin] standard error of the predicted y value
    :param y: actual series
    :param predicted_y: predicted series
    :param standard_error: the standard error
    :param error_margin: error count
    :return: percentage of actual y values that are within [error_margin] standard error of the predicted y value
    """
    diff = abs(predicted_y - y)
    lower_diffs = [d for d in diff if d <= (standard_error * error_margin)]

    within_count = len(lower_diffs)
    return float(float(within_count) / float(len(y)))


def main():
    try:
        wine_df = pd.read_csv("data/wine_quality_white.csv")

        # calculate the slope m. the formula for m = cov(x, y) / var(x)
        # look at http://stackoverflow.com/questions/15317822/calculating-covariance-with-python-and-numpy
        # for explanation on the [0][1] in the cov calc
        slope_density = np.cov(wine_df["density"], wine_df["quality"])[0][1] / wine_df["density"].var()

        # calculate the intercept
        intercept_density = wine_df["quality"].mean() - (slope_density * wine_df["density"].mean())

        predicted_quality = wine_df["density"].apply(predict, slope=slope_density, intercept=intercept_density)
        wine_df["predicted_quality"] = predicted_quality

        # compute squared residuals which is the square if distance between each prediction and the actual value or rss
        wine_df["diff squared"] = (wine_df["quality"] - wine_df["predicted_quality"]) ** 2
        rss = wine_df["diff squared"].sum()
        print("RSS = {0}".format(rss))

        # compute the standard error. The standard error lets us quickly determine how good or bad a linear model
        # is at prediction
        standard_error = (rss/(len(wine_df) - 2)) ** 0.5
        print("Standard Error = {0}".format(standard_error))

        # what percentage of actual y values are within 1 standard error of the predicted y value
        within_one = within_standard_error(wine_df["quality"], wine_df["predicted_quality"], standard_error, 1)
        print(within_one)
        print("percentage of actual y values are within 1 standard error of the predicted y value = {0}".format(within_one))

        # what percentage of actual y values are within 2 standard errors of the predicted y value?
        within_two = within_standard_error(wine_df["quality"], wine_df["predicted_quality"], standard_error, 2)
        print(within_two)
        print("percentage of actual y values are within 2 standard error of the predicted y value = {0}".format(within_two))

        # what percentage of actual y values are within 3 standard errors of the predicted y value?
        within_three = within_standard_error(wine_df["quality"], wine_df["predicted_quality"], standard_error, 3)
        print(within_three)
        print("percentage of actual y values are within 3 standard error of the predicted y value = {0}".format(within_three))

    except IOError as e:
        print(e)
        sys.exit(e.errno)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)