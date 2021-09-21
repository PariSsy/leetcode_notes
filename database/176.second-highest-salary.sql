/* [175] Second Highest Salary */


-- MySQL
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)


-- MSSQL
WITH cte AS
(SELECT *,
  RANK() OVER (ORDER BY Salary DESC) AS rank
FROM Employee)
SELECT MAX(Salary) AS SecondHighestSalary
FROM cte
WHERE rank = 2