/* [180] Consecutive Numbers */

-- MySQL, solution 1
with cte as
(
    select
      Num, lag(Num,1) over (order by Id) as Num1, lag(Num,2) over (order by Id) as Num2
    from `Logs` -- MySQL needs to distinguish between variable name and default function
)
select distinct(Num) as ConsecutiveNums
from (
    select Num, Num - Num1 as diff1, Num - Num2 as diff2
    from cte
) t
where diff1 = 0 and diff2 = 0


-- MSSQL
with cte as
(
    select
      Num, lag(Num,1) over (order by Id) as Num1, lag(Num,2) over (order by Id) as Num2
    from Logs
)
select distinct(Num) as ConsecutiveNums
from (
    select Num, Num - Num1 as diff1, Num - Num2 as diff2
    from cte
) t
where diff1 = 0
and diff2 = 0


-- MySQL, solution 2 - User defined variables
select distinct num ConsecutiveNums
from (
  select num, case
    when @record=num then @count:=@count+1
		when @record:=num then @count:=1 end as n
  from logs , (select @count:=0, @record:=null) r
) a
where a.n >= 3;