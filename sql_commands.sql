CREATE database RetailSalesData;
USE RetailSalesData;

CREATE TABLE Sales_Data_Transactions (
 customer_id VARCHAR(255),
 trans_date VARCHAR(255),
 tran_amount INT );
 
 CREATE TABLE Sales_Data_Response (
 customer_id VARCHAR(255) PRIMARY KEY,
 response INT );
 
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Retail_Data_Transactions.csv'
INTO TABLE Sales_Data_Transactions
FIELDS Terminated by ','
LINES Terminated by '\n'
IGNORE 1 ROWS;

 EXPLAIN SELECT * FROM Sales_Data_Transactions WHERE customer_id='CS5295';
 
 CREATE INDEX idx_id ON Sales_Data_Transactions(customer_id)
