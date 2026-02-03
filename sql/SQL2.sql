use student ;

--1️ Count total number of student

SELECT COUNT (name) AS total_student
FROM students;

--2️ Find average marks of students

SELECT AVG(marks) AS average_marks
FROM students;

--3️ Find highest and lowest marks

SELECT 
    MAX(marks) AS highest_marks,
    MIN(marks) AS lowest_marks
FROM students;

--4️ Find department-wise average marks

SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department;

--5️ Display departments where average marks > 70

SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department
HAVING AVG(marks) > 70;


