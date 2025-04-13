import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import os

# 1. Load dataset
df = pd.read_csv('data/triangles.csv')
X = df[['a', 'b']]  # Features: legs a and b
y = df['c']         # Target: hypotenuse c

# 2. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📊 Mean Squared Error (MSE): {mse:.4f}")
print(f"📈 R² Score: {r2:.4f}")

# 5. Plot prediction results
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("True Hypotenuse")
plt.ylabel("Predicted Hypotenuse")
plt.title("Hypotenuse Prediction")
plt.grid(True)

# 6. Save the plot
os.makedirs('data', exist_ok=True)
plt.savefig('data/prediction_plot.png')
plt.show()
