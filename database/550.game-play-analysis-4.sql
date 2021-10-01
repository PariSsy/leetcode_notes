/* 550. Game play analysis IV */

-- MySQL approach 1, optimal (420 ms, 98%)
SELECT ROUND(SUM(CASE WHEN a.event_date + 1 = b.event_date THEN 1 ELSE 0 END)/COUNT(DISTINCT a.player_id), 2) AS fraction 
FROM (SELECT player_id, MIN(event_date) AS event_date
      FROM Activity 
      GROUP BY player_id) AS a JOIN Activity AS b 
ON a.player_id = b.player_id 

-- MySQL approach 2a (633 ms)
-- This approach makes an assumption that no player logs in twice on the same day.
select round((count(a.player_id)/count(t.player_id)), 2) as fraction
from (
    select player_id, min(event_date) as first_login
    from Activity group by player_id
) t
left join Activity a
on t.player_id = a.player_id and t.first_login = a.event_date - 1

-- MySQL approach 2b (660 ms)
select round((count(distinct a.player_id)/count(distinct t.player_id)), 2) as fraction
from (
    select player_id, min(event_date) as first_login
    from Activity group by player_id
) t
left join Activity a
on t.player_id = a.player_id and t.first_login = a.event_date - 1