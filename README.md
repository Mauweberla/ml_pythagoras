# Predicting the Hypotenuse with Mau

This project uses machine learning to predict the hypotenuse (c) of a right-angled triangle using sides a and b, based on Pythagoras' Theorem.  
It was developed as part of the **Software III - MRAC01** course.

---

## 1. Software

Developed on: Ubuntu · Python 3 · Visual Studio Code  
Make sure you're using a virtual environment before installing dependencies from `requirements.txt`.

---

## 2. Objective

1 - Approximate the mathematical formula  
   c = √(a² + b²)  
   using shallow machine learning.

2 - Evaluate a **Linear Regression** model on this nonlinear relationship.  
   Although Pythagoras’ Theorem is nonlinear due to the square root, this project explores how well a linear model can approximate it.

---

## 2. Folder Structure

ml_pythagoras/  
├── data/  
│   ├── triangles.csv               # Generated dataset  
│   └── prediction_plot.png         # Prediction vs True plot  
├── src/  
│   ├── generate_data.py            # Create synthetic dataset  
│   └── train_model.py              # Train and evaluate Linear Regression model  
├── requirements.txt                # Python dependencies  
└── README.md                       # Project documentation

---

## 3. Installation

Install required packages:

```bash
pip install -r requirements.txt

