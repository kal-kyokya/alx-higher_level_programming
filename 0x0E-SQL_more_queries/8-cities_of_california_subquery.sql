-- Script subquerying two 2 tables

-- Command for printing result
SELECT *
FROM `cities`
WHERE `id` IN (
      SELECT id FROM `states`;
);
