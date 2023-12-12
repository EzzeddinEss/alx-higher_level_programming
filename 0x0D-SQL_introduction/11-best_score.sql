-- This script retrieves all records from the table and 
-- orders them according to a specified criteria.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
