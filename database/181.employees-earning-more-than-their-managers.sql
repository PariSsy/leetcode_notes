/* [181] Employees Earning More Than Their Managers */

-- MySQL, my solution (300ms; optimal)
select member as Employee
from (
    select e1.Id, e1.Name as member, e1.Salary as member_salary, e2.Salary as manager_salary
    from Employee e1
    left join Employee e2 on e1.ManagerId = e2.Id
    where e1.Salary > e2.Salary
) t


-- MSSQL, solution 1 (1035ms)
select E1.Name 
from Employee as E1, Employee as E2 
where E1.ManagerId = E2.Id and E1.Salary > E2.Salary

-- MSSQL, solution 2 (3340ms)
SELECT
     a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
     ON a.ManagerId = b.Id
     AND a.Salary > b.Salary
;