-- Create a new schema named finance_ml
CREATE SCHEMA IF NOT EXISTS mlops;

-- Create a new table named stock_data in the mlops schema
CREATE TABLE IF NOT EXISTS mlops.stock_data (
  id SERIAL PRIMARY KEY,
  stock_code VARCHAR(255) NOT NULL,
  stock_name VARCHAR(255) NOT NULL,
  status VARCHAR(255) NOT NULL,
  latest_dataset VARCHAR(255) NOT NULL
);

INSERT INTO mlops.stock_data(stock_code, stock_name, status, latest_dataset)
VALUES ('EGIE3.SA', 'ENGIE BRASIL', 'true', 'test');