/* [184] Department Highest Salary */

-- MySQL, my solution (484ms, 96%)
select d.Name as Department, e.Name as Employee, e.Salary
from Employee e
inner join (
    select DepartmentId, max(Salary) as Salary
    from Employee
    group by DepartmentId
) t using(DepartmentId, Salary)
left join Department d on e.DepartmentId = d.Id
;