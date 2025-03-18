import pandas as pd
# Load the dataset
df = pd.read_excel("Folds5x2_pp.xlsx")  # Make sure the file is in the same folder

# Save as CSV
df.to_csv("C:/Users/uday kiran/Documents/power_plant_data.csv", index=False)

# Print first few rows
print(df.head())
