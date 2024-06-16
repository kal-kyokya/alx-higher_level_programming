-- Script creating a Database and a User with 'SELECT' granted.

-- Command for Database creation
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';

-- Command creating the User
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Command granting 'SELECT' to User.
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
