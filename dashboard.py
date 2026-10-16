
import pandas as pd
import streamlit as st

# Step 1: Set up the dashboard
st.set_page_config(
    page_title="Retail Business Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("Retail Business Analytics Dashboard")
st.write("Exploring sales performance to support business decisions.")

# Step 2: Load the retail dataset
sales = pd.read_csv("Data/retail_sales.csv")

# Step 3: Prepare the data
sales["date"] = pd.to_datetime(sales["date"])
sales["revenue"] = sales["quantity"] * sales["unit_price"]

# Step 4: Create an interactive category filter
categories = sorted(sales["category"].unique())

selected_categories = st.multiselect(
    "Select product categories:",
    options=categories,
    default=categories
)

filtered_sales = sales[
    sales["category"].isin(selected_categories)
]

# Step 5: Calculate business performance metrics
total_revenue = filtered_sales["revenue"].sum()
total_orders = filtered_sales["order_id"].nunique()
units_sold = filtered_sales["quantity"].sum()

# Step 6: Display key business metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"£{total_revenue:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Units Sold", units_sold)

# Step 7: Display revenue by category
st.subheader("Revenue by Product Category")

category_revenue = (
    filtered_sales.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_revenue)

# Step 8: Display monthly revenue trends
st.subheader("Monthly Revenue Trend")

monthly_revenue = (
    filtered_sales.set_index("date")
    .resample("MS")["revenue"]
    .sum()
)

st.line_chart(monthly_revenue)

# Step 9: Display the underlying sales data
st.subheader("Sales Transactions")
st.dataframe(filtered_sales, width="stretch")

# Step 10: Generate business insights
st.subheader("Business Performance Insights")

if not filtered_sales.empty:
    top_category = category_revenue.idxmax()
    top_revenue = category_revenue.max()

    st.success(
        f"Top-performing category: {top_category} "
        f"with £{top_revenue:,.2f} in revenue."
    )

    st.write(
        "Business recommendation: Investigate the "
        "performance of this category, including "
        "profit margins, customer demand and "
        "inventory requirements before making "
        "investment decisions."
    )
else:
    st.info("Select at least one category to view insights.")
