-- Creates table unique_id
CREATE TABLE IF NOT EXISTS unique_id(
	id INT NOT NULL UNIQUE,
	name varchar(256)
)
ALTER TABLE unique_id ALTER id SET DEFAULT 1;
