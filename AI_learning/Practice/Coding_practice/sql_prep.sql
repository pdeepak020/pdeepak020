-- SQL Preparation Notes for Interviews
-- ===================================
-- Topics: Data Types, DDL, DML, DQL, Joins, Subqueries, Aggregations, Constraints, Indexes, Views, Transactions, Functions, Window Functions, and more.

-- 1. Data Types
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2),
    hire_date DATE,
    is_active BOOLEAN
);

-- 2. DDL (CREATE, ALTER, DROP, TRUNCATE)
CREATE TABLE departments (dept_id INT PRIMARY KEY, dept_name VARCHAR(50));
ALTER TABLE employees ADD COLUMN dept_id INT;
DROP TABLE departments;
TRUNCATE TABLE employees;

-- 3. DML (INSERT, UPDATE, DELETE)
INSERT INTO employees (id, name, salary, hire_date, is_active) VALUES (1, 'John Doe', 50000, '2022-01-01', TRUE);
UPDATE employees SET salary = 55000 WHERE id = 1;
DELETE FROM employees WHERE id = 1;

-- 4. DQL (SELECT)
SELECT * FROM employees;
SELECT name, salary FROM employees WHERE salary > 40000;

-- 5. WHERE Clause & Operators
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 60000;
SELECT * FROM employees WHERE name LIKE 'J%';
SELECT * FROM employees WHERE dept_id IN (1,2,3);
SELECT * FROM employees WHERE hire_date IS NULL;

-- 6. JOINS
SELECT e.name, d.dept_name FROM employees e INNER JOIN departments d ON e.dept_id = d.dept_id;
SELECT e.name, d.dept_name FROM employees e LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- 7. GROUP BY & Aggregations
SELECT dept_id, COUNT(*) AS num_employees, AVG(salary) AS avg_salary FROM employees GROUP BY dept_id;

-- 8. HAVING Clause
SELECT dept_id, AVG(salary) AS avg_salary FROM employees GROUP BY dept_id HAVING AVG(salary) > 50000;

-- 9. Subqueries
SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

-- 10. Constraints
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100) UNIQUE,
    start_date DATE NOT NULL,
    budget DECIMAL(10,2) CHECK (budget > 0),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- 11. Indexes
CREATE INDEX idx_salary ON employees(salary);

-- 12. Views
CREATE VIEW high_earners AS SELECT name, salary FROM employees WHERE salary > 60000;

-- 13. Transactions
BEGIN;
UPDATE employees SET salary = salary + 1000 WHERE dept_id = 1;
COMMIT;
ROLLBACK;

-- 14. Functions
SELECT UPPER(name), LENGTH(name) FROM employees;
SELECT COALESCE(hire_date, NOW()) FROM employees;

-- 15. Window Functions
SELECT name, salary, RANK() OVER (ORDER BY salary DESC) AS salary_rank FROM employees;

-- 16. Common SQL Interview Questions with Examples
-- Q1: Find the second highest salary
SELECT MAX(salary) AS second_highest_salary FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);
-- Q2: Find employees with duplicate salaries
SELECT salary, COUNT(*) FROM employees GROUP BY salary HAVING COUNT(*) > 1;
-- Q3: Get department-wise highest salary
SELECT dept_id, MAX(salary) AS max_salary FROM employees GROUP BY dept_id;
-- Q4: List employees who joined in the last 6 months
SELECT * FROM employees WHERE hire_date >= DATEADD(month, -6, GETDATE());
-- Q5: Retrieve employees whose name starts with 'A'
SELECT * FROM employees WHERE name LIKE 'A%';
-- Q6: Get the total salary paid per department
SELECT dept_id, SUM(salary) AS total_salary FROM employees GROUP BY dept_id;
-- Q7: Show employees with salary above department average
SELECT name, salary, dept_id FROM employees e WHERE salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id);
-- Q8: Find employees who do not belong to any department
SELECT * FROM employees WHERE dept_id IS NULL;
-- Q9: List top 3 highest paid employees
SELECT TOP 3 name, salary FROM employees ORDER BY salary DESC;
-- Q10: Count employees per department, including departments with zero employees
SELECT d.dept_name, COUNT(e.id) AS num_employees FROM departments d LEFT JOIN employees e ON d.dept_id = e.dept_id GROUP BY d.dept_name;

-- 17. Best Practices
-- Use proper indexing for performance.
-- Avoid SELECT * in production queries.
-- Use parameterized queries to prevent SQL injection.
-- Normalize data but denormalize for reporting if needed.
-- Always backup before running destructive queries.

-- 18. Miscellaneous
SELECT * FROM employees LIMIT 10 OFFSET 20;
SELECT name, salary, CASE WHEN salary > 60000 THEN 'High' ELSE 'Low' END AS salary_level FROM employees;

-- 19. Advanced SQL Interview Questions with Examples
-- Q11: Find employees with the highest salary in each department
SELECT e.* FROM employees e
INNER JOIN (
    SELECT dept_id, MAX(salary) AS max_salary
    FROM employees
    GROUP BY dept_id
) m ON e.dept_id = m.dept_id AND e.salary = m.max_salary;

-- Q12: Get the count of employees hired each year
SELECT YEAR(hire_date) AS year, COUNT(*) AS num_hired
FROM employees
GROUP BY YEAR(hire_date)
ORDER BY year;

-- Q13: Find departments with more than 5 employees
SELECT dept_id, COUNT(*) AS num_employees
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 5;

-- Q14: List employees who have the same salary as someone else (excluding themselves)
SELECT e1.* FROM employees e1
JOIN employees e2 ON e1.salary = e2.salary AND e1.id <> e2.id;

-- Q15: Retrieve the top 2 salaries per department
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn
    FROM employees
) t WHERE rn <= 2;

-- Q16: Find employees who have never received a salary update (assuming a salary_history table)
-- (Assume salary_history has columns: employee_id, change_date)
SELECT e.* FROM employees e
LEFT JOIN salary_history sh ON e.id = sh.employee_id
WHERE sh.employee_id IS NULL;

-- Q17: Calculate the percentage of employees in each department
SELECT dept_id, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employees) AS percent_of_total
FROM employees
GROUP BY dept_id;

-- 20. Stored Procedure Example (for SQL Server)
-- =========================================
-- Create a stored procedure to get employee details by department
CREATE PROCEDURE GetEmployeesByDepartment
    @DeptId INT
AS
BEGIN
    SELECT * FROM Employee WHERE department_id = @DeptId;
END;
GO

-- Call the stored procedure:
EXEC GetEmployeesByDepartment @DeptId = 2;

-- Explanation:
-- A stored procedure is a precompiled collection of SQL statements stored in the database.
-- It can accept parameters, execute logic, and return results. Useful for code reuse, security, and performance.

-- 21. Interview Questions and Answers on Stored Procedures
-- ===================================================
-- Q1: What is a stored procedure?
-- A1: A stored procedure is a set of SQL statements with an assigned name stored in the database. It can be executed with parameters and is used to encapsulate logic for reuse and security.

-- Q2: What are the advantages of using stored procedures?
-- A2: Advantages include improved performance (precompiled), code reuse, better security (controlled access), and easier maintenance.

-- Q3: How do you pass parameters to a stored procedure?
-- A3: Parameters are defined in the procedure and passed during execution. Example: EXEC ProcName @param1 = value1;

-- Q4: Can a stored procedure return values?
-- A4: Yes, it can return result sets (via SELECT), output parameters, or return codes.

-- Q5: How do you handle errors in stored procedures?
-- A5: Use TRY...CATCH blocks (in SQL Server) or exception handling constructs to catch and handle errors.

-- Example with error handling:
CREATE PROCEDURE SafeDivide
    @a INT, @b INT, @result INT OUTPUT
AS
BEGIN
    BEGIN TRY
        SET @result = @a / @b;
    END TRY
    BEGIN CATCH
        SET @result = NULL;
    END CATCH
END;
GO

-- Call:
DECLARE @res INT;
EXEC SafeDivide @a = 10, @b = 0, @result = @res OUTPUT;
SELECT @res;

-- Explanation: If division by zero occurs, @result is set to NULL instead of causing an error.

-- End of SQL Interview Preparation Notes

