create database student;
create table students(
student_id INT,
name VARCHAR(50),
department VARCHAR(30),
year INT,
marks INT
);

insert into students values
(1,'Henil','computer','5','90'),
(2,'Urva','IT','3','80'),
(3,'Darshil','Marketing','3','70'),
(4,'jems','IT','5','60'),
(5,'Dixit','COMPUTER','5','50');

--Tasks Display all student records 
Select * from students;

--Display only name and department 
select name, department from students;

--students( student_id INT, name VARCHAR(50), 
select student_id, name from students;

--department VARCHAR(30), year INT, marks INT ) 
select department,year,marks from students;

--Find students with marks greater than 75 
select * from students  where marks > 75;

--Display students from CSE department Sort students by marks (descending) 
select * from students order by marks desc;

--Display top 3 scorers	
select top 3 * from students order by marks desc;