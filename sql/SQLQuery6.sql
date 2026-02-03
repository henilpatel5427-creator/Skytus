--1️ Create Database

CREATE DATABASE statebank_db;
USE statebank_db;

--2️ Create accounts Table

CREATE TABLE accounts (
    acc_id INT PRIMARY KEY,
    acc_name VARCHAR(50),
    balance INT
);

--3 Insert Initial Records

INSERT INTO accounts VALUES
(101, 'Henil', 450000),
(102, 'Urva', 900000);

--4️ Start Transaction + Insert + Rollback

BEGIN TRANSACTION;

INSERT INTO accounts VALUES (103, 'Darshil', 40000);

ROLLBACK;

--5️ Start Transaction + Insert + Commit

BEGIN TRANSACTION;

INSERT INTO accounts VALUES (103, 'Darshil', 40000);

COMMIT;

--6️ Transfer Money Using Transaction

BEGIN TRANSACTION;

UPDATE accounts
SET balance = balance - 5000
WHERE acc_id = 101;

UPDATE accounts
SET balance = balance + 5000
WHERE acc_id = 102;

COMMIT;

--7️ Final Data

SELECT * FROM accounts;




