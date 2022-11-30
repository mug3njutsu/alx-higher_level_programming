-- Lists all the cities contained in htbn_0d_usa
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities ON cities.state_id=states.id
ORDER BY cities.id ASC;
