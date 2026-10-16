
import sqlite3
import pandas as pd

# Step 1: Load the retail sales dataset
sales = pd.read_csv("Data/retail_sales.csv")

# Step 2: Calculate revenue for each transaction
sales["revenue"] = sales["quantity"] * sales["unit_price"]

# Step 3: Create a local SQLite database
connection = sqlite3.connect("retail_analytics.db")

# Step 4: Store our sales data in a database table
sales.to_sql("sales", connection, if_exists="replace", index=False)

# Step 5: Analyse revenue by category using SQL
query = """
SELECT
    category,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;
"""

results = pd.read_sql_query(query, connection)

print("REVENUE BY CATEGORY (SQL):")
print(results)

# Step 6: Close the database connection
connection.close()
