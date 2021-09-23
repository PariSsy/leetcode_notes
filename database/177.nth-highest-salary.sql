/* [177] Nth Highest Salary */

-- MySQL, Solution 1
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1; -- No calculation can happen in the argument
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1
  );
END

-- MySQL, Solution 2
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
RETURN (
  select distinct e1.salary
  from Employee e1
  where N-1 = (
    select count(distinct e2.Salary)
    from Employee e2
    where e1.Salary < e2.Salary
  )
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

