-- Create a new schema named finance_ml
CREATE SCHEMA IF NOT EXISTS finance_ml;

-- Create a new table named stock_data in the finance_ml schema
CREATE TABLE IF NOT EXISTS finance_ml.stock_data (
  id SERIAL PRIMARY KEY,
  stock_code VARCHAR(255) NOT NULL,
  stock_name VARCHAR(255) NOT NULL,
  status VARCHAR(255) NOT NULL,
  latest_dataset VARCHAR(255) NOT NULL
);