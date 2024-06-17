-- Script subquerying two 2 tables

-- Command for printing result
SELECT `cities`.`id`, `cities`.`name`
FROM `cities`
WHERE `id` IN (
      SELECT id FROM `states`
)
ORDER BY `cities`.`id`;
