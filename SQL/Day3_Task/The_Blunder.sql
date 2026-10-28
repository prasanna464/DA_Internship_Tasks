## Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

## Write a query calculating the amount of error (i.e.: actual-miscaluclated average monthly salaries), and round it up to the next int

## Problem Statement Link :- https://www.hackerrank.com/challenges/the-blunder/problem

select cast(ceil(avg(cast(salary as decimal(8,2))) - avg(cast(replace(salary, '0', '') as decimal(8,2)))) as int) from employees;

  

