-- Script creating a Database and its table

-- Command creating the Database
CREATE DATABASE
IF NOT EXISTS `hbtn_0d_usa`;

-- Command creating the table
CREATE TABLE
IF NOT EXISTS `hbtn_0d_usa`.`states` (
   id INT AUTO_INCREMENT NOT NULL,
   name VARCHAR(256) NOT NULL,
   PRIMARY KEY (id)
);
