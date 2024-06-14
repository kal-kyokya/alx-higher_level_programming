-- Script list count of rows with same field value

-- Command doing the listing
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
