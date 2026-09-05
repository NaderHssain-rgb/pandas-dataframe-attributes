# Pandas DataFrame Attributes

Beginner Python practice using **Pandas** to understand important DataFrame attributes and methods used for inspecting and analyzing data.

## 📌 Topics Covered

* DataFrame
* `index`
* `columns`
* `values`
* `dtypes`
* `shape`
* `ndim`
* `size`
* `empty`
* `T`
* `axes`
* `isna()`
* `notna()`
* `describe()`
* `info()`
* `head()`
* `tail()`

## 🛠️ Technologies

* Python
* Pandas

## 📂 Project Structure

```text
pandas-dataframe-attributes/
│
├── pandas_dataframe_attributes.py
├── requirements.txt
└── README.md
```

## 🚀 Installation

Install the required library:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python pandas_dataframe_attributes.py
```

## 📖 DataFrame Attributes

### `df.index`

Returns the index of the DataFrame.

```python
df.index
```

### `df.columns`

Returns the column names.

```python
df.columns
```

### `df.values`

Returns the underlying values of the DataFrame.

```python
df.values
```

### `df.dtypes`

Returns the data type of each column.

```python
df.dtypes
```

### `df.shape`

Returns the number of rows and columns.

```python
df.shape
```

For example:

```text
(3, 3)
```

means 3 rows and 3 columns.

### `df.ndim`

Returns the number of dimensions.

```python
df.ndim
```

A DataFrame normally has 2 dimensions.

### `df.size`

Returns the total number of elements in the DataFrame.

```python
df.size
```

### `df.empty`

Checks whether the DataFrame is empty.

```python
df.empty
```

Returns:

```text
True
```

if the DataFrame is empty and:

```text
False
```

if it contains data.

### `df.T`

Transposes the DataFrame by switching rows and columns.

```python
df.T
```

### `df.axes`

Returns the DataFrame axes, including the row index and column labels.

```python
df.axes
```

## 🔎 Missing Values

### `df.isna()`

Checks for missing values.

```python
df.isna()
```

A result of `True` means that the value is missing.

### `df.notna()`

Checks for values that are not missing.

```python
df.notna()
```

A result of `True` means that the value exists.

## 📊 Statistical Summary

The `describe()` method provides a statistical summary of numerical columns.

```python
df.describe()
```

It can provide information such as:

* Count
* Mean
* Standard deviation
* Minimum
* Percentiles
* Maximum

## ℹ️ DataFrame Information

The `info()` method provides general information about the DataFrame.

```python
df.info()
```

It is useful for checking:

* Number of rows
* Column names
* Non-null values
* Data types
* Memory usage

## 🔝 First Rows

The `head()` method displays the first rows.

```python
df.head(1)
```

This displays the first row.

You can also specify a different number:

```python
df.head(5)
```

## 🔚 Last Rows

The `tail()` method displays the last rows.

```python
df.tail(1)
```

This displays the last row.

## 🧠 What I Learned

Through this project, I practiced how to inspect a Pandas DataFrame and understand its:

* Structure
* Index
* Columns
* Data types
* Dimensions
* Size
* Missing values
* Statistical information
* First and last rows

## 🎯 Project Goal

The goal of this project is to build a strong foundation in Pandas DataFrame inspection before moving to more advanced data-analysis techniques.

## 📚 Future Improvements

Possible next steps:

* Practice `value_counts()`
* Practice `unique()`
* Practice `nunique()`
* Work with missing values
* Filter DataFrames
* Sort data
* Add and remove columns
* Group data using `groupby()`
* Analyze real datasets

## 👨‍💻 Author

Nader

## ⭐ Note

This repository is part of my Python and Data Science learning journey.
