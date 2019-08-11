--List the following details of each employee: employee number, 
--last name, first name, gender, and salary.
SELECT
e.emp_no,
e.last_name,
e.first_name,
e.gender,
s.salary
FROM "Employees" e
LEFT JOIN "Salaries" s
ON e.emp_no = s.emp_no;

--List employees who were hired in 1986.
SELECT *
FROM "Employees"
WHERE hire_date >= '1986-01-01' and hire_date <= '1986-12-31';

--List the manager of each department with the following information: 
--department number, department name, the manager's employee number, 
--last name, first name, and start and end employment dates.
SELECT
d.dept_no,
d.dept_name,
dm.emp_no,
e.last_name,
e.first_name,
de.from_date,
de.to_date
FROM "Department_Manager" as dm
INNER JOIN "Departments" as d
ON dm.dept_no = d.dept_no
INNER JOIN "Employees" as e
ON e.emp_no = dm.emp_no
INNER JOIN "Department_Employees" as de
ON de.emp_no = e.emp_no

--List the department of each employee with the following information: 
--employee number, last name, first name, and department name.
SELECT
e.emp_no,
e.last_name,
e.first_name,
d.dept_name
FROM "Employees" as e
JOIN "Department_Employees" as de
ON e.emp_no = de.emp_no
JOIN "Departments" as d
ON de.dept_no = d.dept_no

--List all employees whose first name is "Hercules" and last names 
--begin with "B."
SELECT *
FROM "Employees"
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%'

--List all employees in the Sales department, including their 
--employee number, last name, first name, and department name.
SELECT
e.emp_no,
e.last_name,
e.first_name,
d.dept_name
FROM "Employees" as e
JOIN "Department_Employees" as de
ON e.emp_no = de.emp_no
JOIN "Departments" as d
ON de.dept_no = d.dept_no
WHERE dept_name = 'Sales'

--List all employees in the Sales and Development departments, 
--including their employee number, last name, first name, and department name.
--employee number, last name, first name, and department name.
SELECT
e.emp_no,
e.last_name,
e.first_name,
d.dept_name
FROM "Employees" as e
JOIN "Department_Employees" as de
ON e.emp_no = de.emp_no
JOIN "Departments" as d
ON de.dept_no = d.dept_no
WHERE dept_name = 'Sales' or dept_name = 'Development'

--In descending order, list the frequency count of employee last names, 
--i.e., how many employees share each last name.

SELECT last_name, count(*)
FROM "Employees"
Group By last_name
ORDER BY count DESC








