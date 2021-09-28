/* [197] Rising Temperature */


-- mysql Solution 1 (326ms, 90%)

SELECT w1.Id FROM Weather w1, Weather w2
WHERE subdate(w1.RecordDate, 1) = w2.RecordDate
  AND w1.Temperature > w2.Temperature

-- mysql Solution 2 (461ms, 44%)
SELECT w2.Id
FROM Weather w1, Weather w2 
WHERE w2.RecordDate = DATE_ADD(w1.RecordDate, INTERVAL 1 DAY) 
AND w2.Temperature > w1.Temperature;