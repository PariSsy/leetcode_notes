/* [178] Rank Scores */

-- MySQL, Solution 1
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


-- MySQL, Solution 2 - User defined variables
SELECT
  Score,
  @rank := @rank + (@prev <> (@prev := Score)) `Rank`
FROM
  Scores,
  (SELECT @rank := 0, @prev := -1) init
ORDER BY Score desc


-- MySQL, Optimal solution 3 - user defined variables
SELECT Score, convert(Rank,SIGNED) AS Rank FROM
    (SELECT Score, @rank:=CASE WHEN Score=@previous THEN @rank ELSE @rank+1 END AS Rank, @previous:=Score FROM Scores,
        (SELECT @previous:=-1,@rank:=0) AS initial
    ORDER BY Score DESC) A;