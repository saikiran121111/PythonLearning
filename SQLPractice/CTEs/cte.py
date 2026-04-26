#What is a CTE?
#A CTE is just a named subquery written at the top using WITH. That's it

# # You already know subqueries:
# pd.read_sql("""
#     SELECT name, salary
#     FROM employees
#     WHERE salary > (SELECT AVG(salary) FROM employees)
# """, conn)
#
# # CTE does the exact same thing — just cleaner:
# pd.read_sql("""
#     WITH avg_salary AS (
#         SELECT AVG(salary) AS avg_sal FROM employees
#     )
#     SELECT name, salary
#     FROM employees, avg_salary
#     WHERE salary > avg_salary.avg_sal
# """, conn)

#Same result. CTE just gives the subquery a name so it reads like English.

# The Syntax — Always This Pattern
# WITH cte_name AS (
#     -- your query here
# )
# SELECT ...
# FROM cte_name