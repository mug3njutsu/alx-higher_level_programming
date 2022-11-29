SELECT score, COUNT(score) as number FROM contacts GROUP BY score HAVING COUNT(score) > 1
ORDER BY number DESC;
