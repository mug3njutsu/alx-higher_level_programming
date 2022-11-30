-- Creates Db hbtn_0d_usa and table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name varchar(256),
	UNIQUE (id),
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES states(id)
)
