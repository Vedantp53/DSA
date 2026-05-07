-- Last updated: 5/8/2026, 3:50:11 AM
# Write your MySQL query statement below
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(id) > 1;
