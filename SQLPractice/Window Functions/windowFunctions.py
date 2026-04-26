#function() OVER (PARTITION BY col ORDER BY col)
#      ↑              ↑                ↑
#  what to        group by         sort within
#  calculate      which col        each group


#ROW_NUMBER → always unique, no ties ever

#RANK → ties get same number, skips next number

#DENSE_RANK → ties get same number, no skipping

#GROUP BY dept → collapses everything → you LOSE individual rows
# pd.read_sql("""
#     SELECT dept, AVG(salary) as avg_sal
#     FROM employees
#     GROUP BY dept
# """, conn)

# You only get 3 rows — individual employees are GONE:
#       dept    avg_sal
# 0  Finance    70000.0
# 1       HR    70000.0
# 2       IT    50000.0

# But what if you want this instead:
#     name     dept  salary  dept_avg
# 0  Alice       IT   50000   50000.0   ← Alice's row + her dept avg
# 1    Bob       HR   60000   70000.0   ← Bob's row + his dept avg
# 2  Charlie     IT   55000   50000.0   ← Charlie's row + his dept avg
# ...all 6 rows kept!

# Step 2 — The Magic Word: OVER()
# The moment you write OVER() after any function — it becomes a window function.

# pd.read_sql("""
#     SELECT name, dept, salary,
#            AVG(salary) OVER() AS company_avg
#     FROM employees
# """, conn)

# Expected output:
#       name     dept  salary  company_avg
# 0    Alice       IT   50000      60000.0
# 1      Bob       HR   60000      60000.0
# 2  Charlie       IT   55000      60000.0
# 3    Diana  Finance   70000      60000.0
# 4      Eve       IT   45000      60000.0
# 5    Frank       HR   80000      60000.0
# All 6 rows kept! Same avg added to every row.

#OVER() with nothing inside = whole table as one group

# Step 3 — PARTITION BY = "Do it group by group"
# PARTITION BY is like saying "calculate separately for each department" — but still keep all rows.
#
# python
# pd.read_sql("""
#     SELECT name, dept, salary,
#            AVG(salary) OVER(PARTITION BY dept) AS dept_avg
#     FROM employees
# """, conn)

# Expected output:
#       name     dept  salary     dept_avg
# 0    Alice       IT   50000   50000.000   ← IT avg
# 1      Bob       HR   60000   70000.000   ← HR avg
# 2  Charlie       IT   55000   50000.000   ← IT avg (same group as Alice)
# 3    Diana  Finance   70000   70000.000   ← Finance avg
# 4      Eve       IT   45000   50000.000   ← IT avg
# 5    Frank       HR   80000   70000.000   ← HR avg (same group as Bob)
# Think of PARTITION BY as drawing invisible boxes around each department — the calculation happens inside each box separately.
#
# Step 4 — ROW_NUMBER() = Give each row a number
# python
# pd.read_sql("""
#     SELECT name, dept, salary,
#            ROW_NUMBER() OVER(PARTITION BY dept ORDER BY salary DESC) AS rank
#     FROM employees
# """, conn)

# Expected output:
#       name     dept  salary  rank
# 0    Diana  Finance   70000     1   ← only one in Finance, rank 1
# 1    Frank       HR   80000     1   ← highest in HR, rank 1
# 2      Bob       HR   60000     2   ← second in HR, rank 2
# 3  Charlie       IT   55000     1   ← highest in IT, rank 1
# 4    Alice       IT   50000     2   ← second in IT, rank 2
# 5      Eve       IT   45000     3   ← third in IT, rank 3
# Each dept restarts from 1!
# Step 5 — RANK() vs DENSE_RANK() vs ROW_NUMBER()
# Only matters when two people have the same salary (a tie):
#
# text
# salary   ROW_NUMBER   RANK   DENSE_RANK
# 80000         1         1         1
# 70000         2         2         2
# 70000         3         2         2   ← tie!
# 60000         4         4         3   ← RANK skips to 4, DENSE_RANK goes to 3