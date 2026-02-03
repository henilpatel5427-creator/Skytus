--1️ Create Database

CREATE DATABASE shop_db;
USE shop_db;

--2️ Create users Table

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
);

--3️ Create orders Table

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    amount DECIMAL(10,2),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

--4️ Insert Sample Data into users

INSERT INTO users VALUES
(1, 'henil@gmail.com', 'henil123'),
(2, 'urva@gmail.com', 'urva123'),
(3, 'darshil@gmail.com', 'darshil123');

--5️ Insert Sample Data into orders

INSERT INTO orders VALUES
(101, '2024-01-10', 2500.00, 1),
(102, '2024-01-12', 1800.00, 1),
(103, '2024-01-15', 3200.00, 2);

--6️ Create Index on Email

CREATE INDEX idx_email
ON users(email);

--7️ Create View 

DROP VIEW IF EXISTS user_order_summary;


CREATE VIEW user_order_summary
AS
SELECT
    u.user_id,
    u.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.email;

--8️ Check View Output

SELECT * FROM user_order_summary;








