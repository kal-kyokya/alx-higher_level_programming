-- Create a Database, sets it as 'in use', Add a table to it with associated values

-- Database creation
CREATE DATABASE
IF NOT EXISTS hbtn_0e_0_usa;

-- Setting created Database 'in use'
USE hbtn_0e_0_usa;

-- Table creation
CREATE TABLE
IF NOT EXISTS states (
   id INT     NOT NULL AUTO_INCREMENT,
   name VARCHAR(256)   NOT NULL,
   PRIMARY KEY (id)
);

-- Rows/Record addition to Table
INSERT INTO states (name)
VALUES ("Congo"), ("Kenya"), ("Rwanda"),
       ("Burundi"), ("Uganda"), ("Tanzania"),
       ("Nigeria"), ("Zambia"), ("Zimbabwe"),
       ("Tchad"), ("Somaliland"), ("Ethiopia");

-- Show structure of database's tables
SHOW CREATE TABLE states;
