-- Script creating a mysql user

-- Command for user creation
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Command granting all privileges to create user
GRANT ALL PRIVILEGES *.* TO 'user_0d_1'@'localhost';
