--1️ Create Database

 DATABASE company_db;

--2 Create departments Table
USE company_db;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);
--3️ Create employees Table

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

--4️ Insert Data into departments

INSERT INTO departments VALUES
(1, 'Computer'),
(2, 'IT'),
(3, 'Finance'),
(4, 'Computer');

--5️ Insert Data into employees

INSERT INTO employees VALUES
(101, 'Henil', 2, 60000),
(102, 'Jems', 2, 55000),
(103, 'Urva', 3, 48000),
(104, 'Darshil', 1, 52000),
(105, 'Aryan', 2, 70000),
(106, 'Dixit', NULL, 45000);


--1️⃣ Display employee name with department name

SELECT e.emp_name, d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;

--2️⃣ Display employees earning more than 50,000

SELECT emp_name, salary
FROM employees
WHERE salary > 50000;

--3️⃣ Display department-wise total salary

SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

--4️⃣ Display departments with more than 2 employees

SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2;

--5️⃣ Display employees without a department

SELECT emp_name
FROM employees
WHERE dept_id IS NULL;
