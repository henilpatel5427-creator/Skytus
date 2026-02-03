--1 Create Database

CREATE DATABASE ecommerce_db;
USE ecommerce_db;

--2️ Create customers Table

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

--3️ Create orders Table

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

--4️ Create products Table

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price INT
);

--5️ Create order_items Table

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

--6️ Insert Data into customers

INSERT INTO customers VALUES
(1, 'Henil', 'Amadhara'),
(2, 'Urva', 'Amadhara'),
(3, 'Darshil', 'Amadhara'),
(4, 'Jems', 'Bilimora'),
(5, 'Dixit', 'Bilimora');

--7️ Insert Data into orders

INSERT INTO orders VALUES
(101, 1, '2024-01-10', 20000),
(102, 1, '2024-02-15', 18000),
(103, 2, '2024-02-20', 25000),
(104, 3, '2024-03-05', 30000),
(105, 2, '2024-03-18', 12000);

--8️ Insert Data into products

INSERT INTO products VALUES
(1, 'Laptop', 50000),
(2, 'Mobile', 20000),
(3, 'Headphones', 3000);

--9️ Insert Data into order_items

INSERT INTO order_items VALUES
(101, 1, 1),
(102, 2, 1),
(103, 2, 2),
(104, 1, 1),
(105, 3, 3);
 
 Select * from order_items