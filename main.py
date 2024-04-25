import pandas as pd
import sys

# Load the Excel file
xls_file = pd.ExcelFile(sys.argv[1])

# Read the first sheet into a DataFrame
df = pd.read_excel(xls_file)

# Get the row count of the DataFrame
row_count = len(df)

print(row_count)