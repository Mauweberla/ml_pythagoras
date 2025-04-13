# Predicting the Hypotenuse with Mau

Using machine learning, this project predicts the hypotenuse (c) of right-angle triangles given legs a and b, approximating the Pythagorean Theorem.

## 1. Software

Developed on: Ubuntu · Python 3 · Visual Studio Code  
Make sure you're using a virtual environment before installing dependencies from `requirements.txt`.

## 2. Objective

1 - Approximate the mathematical formula  
   c = √(a² + b²)  
   using shallow machine learning.

2 - Evaluate a **Linear Regression** model on this nonlinear relationship.  
   Although Pythagoras’ Theorem is nonlinear due to the square root, this project explores how well a linear model can approximate it.

## 3. Folder Structure

ml_pythagoras/  
1. data:  
- triangles.csv (Generated dataset)  
- prediction_plot.png (Prediction vs True plot)  

2. src:  
- generate_data.py (Create synthetic dataset)  
- train_model.py (Train and evaluate Linear Regression model)  

3. requirements.txt  
(Python dependencies)  

4. README.md  
(Project documentation)

## 4. Installation

Install required packages:
pip install -r requirements.txt

## 5. Dataset Description

The dataset contains 2000 samples of right-angled triangles.The side lengths a and b were randomly generated using a uniform distribution between 1 and 100.The hypotenuse c was calculated using Pythagoras' Theorem:

c = √(a² + b²)

All values were saved to a CSV file:data/triangles.csv

## 6. Model Details

This project uses a Linear Regression model from scikit-learn to approximate the relationship between the input features (a, b) and the output (c).

Why Linear Regression?

Although the true function (c = √(a² + b²)) is nonlinear, linear regression is tested to see how well it can approximate the result in practice.

Features (X): side a, side b

Target (y): hypotenuse c

Model: LinearRegression()

## 7. Evaluation Results

After training the model on 80% of the data and evaluating it on 20%, the following metrics were observed:

Metric

Value

MSE

35.4274

R²

0.9812

These results show that despite the square root non-linearity, the linear model approximates the relationship with high accuracy.A scatter plot comparing the true and predicted values was saved as:data/prediction_plot.png

![prediction_plot](https://github.com/user-attachments/assets/a45bc9bb-8aed-48e3-8e1b-59fdeb15e83a)

## 8. How to Run

To execute the full workflow, run the following commands from the terminal:

python src/generate_data.py      # Generates the dataset
python src/train_model.py        # Trains the model and evaluates it

Make sure you have activated your virtual environment before running the scripts.












