/* [569. Median Employee Salary] */

-- My MySQL solution (278 ms, 75%)
with cte1 as (
    select Id, Company, Salary, rank() over (partition by Company order by Salary) as rk
    from Employee
)
, cte2 as (
    select Company, max(rk) as max_rank
    from cte1
    group by Company
)
, cte3 as (
    select c1.*, max_rank
    from cte1 c1
    left join cte2 c2 using(Company)
)
, cte4 as (
    select Id, Company, Salary
    from cte3
    where (
        max_rank % 2 = 0 and ((rk = max_rank/2) or (rk = max_rank/2 + 1))
    ) or (
        max_rank % 2 != 0 and rk = ceiling(max_rank/2)
    )
)
select min(Id) as Id, Company, Salary
from cte4
group by Company, Salary


-- MySQL solution in a better structure (322 ms, 46%)
with cte as (
    select *,
      row_number() over (partition by company order by salary) as row_id,
      count(salary) over (partition by company) as cnt
    from employee)
select id, company, salary
from cte
where row_id between cnt/2.0 and cnt/2.0+1;


-- MSSQL solution (1132 ms, 90%)
SELECT Id, Company, Salary
FROM (
    SELECT *,
      ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary ASC, Id ASC) AS RN_ASC,
      ROW_NUMBER() OVER(PARTITION BY COMPANY ORDER BY Salary DESC, Id DESC) AS RN_DESC
    FROM Employee) AS temp
WHERE ABS(RN_ASC-RN_DESC) BETWEEN 0 AND 1
ORDER BY Company, Salary;


-- MySQL solution 2 (1409 ms, 5%)
-- This solution will execute in MSSQL, but return a wrong answer
SELECT MIN(A.Id) AS Id, A.Company, A.Salary
FROM Employee A, Employee B
WHERE A.Company = B.Company
GROUP BY A.Company, A.Salary
HAVING SUM(CASE WHEN B.Salary >= A.Salary then 1 ELSE 0 END) >= COUNT(*)/2
AND SUM(CASE WHEN B.Salary <= A.Salary then 1 ELSE 0 END) >= COUNT(*)/2