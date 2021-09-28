/* [196] Delete Duplicate Emails */

-- My mysql solution (web 461ms, 99.6%), optimal
with cte as (
    select min(Id) as Id
    from Person
    group by Email
)

delete from Person
where Id not in (select Id from cte);

-- Solution 2, mysql (vs code 942ms, 96%)
DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND
p1.Id > p2.Id



