-- Script displaying all granted privileges to user John Doe.

-- Command doing the display
SELECT GRANT PRIVILEGES
ON *.*
TO 'user_0d_1'@'localhost'
AND
GRANT PRIVILEGES
ON *.*
TO 'user_0d_2'@'localhost';
