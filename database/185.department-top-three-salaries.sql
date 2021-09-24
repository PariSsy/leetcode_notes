/* [185] Department Top Three Salaries */

-- MySQL, my solution 1 using dense_rank (620ms, 89%)
select distinct d.Name as Department, e.Name as Employee, e.Salary
from Employee e
inner join (
    select DepartmentId, Salary, dense_rank() over (partition by DepartmentId order by Salary desc) as rk
    from Employee
) t using (DepartmentId, Salary)
left join Department d on e.DepartmentId = d.Id
where rk <= 3

-- MySQL, my solution 2 using rank (661ms, 77%)
select d.Name as Department, e.Name as Employee, e.Salary
from Employee e
inner join (
    select DepartmentId, Salary, rank() over (partition by DepartmentId order by Salary desc) as rk
    from (
        select distinct DepartmentId, Salary
        from Employee
    ) t1
) t2 using (DepartmentId, Salary)
left join Department d on e.DepartmentId = d.Id
where rk <= 3