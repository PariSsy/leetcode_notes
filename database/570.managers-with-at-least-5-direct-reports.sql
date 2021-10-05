/* 570. Managers with at least 5 direct report */

-- MySQL solution, optimal (231 ms, 99.6%)
select name from Employee
where Id in (
    select ManagerId from Employee
    group by ManagerId
    having count(ManagerId) >= 5
)

-- Wrong MySQL solution; prone to NULL
with cte as (
    select ManagerId, count(*) as ct
    from Employee
    where ManagerId is not null
    group by ManagerId
)

select e.Name
from cte c
left join Employee e on c.ManagerId = e.Id
where ct >= 5

Output:
{"headers": ["Name"], "values": [[""]]}
Expected:
{"headers": ["Name"], "values": []}