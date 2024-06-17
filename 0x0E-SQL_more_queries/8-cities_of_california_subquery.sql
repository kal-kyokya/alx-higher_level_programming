-- Script subquerying two 2 tables

-- Command for printing result
SELECT *
FROM `cities`
WHERE `cities`.`id` IN (
      SELECT `states`.`id` FROM `states`;
)
ORDER BY `cities`.`id`;
