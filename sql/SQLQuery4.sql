--1️ Find employees earning more than average salary

SELECT emp_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);

--2️ Find department with highest total salary

SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total_salary DESC



--3️ Display employee with second highest salary

SELECT emp_name, salary
FROM employees
ORDER BY salary DESC
 

--4️ Display employees working in same department as "Amit"

SELECT emp_name
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Jems'
)
AND emp_name <> 'Jems';
