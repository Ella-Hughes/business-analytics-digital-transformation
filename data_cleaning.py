
import pandas as pd

# Step 1: Load the original retail dataset
sales = pd.read_excel("Data/raw/Online Retail.xlsx")

# Step 2: Display the first five rows
print("FIRST FIVE ROWS:")
print(sales.head())

# Step 3: Check the dataset size
print("\nDATASET SIZE:")
print(sales.shape)

# Step 4: Display column information
print("\nCOLUMN INFORMATION:")
sales.info()

# Step 5: Check for missing values
print("\nMISSING VALUES:")
print(sales.isnull().sum())

# Step 6: Create a copy of the original dataset
clean_sales = sales.copy()

print("\nORIGINAL RECORDS:", len(clean_sales))

# Step 7: Remove exact duplicate records
duplicates = clean_sales.duplicated().sum()
print("DUPLICATE RECORDS:", duplicates)

clean_sales = clean_sales.drop_duplicates()

# Step 8: Remove missing or blank product descriptions
clean_sales = clean_sales.dropna(subset=["Description"])

clean_sales = clean_sales[
    clean_sales["Description"].str.strip() != ""
].copy()

# Step 9: Identify cancelled invoices
cancelled = clean_sales["InvoiceNo"].astype(str).str.startswith("C")

print("CANCELLED TRANSACTION ROWS:", cancelled.sum())

# Keep completed sales only
clean_sales = clean_sales[~cancelled].copy()

# Step 10: Remove invalid quantities and prices
clean_sales = clean_sales[
    (clean_sales["Quantity"] > 0) &
    (clean_sales["UnitPrice"] > 0)
].copy()

# Step 11: Calculate sales revenue
clean_sales["Revenue"] = (
    clean_sales["Quantity"] * clean_sales["UnitPrice"]
)

# Step 12: Save the cleaned dataset
clean_sales.to_csv("Data/cleaned_retail_sales.csv", index=False)

# Step 13: Check the cleaned results
print("\nCLEANED DATASET SIZE:")
print(clean_sales.shape)

print("\nTOTAL SALES REVENUE:")
print(f"£{clean_sales['Revenue'].sum():,.2f}")

print("\nCLEANED DATASET SAVED SUCCESSFULLY!")
