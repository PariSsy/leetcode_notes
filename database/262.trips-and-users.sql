/* [262] Trips and Users */

-- 389 ms (96.6%)
with cte as (
    select Users_Id from Users where Banned = 'No'
)

select
  Request_at as Day,
  round(sum(case when Status != 'completed' then 1 else 0 end) / count(Id), 2) as `Cancellation Rate`
from Trips t
where (Request_at between date '2013-10-01' and date '2013-10-03')
  and Client_Id in (select Users_Id from cte)
  and Driver_Id in (select Users_Id from cte)
group by Request_at

-- 452 ms (64%)
with cte as (
    select Users_Id from Users where Banned = 'No'
)

select
  Request_at as Day,
  round(count(case when Status != 'completed' then 1 end) / count(Id), 2) as `Cancellation Rate`
from Trips t
where (Request_at between date '2013-10-01' and date '2013-10-03')
  and Client_Id in (select Users_Id from cte)
  and Driver_Id in (select Users_Id from cte)
group by Request_at


-- 519 ms (36%)
select
  Request_at as Day,
  round(count(case when Status != 'completed' then 1 end) / count(Id), 2) as `Cancellation Rate`
from Trips t
where (Request_at between date '2013-10-01' and date '2013-10-03')
  and Client_Id in (select Users_Id from Users where Banned = 'No')
  and Driver_Id in (select Users_Id from Users where Banned = 'No')
group by Request_at

--
with cte as (
    select Users_Id from Users where Banned = 'No'
)

select
  Request_at as Day,
  round(sum(case when Status != 'completed' then 1 else 0 end) / count(Id), 2) as `Cancellation Rate`
from Trips t
where (Request_at between date '2013-10-01' and date '2013-10-03')
  and Client_Id in (select Users_Id from cte)
  and Driver_Id in (select Users_Id from cte)
group by Request_at

