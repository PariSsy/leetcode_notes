/* [182] Duplicate Emails */

-- MySQL, brute force (433ms, 17%)
select Email
from (
    select Email, count(Id)
    from Person
    group by Email
    having count(Id) > 1
) t
;

-- MySQL, simplified (305ms, 69%)
select Email
from Person
group by Email
having count(Id) > 1
;

-- MySQL, self join
 SELECT DISTINCT a.Email
 FROM Person a JOIN Person b
 ON (a.Email = b.Email)
 WHERE a.Id <> b.Id
;