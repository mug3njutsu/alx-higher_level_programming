-- Lists all the cities contained in htbn_0d_usa
SELECT id,name FROM cities WHERE states.name = "California";
ORDER BY id ASC;
