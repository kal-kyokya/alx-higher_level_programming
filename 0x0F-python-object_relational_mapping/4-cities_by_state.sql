-- Create and insert rows in states and cities Table for a Database x.

-- Database creation command
CREATE DATABASE
IF NOT EXISTS hbtn_0e_4_usa;

-- Set Database for usage
USE hbtn_0e_4_usa;

-- Command for states Table Creation
CREATE TABLE
IF NOT EXISTS states (
   id INT     NOT NULL AUTO_INCREMENT,
   name VARCHAR(256),
   PRIMARY KEY (id)
);

-- Cities Table creation command
CREATE TABLE
IF NOT EXISTS cities (
   id INT     NOT NULL AUTO_INCREMENT,
   state_id INT,
   name VARCHAR(256),
   PRIMARY KEY (id),
   FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Command for data insertion in states
INSERT INTO states (name)
VALUES ("Congo"), ("Kenya"), ("Rwanda"),
       ("Burundi"), ("Uganda"), ("Tanzania"),
       ("Nigeria"), ("Zambia"), ("Zimbabwe"),
       ("Tchad"), ("Somaliland"), ("Ethiopia");

-- Command for insertion of data in cities table
INSERT INTO cities (state_id, name)
VALUES (1, "Kinshasa"), (2, "Nairobi"), (3, "Kigali"),
       (4, "Bujumbura"), (5, "Kampala"), (6, "Dodoma"),
       (7, "Lagos"), (8, "Lusaka"), (9, "Harare"),
       (10, "N`Djamena"), (11, "Hargeysa"), (12, "Addis-Ababa");

-- Show structure of Database's tables
SHOW CREATE TABLE states;
SHOW CREATE TABLE cities;
