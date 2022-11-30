-- Creates database htbn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states(
        id INT NOT NULL AUTO_INCREMENT,
        name varchar(256),
        UNIQUE (id),
        PRIMARY KEY (id)
)
