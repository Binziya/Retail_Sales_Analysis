# Retail Transaction Data Analysis

## Project Overview
This project focuses on analyzing retail transaction data to understand customer purchasing behavior, sales performance, customer segmentation, and churn patterns using Python.

The analysis was performed using transaction records and customer response data to generate meaningful business insights and visualizations.

## Dataset

### Retail_Data_Transactions.csv
Contains:
- Customer ID
- Transaction Date
- Transaction Amount

### Retail_Data_Response.csv
Contains:
- Customer response data

The datasets were merged using the `customer_id` field.

## Tools and Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

# Project Workflow

## 1. Data Collection and Database Setup
- Imported retail transaction and response datasets
- Loaded CSV files into Python environment
- Merged datasets using `customer_id`

## 2. Data Cleaning and Preparation
- Checked missing values
- Removed null records
- Converted transaction date into datetime format
- Converted response column into integer type
- Performed outlier detection using Z-score analysis
- Created additional fields:
  - `month`
  - `month_year`

## 3. Data Analysis

The following analyses were performed:

- Monthly sales analysis
- Top customers by order frequency
- Top customers by transaction value
- Time-series sales trend analysis
- RFM customer segmentation
- Churn analysis
- Top customer monthly sales trend analysis

## 4. Reporting and Visualization

Generated outputs include:
- Transaction amount boxplot
- Customer frequency charts
- Customer sales value charts
- Monthly sales trend graphs
- Churn analysis graph
- Customer sales trend visualization

Exported files:
- `MainData.csv`
- `AddAnlys.csv`

## Key Insights

- Certain months recorded higher sales compared to others.
- A small group of customers contributed significantly to overall revenue.
- Loyal customers showed repeated purchasing behavior.
- RFM analysis identified different customer segments based on purchasing patterns.
- Churn analysis helped identify inactive customers.
- Outlier detection identified unusually high transaction amounts.

## Conclusion

The project successfully analyzed retail transaction data and generated business insights related to sales trends, customer behavior, customer segmentation, and customer retention. The analysis demonstrates the use of Python data analytics techniques for business understanding and decision-making.
