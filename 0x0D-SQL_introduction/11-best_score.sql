-- Script listing table elements in specific range

-- Command doing the listing
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
