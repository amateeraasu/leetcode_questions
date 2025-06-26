# Write your MySQL query statement below
SELECT e.name , bonus
FROM Employee as e 
LEFT JOIN Bonus as b 
ON e.empId = b.empID 
WHERE b.bonus < 1000 OR b.bonus is NULL;