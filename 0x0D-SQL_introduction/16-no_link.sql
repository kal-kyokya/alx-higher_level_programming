-- Script listing table's row with advanced requirements.

-- Command doing the listing
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
