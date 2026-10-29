## Problem Statement Link :- https://www.hackerrank.com/challenges/earnings-of-employees/problem

with a as( select employee_id, months*salary as total_employee_salary, max(months*salary)over() as max_employee_salary from employee ) select max_employee_salary, count(distinct employee_id) from a where total_employee_salary=max_employee_salary group by max_employee_salary limit 1
