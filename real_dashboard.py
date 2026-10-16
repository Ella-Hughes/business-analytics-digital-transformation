
import pandas as pd
import streamlit as st

# Step 1: Configure the dashboard
st.set_page_config(
    page_title="Retail Business Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("Retail Business Intelligence Dashboard")
st.write(
    "Analysing real retail transactions to support "
    "data-driven business decisions."
)

# Step 2: Load the cleaned retail dataset
# Step 2: Load the cleaned retail dataset
@st.cache_data
def load_data():
    data = pd.read_csv(
        "Data/cleaned_retail_sales.csv",
        dtype={"InvoiceNo": str},
        parse_dates=["InvoiceDate"]
    )
    return data

sales = load_data()

# Step 3: Create country filters
countries = sorted(sales["Country"].dropna().unique())

selected_countries = st.multiselect(
    "Select countries:",
    options=countries,
    default=["United Kingdom"]
)

filtered_sales = sales[
    sales["Country"].isin(selected_countries)
].copy()

# Step 4: Calculate business metrics
total_revenue = filtered_sales["Revenue"].sum()
total_orders = filtered_sales["InvoiceNo"].nunique()
units_sold = filtered_sales["Quantity"].sum()

# Step 5: Display KPI metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"£{total_revenue:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Units Sold", f"{units_sold:,}")

# Step 6: Monthly revenue analysis
st.subheader("Monthly Revenue Trend")

monthly_revenue = (
    filtered_sales.set_index("InvoiceDate")
    .resample("MS")["Revenue"]
    .sum()
)

st.line_chart(monthly_revenue)

# Step 7: Top 10 products
st.subheader("Top 10 Products by Revenue")

top_products = (
    filtered_sales.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)

# Step 8: Country revenue comparison
st.subheader("Revenue by Country")

country_revenue = (
    filtered_sales.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(country_revenue)

# Step 9: Display sample transactions
st.subheader("Sample Sales Transactions")
st.dataframe(filtered_sales.head(100), width="stretch")

# Step 10: Generate business insights
st.subheader("Business Performance Insights")

if not filtered_sales.empty:
    top_product = top_products.idxmax()
    top_product_revenue = top_products.max()

    st.success(
        f"Highest-revenue product: {top_product} "
        f"(£{top_product_revenue:,.2f})."
    )

    st.write(
        "Recommendation: Investigate demand patterns, "
        "profit margins and stock availability for "
        "high-revenue products before making "
        "inventory or investment decisions."
    )
else:
    st.info("Select at least one country to view insights.")
