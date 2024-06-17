-- Script subquerying two 2 tables

-- Command for printing result
SELECT `name`
FROM `cities`
WHERE `id` IN (
      SELECT id FROM `states`;
);
