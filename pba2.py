import pandas as pd

# 1. Create a Pandas Series containing 10 temperature readings
temperatures = pd.Series([28, 32, 35, 29, 31, 27, 34, 30, 36, 25])

print("Daily Temperatures:")
print(temperatures)

# 2. Access temperatures at specific index positions
print("\nTemperature at index 2:", temperatures.iloc[2])
print("Temperature at index 5:", temperatures.iloc[5])

# 3. Filter and display temperatures above 30°C
print("\nTemperatures above 30°C:")
print(temperatures[temperatures > 30])

# 4. Calculate the mean and median temperatures
print("\nMean Temperature:", temperatures.mean())
print("Median Temperature:", temperatures.median())

# 5. Find the minimum and maximum temperatures
print("Minimum Temperature:", temperatures.min())
print("Maximum Temperature:", temperatures.max())



#output:
2    35
4    31
6    34
8    36
dtype: int64

Mean Temperature: 30.7
Median Temperature: 30.5
Minimum Temperature: 25
Maximum Temperature: 36
PS C:\Users\N51314\AppData\Local\Programs\Microsoft VS Code> 
