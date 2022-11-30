-- Creates table unique_id
CREATE TABLE IF NOT EXISTS unique_id(
	id INT,
	name varchar(256),
	UNIQUE (ID)
)
ALTER TABLE unique_id ALTER id SET DEFAULT 1;
