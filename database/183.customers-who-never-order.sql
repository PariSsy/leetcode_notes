/* [183] Customers Who Never Order */

-- MySQL, my solution (380ms, 97%)
select Name as Customers
from Customers c
left join Orders o on c.Id = o.CustomerId
where CustomerId is NULL;

-- MySQL, solution 2 (427ms, 73%)
SELECT A.Name as Customers
from Customers A
WHERE NOT EXISTS (SELECT 1 FROM Orders B WHERE A.Id = B.CustomerId limit 1)