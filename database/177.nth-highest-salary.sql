/* [177] Nth Highest Salary */


-- MySQL
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1
  );
END


-- MSSQL
CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        SELECT MAX(Salary)
        FROM (
        SELECT *,
          DENSE_RANK() OVER (ORDER BY Salary DESC) AS rank
        FROM Employee
      ) t
      WHERE rank = @N
    );
END

