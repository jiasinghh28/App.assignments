import numpy as np
import pandas as pd

rooms = ["Single", "Double", "Deluxe", "Suite", "Luxury"]
rents = np.array([2000, 3500, 4500, 6000, 8000])

print("Mean Rent:", np.mean(rents))
print("Median Rent:", np.median(rents))
print("Maximum Rent:", np.max(rents))
print("Minimum Rent:", np.min(rents))

df = pd.DataFrame({
    "Room": rooms,
    "Rent": rents
})

print("\nHotel Room Data:")
print(df)

print("\nRooms with rent greater than 4000:")
print(df[df["Rent"] > 4000])
