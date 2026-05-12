# Sales Data Analysis and Reporting for a Retail Chain
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from scipy import stats

# PHASE 1: DATA COLLECTION

trxn = pd.read_csv('Retail_Data_Transactions.csv')
response = pd.read_csv('Retail_Data_Response.csv')
# Merge on customer_id
df = trxn.merge(response, on='customer_id', how='left')
print("Shape:", df.shape)
print("Data Types:\n", df.dtypes)
print("Summary:\n", df.describe())

# PHASE 2: DATA CLEANING & PREPARATION

# Check and handle missing values
print("\nMissing Values:\n", df.isnull().sum())
df = df.dropna()
# Fix data types
df['trans_date'] = pd.to_datetime(df['trans_date'])
df['response'] = df['response'].astype('int64')
# Outlier detection using Z-score
z_score = np.abs(stats.zscore(df['tran_amount']))
threshold = 3
outliers = z_score > threshold
print(f"\nOutliers detected: {outliers.sum()}")
print(df[outliers])
# Visualize distribution with boxplot
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['tran_amount'])
plt.title('Transaction Amount Distribution (Boxplot)')
plt.tight_layout()
plt.savefig('outputs/boxplot_tran_amount.png')
plt.close()
# Create derived columns
df['month'] = df['trans_date'].dt.month
df['month_year'] = df['trans_date'].dt.to_period('M')

# PHASE 3: DATA ANALYSIS

# Top 3 Months by Total Sales 
monthly_sales = df.groupby('month')['tran_amount'].sum()
top_3_months = monthly_sales.sort_values(ascending=False).reset_index().head(3)
print("\nTop 3 Months by Sales:\n", top_3_months)
# Top 5 Customers by Order Frequency
customer_counts = df['customer_id'].value_counts().reset_index()
customer_counts.columns = ['customer_id', 'count']
top_5_freq = customer_counts.head(5)
print("\nTop 5 Customers by Frequency:\n", top_5_freq)
plt.figure(figsize=(8, 5))
sns.barplot(x='customer_id', y='count', data=top_5_freq)
plt.title('Top 5 Customers by Order Frequency')
plt.xlabel('Customer ID')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/top5_customers_frequency.png')
plt.close()
# Top 5 Customers by Transaction Value
customer_sales = df.groupby('customer_id')['tran_amount'].sum().reset_index()
top_5_value = customer_sales.sort_values(by='tran_amount', ascending=False).head(5)
print("\nTop 5 Customers by Sales Value:\n", top_5_value)
plt.figure(figsize=(8, 5))
sns.barplot(x='customer_id', y='tran_amount', data=top_5_value)
plt.title('Top 5 Customers by Total Transaction Value')
plt.xlabel('Customer ID')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/top5_customers_value.png')
plt.close()
# Time Series Analysis
monthly_ts = df.groupby('month_year')['tran_amount'].sum()
monthly_ts.index = monthly_ts.index.to_timestamp()
plt.figure(figsize=(12, 6))
plt.plot(monthly_ts.index, monthly_ts.values, color='steelblue', linewidth=2)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
plt.xlabel('Month-Year')
plt.ylabel('Total Sales')
plt.title('Monthly Sales Trend (Time Series)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/monthly_sales_trend.png')
plt.close()
# RFM Customer Segmentation
recency = df.groupby('customer_id')['trans_date'].max()
frequency = df.groupby('customer_id')['trans_date'].count()
monetary = df.groupby('customer_id')['tran_amount'].sum()
rfm = pd.DataFrame({
    'recency': recency,
    'frequency': frequency,
    'monetary': monetary
})
def segment_customer(row):
    if row['recency'].year >= 2012 and row['frequency'] >= 15 and row['monetary'] > 1000:
        return 'P0'
    elif (2011 <= row['recency'].year < 2012) and (10 < row['frequency'] < 15) and (500 < row['monetary'] <= 1000):
        return 'P1'
    else:
        return 'P2'
rfm['segment'] = rfm.apply(segment_customer, axis=1)
print("\nRFM Segmentation:\n", rfm['segment'].value_counts())
# Churn Analysis
churn_counts = df['response'].value_counts()
plt.figure(figsize=(6, 4))
churn_counts.plot(kind='bar', color=['salmon', 'steelblue'])
plt.title('Churn vs Active Customers')
plt.xlabel('Response (0 = Churned, 1 = Active)')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('outputs/churn_analysis.png')
plt.close()
# Top 5 Customers Monthly Sales Trend 
top_5_ids = monetary.sort_values(ascending=False).head(5).index
top_df = df[df['customer_id'].isin(top_5_ids)]
top_sales = top_df.groupby(['customer_id', 'month_year'])['tran_amount'].sum().unstack(level=0)
top_sales.index = top_sales.index.to_timestamp()
top_sales.plot(kind='line', figsize=(12, 6))
plt.title('Monthly Sales Trend - Top 5 Customers')
plt.xlabel('Month-Year')
plt.ylabel('Transaction Amount')
plt.tight_layout()
plt.savefig('outputs/top5_monthly_trend.png')
plt.close()

# PHASE 4: EXPORT OUTPUTS

df.to_csv('outputs/MainData.csv', index=False)
rfm.to_csv('outputs/AddAnlys.csv')
print("\n Analysis complete. Outputs saved to /outputs/")