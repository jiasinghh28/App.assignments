import numpy as np
import pandas as pd

products = ["Rice", "Milk", "Bread", "Sugar", "Oil"]
prices = np.array([500, 60, 40, 50, 150])
quantity = [20, 5, 8, 15, 4]

print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

df = pd.DataFrame({
    "Product": products,
    "Price": prices,
    "Quantity": quantity
})

print("\nGrocery Data:")
print(df)

print("\nItems with quantity less than 10:")
print(df[df["Quantity"] < 10])
