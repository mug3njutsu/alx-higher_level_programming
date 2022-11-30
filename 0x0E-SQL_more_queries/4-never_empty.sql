-- Creates the table id_not_null
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT,
	name varchar(256)
)
ALTER TABLE id_not_null ALTER id SET DEFAULT 1;
