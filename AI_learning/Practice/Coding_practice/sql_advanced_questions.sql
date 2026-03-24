-- Advanced SQL Interview Questions for 8+ Years Experience

-- 1. Write a query to find the second highest salary from the Employee table.
-- Answer:
SELECT MAX(salary) AS second_highest_salary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
-- Explanation: Finds the maximum salary less than the highest salary.

-- 2. Explain and demonstrate the use of window functions (ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD).
-- Answer:
SELECT *,
  ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn,
  RANK() OVER (ORDER BY salary DESC) AS rnk,
  DENSE_RANK() OVER (ORDER BY salary DESC) AS drnk,
  LAG(salary, 1) OVER (ORDER BY salary DESC) AS prev_salary,
  LEAD(salary, 1) OVER (ORDER BY salary DESC) AS next_salary
FROM Employee;
-- Explanation: Window functions allow calculations across rows related to the current row.

-- 3. How do you optimize a slow query? List steps and give an example.
-- Answer:
-- Steps: Analyze execution plan, add indexes, rewrite queries, avoid SELECT *, use joins efficiently, partition tables.
-- Example: Add index on WHERE clause column.
CREATE INDEX idx_emp_dept ON Employee(department_id);
-- Explanation: Indexes speed up lookups and filtering.

-- 4. Write a query to pivot data (rows to columns) and unpivot (columns to rows).
-- Answer (Pivot):
SELECT department,
  SUM(CASE WHEN gender = 'M' THEN 1 ELSE 0 END) AS male_count,
  SUM(CASE WHEN gender = 'F' THEN 1 ELSE 0 END) AS female_count
FROM Employee
GROUP BY department;
-- Answer (Unpivot):
SELECT department, 'M' AS gender, male_count AS count FROM DeptGender
UNION ALL
SELECT department, 'F', female_count FROM DeptGender;
-- Explanation: Pivot uses CASE, unpivot uses UNION ALL.

-- 5. Explain the difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN with examples.
-- Answer:
-- INNER JOIN: Returns rows with matching keys in both tables.
-- LEFT JOIN: Returns all rows from left table, matched rows from right.
-- RIGHT JOIN: All rows from right, matched from left.
-- FULL OUTER JOIN: All rows from both, matched where possible.
-- Example:
SELECT * FROM A INNER JOIN B ON A.id = B.id;
SELECT * FROM A LEFT JOIN B ON A.id = B.id;
SELECT * FROM A RIGHT JOIN B ON A.id = B.id;
SELECT * FROM A FULL OUTER JOIN B ON A.id = B.id;

-- 6. What is a CTE (Common Table Expression)? Write a recursive CTE to generate a hierarchy/tree structure.
-- Answer:
WITH RECURSIVE EmpCTE AS (
  SELECT id, name, manager_id FROM Employee WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id FROM Employee e
    JOIN EmpCTE c ON e.manager_id = c.id
)
SELECT * FROM EmpCTE;
-- Explanation: CTEs are temporary result sets. Recursive CTEs help with hierarchies.

-- 7. How do you handle duplicate records in a table? Write a query to delete duplicates but keep one.
-- Answer:
DELETE FROM Employee
WHERE rowid NOT IN (
  SELECT MIN(rowid) FROM Employee GROUP BY name, salary, department_id
);
-- Explanation: Keeps the first occurrence, deletes others.

-- 8. What are indexes? How do you decide which columns to index? Give an example of a composite index.
-- Answer:
-- Indexes speed up data retrieval. Index columns used in WHERE, JOIN, ORDER BY.
CREATE INDEX idx_emp_name_dept ON Employee(name, department_id);
-- Explanation: Composite index covers queries filtering by both columns.

-- 9. Explain ACID properties. How do you ensure transaction consistency in SQL?
-- Answer:
-- ACID: Atomicity, Consistency, Isolation, Durability.
-- Use BEGIN TRANSACTION, COMMIT, ROLLBACK to ensure consistency.
BEGIN TRANSACTION;
  -- SQL statements
COMMIT;

-- 10. Write a query to find gaps in a sequence (e.g., missing IDs in a table).
-- Answer:
SELECT t1.id + 1 AS missing_id
FROM Employee t1
LEFT JOIN Employee t2 ON t1.id + 1 = t2.id
WHERE t2.id IS NULL;
-- Explanation: Finds IDs where the next ID is missing.

-- 11. What is normalization and denormalization? When would you use each?
-- Answer:
-- Normalization: Organizing data to reduce redundancy (e.g., 3NF).
-- Denormalization: Combining tables for performance, at the cost of redundancy.
-- Use normalization for data integrity, denormalization for read performance.

-- 12. How do you perform bulk data loading efficiently? What are best practices?
-- Answer:
-- Use bulk load utilities (e.g., LOAD DATA INFILE in MySQL, bcp in SQL Server).
-- Disable indexes/constraints during load, batch commits, use staging tables.

-- 13. Write a query to get the running total and moving average of sales per month.
-- Answer:
SELECT month, sales,
  SUM(sales) OVER (ORDER BY month) AS running_total,
  AVG(sales) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM Sales;
-- Explanation: SUM/AVG with window functions for running/moving calculations.

-- 14. Explain the difference between clustered and non-clustered indexes.
-- Answer:
-- Clustered index: Sorts and stores data rows in table order (one per table).
-- Non-clustered: Separate structure, points to data rows (many per table).

-- 15. How do you handle schema changes in a production environment?
-- Answer:
-- Use migrations, version control, test in staging, schedule downtime if needed, backup before changes.

-- 16. What is a deadlock? How do you detect and resolve it?
-- Answer:
-- Deadlock: Two transactions block each other waiting for resources.
-- Detect via database logs, monitoring tools. Resolve by killing one transaction or using retry logic.

-- 17. Write a query to find all employees who have the same manager.
-- Answer:
SELECT manager_id, GROUP_CONCAT(name) AS employees
FROM Employee
GROUP BY manager_id
HAVING COUNT(*) > 1;
-- Explanation: Groups employees by manager, shows those with more than one report.

-- 18. How do you implement row-level security in SQL?
-- Answer:
-- Use views, user roles, or built-in RLS features (e.g., PostgreSQL RLS, SQL Server security policies).
-- Example: CREATE VIEW EmployeeView AS SELECT * FROM Employee WHERE department_id = CURRENT_USER_DEPT_ID;

-- 19. What are materialized views? When would you use them?
-- Answer:
-- Materialized views store the result of a query physically. Use for expensive queries that don't need real-time data.
-- Example: CREATE MATERIALIZED VIEW mv_sales AS SELECT * FROM Sales WHERE sale_date >= CURDATE() - INTERVAL 30 DAY;

-- 20. Explain the difference between UNION and UNION ALL with examples.
-- Answer:
-- UNION removes duplicates, UNION ALL keeps all rows.
SELECT name FROM A UNION SELECT name FROM B;
SELECT name FROM A UNION ALL SELECT name FROM B;
