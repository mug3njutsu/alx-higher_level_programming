-- Creates the table id_not_null
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT,
	name varchar(256)
)
ALTER TABLE id_not_null ALTER COLUMN id SET DEFAULT 1;
