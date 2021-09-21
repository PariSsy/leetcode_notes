/* [178] Rank Scores */


-- MySQL
SELECT
  Score,
  (SELECT count(*)
   FROM (SELECT distinct Score s
         FROM Scores) tmp
   WHERE s >= Score) `Rank`
FROM Scores
ORDER BY Score desc


-- MSSQL
SELECT Score as score,
  DENSE_RANK() OVER (ORDER BY Score DESC) Rank
FROM Scores
ORDER by Rank


-- MySQL, User defined variables
SELECT
  Score,
  @rank := @rank + (@prev <> (@prev := Score)) `Rank`
FROM
  Scores,
  (SELECT @rank := 0, @prev := -1) init
ORDER BY Score desc