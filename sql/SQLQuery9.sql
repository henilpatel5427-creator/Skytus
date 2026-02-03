--1 Create Database

CREATE DATABASE company_db;
GO
USE company_db;
GO

--2️ Create employees Table

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT,
    hire_date DATE
);

--3️ Insert Sample Data (with duplicates + dates)

INSERT INTO employees VALUES
(1, 'Henil', 1, 60000, '2024-12-01'),
(2, 'Urva', 1, 75000, '2024-10-15'),
(3, 'Darshil', 2, 60000, '2023-08-10'),
(4, 'Jems', 2, 90000, '2024-11-20'),
(5, 'Dixit', 1, 60000, '2024-12-01'), -- duplicate
(6, 'Manish', 3, 50000, '2025-01-05');

--4️ Create Two Tables (for COMMON RECORDS)

CREATE TABLE employees_old (
    emp_id INT,
    emp_name VARCHAR(50)
);

CREATE TABLE employees_new (
    emp_id INT,
    emp_name VARCHAR(50)
);

INSERT INTO employees_old VALUES
(1, 'HENIL'),
(2, 'Darshil'),
(3, 'Dixit');

INSERT INTO employees_new VALUES
(2, 'Urva'),
(3, 'Darshil'),
(4, 'Jems');

--5️ Create logs Table

CREATE TABLE logs (
    id INT PRIMARY KEY,
    value INT
);

INSERT INTO logs VALUES
(1, 10),
(2, 10),
(3, 20),
(4, 30),
(5, 30),
(6, 30),
(7, 40),

WITH cte AS (
    SELECT *,
           LAG(value) OVER (ORDER BY id) AS prev_value
    FROM logs
)
DELETE FROM cte
WHERE value = prev_value;

select * from logs ;