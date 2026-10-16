
print("Business Analytics & Digital Transformation")
print("Project setup successful!")

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load our retail sales dataset
sales = pd.read_csv("Data/retail_sales.csv")

# Step 2: Display the first five rows
print("FIRST FIVE ROWS:")
print(sales.head())

# Step 3: Check the size of the dataset
print("\nDATASET SIZE:")
print(sales.shape)

# Step 4: Calculate revenue for each order
sales["revenue"] = sales["quantity"] * sales["unit_price"]

print("\nSALES WITH REVENUE:")
print(sales)

# Step 5: Calculate total revenue
total_revenue = sales["revenue"].sum()

print("\nTOTAL BUSINESS REVENUE:")
print(f"£{total_revenue:,.2f}")

# Step 6: Calculate revenue by product category
category_revenue = sales.groupby("category")["revenue"].sum()

print("\nREVENUE BY CATEGORY:")
print(category_revenue.sort_values(ascending=False))

# Step 7: Visualise revenue by product category

# Sort categories from highest to lowest revenue
category_revenue = category_revenue.sort_values(ascending=False)

# Create a bar chart
plt.figure(figsize=(8, 5))

plt.bar(category_revenue.index, category_revenue.values)

# Add a title and axis labels
plt.title("Total Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue (£)")

# Make the chart easier to read
plt.tight_layout()

# Save the chart
plt.savefig("visualisations/revenue_by_category.png", dpi=300)

# Close the chart without opening a window
plt.close()

# Step 8: Convert the date column into datetime format
sales["date"] = pd.to_datetime(sales["date"])

# Extract the month from each transaction
sales["month"] = sales["date"].dt.to_period("M")

print("\nSALES DATA WITH MONTHS:")
print(sales[["date", "month", "revenue"]])

# Step 9: Calculate total revenue for each month
monthly_revenue = sales.groupby("month")["revenue"].sum()

print("\nMONTHLY REVENUE:")
print(monthly_revenue)

# Step 10: Create a monthly revenue trend chart
plt.figure(figsize=(8, 5))

plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Sales Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")

# Make the chart easier to read
plt.tight_layout()

# Save the monthly revenue chart
plt.savefig("visualisations/monthly_revenue_trend.png", dpi=300)

# Close the chart without opening a window
plt.close()



