import pandas as pd

# Read the Excel file
df = pd.read_excel(
    'C:\\Users\\pittm\\Programming\\Kaggle\\FWP-CountryData.xlsx')

# Write the data frame to a CSV file
df.to_csv('FWP-CountryData.csv', index=False)
