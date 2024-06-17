-- Script printing all rows of a defined field

-- Command for printing
SELECT `id` FROM `states`
UNION
SELECT `id` FROM `cities`
ORDER BY `cities`.`id`;
