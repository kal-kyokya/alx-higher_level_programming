-- Script printing all rows of a defined field

-- Command for printing
SELECT * FROM `states`
UNION
SELECT * FROM `cities`
ORDER BY `cities`.`id`;
