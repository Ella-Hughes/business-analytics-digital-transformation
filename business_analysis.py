
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Step 1: Load our cleaned retail dataset
sales = pd.read_csv(
    "Data/cleaned_retail_sales.csv",
    parse_dates=["InvoiceDate"]
)

# Step 2: Create a folder for our new charts
output_folder = Path("visualisations")
output_folder.mkdir(exist_ok=True)

# Step 3: Calculate monthly revenue
monthly_revenue = (
    sales.set_index("InvoiceDate")
    .resample("MS")["Revenue"]
    .sum()
)

print("\nMONTHLY REVENUE:")
print(monthly_revenue)

# Step 4: Create a monthly revenue chart
plt.figure(figsize=(10, 5))
monthly_revenue.plot(marker="o")

plt.title("Monthly Retail Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.tight_layout()

plt.savefig(
    output_folder / "real_monthly_revenue.png",
    dpi=300
)
plt.close()

# Step 5: Find the top 10 products by revenue
top_products = (
    sales.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS BY REVENUE:")
print(top_products)

# Step 6: Create a top products chart
plt.figure(figsize=(11, 6))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig(
    output_folder / "top_products_revenue.png",
    dpi=300
)
plt.close()

# Step 7: Find the top 10 countries by revenue
top_countries = (
    sales.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 COUNTRIES BY REVENUE:")
print(top_countries)

# Step 8: Create a country revenue chart
plt.figure(figsize=(10, 6))
top_countries.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(
    output_folder / "top_countries_revenue.png",
    dpi=300
)
plt.close()

print("\nBUSINESS ANALYSIS COMPLETE!")
print("Three new charts saved in visualisations.")
