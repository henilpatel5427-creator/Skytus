--1️ Add index to improve search on orders.customer_id

CREATE INDEX idx_orders_customer_id
ON orders(customer_id);

--2️ Use EXPLAIN to analyze a query
SET STATISTICS PROFILE ON;
GO

SELECT c.name, o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.customer_id = 1;
GO

SET STATISTICS PROFILE OFF;
GO


--3️ Optimize a slow JOIN query

SELECT c.name, o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.customer_id = 1;


