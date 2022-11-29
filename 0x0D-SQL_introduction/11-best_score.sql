-- Lists all records with a score >= 10 in second_table
SELECT (score, name) FROM hbtn_0c_0.second_table
ORDER BY score DESC
WHERE score>=10;
