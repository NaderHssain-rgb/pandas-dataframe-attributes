import pandas as pd


# ============================================
# Pandas DataFrame Attributes and Methods
# ============================================

# Create a dictionary containing student data
data = {
    "Name": ["Nader", "Ahmed", "Ali"],
    "Age": [13, 15, 22],
    "Mark": [100, 92, 96]
}

# Create a DataFrame
df = pd.DataFrame(data)


# Display the complete DataFrame
print("DataFrame:")
print(df)

print("#" * 50)

# Display the DataFrame index
print("Index:")
print(df.index)

print("#" * 50)

# Display the column names
print("Columns:")
print(df.columns)

print("#" * 50)

# Display the underlying values
print("Values:")
print(df.values)

print("#" * 50)

# Display the data type of each column
print("Data Types:")
print(df.dtypes)

print("#" * 50)

# Display the number of rows and columns
print("Shape:")
print(df.shape)

print("#" * 50)

# Display the number of dimensions
print("Number of Dimensions:")
print(df.ndim)

print("#" * 50)

# Display the total number of elements
print("Size:")
print(df.size)

print("#" * 50)

# Check whether the DataFrame is empty
print("Is Empty?")
print(df.empty)

print("#" * 50)

# Transpose the DataFrame
print("Transpose:")
print(df.T)

print("#" * 50)

# Display the DataFrame axes
print("Axes:")
print(df.axes)

print("#" * 50)

# Check for missing values
print("Missing Values:")
print(df.isna())

print("#" * 50)

# Check for non-missing values
print("Non-Missing Values:")
print(df.notna())

print("#" * 50)

# Display statistical summary of numerical columns
print("Statistical Summary:")
print(df.describe())

print("#" * 50)

# Display DataFrame information
print("DataFrame Information:")
df.info()

print("#" * 50)

# Display the first row
print("First Row:")
print(df.head(1))

print("#" * 50)

# Display the last row
print("Last Row:")
print(df.tail(1))