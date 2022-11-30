-- Lists all the cities of California
SELECT id,name FROM cities WHERE states.name = "California";
ORDER BY id ASC;
