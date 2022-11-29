-- Lists number of records with the same score in second_table
-- https://www.mysqltutorial.org/mysql-find-duplicate-values/
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY COUNT(*) DESC;
