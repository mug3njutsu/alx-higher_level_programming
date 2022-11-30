-- Creates database htbn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
        id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
        name varchar(256) NOT NULL,
);
