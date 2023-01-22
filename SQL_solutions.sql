-- 1741. Find Total Time Spent by Each Employee
-- # Write your MySQL query statement below
SELECT event_day AS day, emp_id, SUM(out_time) - SUM(in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;

-- 1890. The Latest Login in 2020
-- # Write your MySQL query statement below
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id;

-- 511. Game Play Analysis I
-- # Write your MySQL query statement below
SELECT DISTINCT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;

-- 586. Customer Placing the Largest Number of Orders
-- # Write your MySQL query statement below
SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 1729. Find Followers Count
--# Write your MySQL query statement below
select DISTINCT(user_id), COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY 1, 2;

-- 1693. Daily Leads and Partners
-- # Write your MySQL query statement below
SELECT date_id, make_name, COUNT(DISTINCT lead_id) AS unique_leads, COUNT(DISTINCT partner_id) as unique_partners
FROM DailySales
GROUP BY 1, 2;


-- 595. Big Countries
-- Write your MySQL query statement below
select name, population, area from World where area >= 3000000 or population >= 25000000;

-- 1757. Recyclable and Low Fat Products
-- Write your MySQL query statement below
select product_id from Products where low_fats = 'Y' and recyclable = "Y";

-- 584. Find Customer Referee
-- Write your MySQL query statement below
select name from Customer where referee_id is null or referee_id <> 2;

-- 183. Customers Who Never Order
-- Write your MySQL query statement below
select Customers.name as Customers from Customers where Customers.id not in (select Orders.customerId from Orders);

-- 1873. Calculate Special Bonus
-- Write your MySQL query statement below
select employee_id, if(employee_id%2!=0 and name not like 'M%', salary, 0) as bonus 
from Employees 
order by employee_id;

-- 627. Swap Salary
-- Write your MySQL query statement below
update Salary set sex = if(sex = 'm', 'f', 'm');

-- 196. Delete Duplicate Emails
-- Please write a DELETE statement and DO NOT write a SELECT statement.
-- Write your MySQL query statement below
delete p1 from Person p1, Person p2
where p1.email = p2.email and p1.id > p2.id;

-- 1667. Fix Names in a Table
-- Write your MySQL query statement below
select user_id, concat(upper(left(name, 1)), lower(right(name, length(name)-1))) as name from users
order by user_id;

-- 1484. Group Sold Products By The Date
-- Write your MySQL query statement below
select sell_date, count(distinct(product)) as num_sold, group_concat(DISTINCT product ORDER BY product ASC SEPARATOR ',') as products
from activities 
group by sell_date
order by sell_date;

-- 1527. Patients With a Condition
-- Write your MySQL query statement below
select patient_id, patient_name, conditions from Patients where conditions like '% DIAB1%' or conditions like 'DIAB1%';

-- 1965. Employees With Missing Information
-- # Write your MySQL query statement below
select employee_id from Employees where employee_id not in (select employee_id from Salaries)
union 
select employee_id from Salaries where employee_id not in (select employee_id from Employees)
order by 1 asc;

-- 1795. Rearrange Products Table
-- # Write your MySQL query statement below
select product_id, 'store1' as store, store1 as price from Products where store1 is not null
union
select product_id, 'store2' as store, store2 as price from Products where store2 is not null
union
select product_id, 'store3' as store, store3 as price from Products where store3 is not null;

-- 608. Tree Node
-- # Write your MySQL query statement below
select id,
    case when p_id is null then 'Root'
         when id in (select p_id from Tree) then 'Inner'
         else 'Leaf'
    end as Type
from tree
order by id;

-- 176. Second Highest Salary
-- # Write your MySQL query statement below
select max(salary) as SecondHighestSalary from Employee where salary not in (select max(salary) from Employee);

-- 175. Combine Two Tables
-- # Write your MySQL query statement below
select FirstName, LastName, City, State
from Person 
left join Address on Person.PersonId = Address.PersonId;

-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- # Write your MySQL query statement below
select customer_id, count(Visits.visit_id) as count_no_trans 
from Visits
left join Transactions on Visits.visit_id = Transactions.visit_id
where Transactions.visit_id is null
group by customer_id;
where Transactions.visit_id is null;

-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- # Write your MySQL query statement below
select distinct author_id as id from Views where author_id = viewer_id order by 1 asc;

-- 197. Rising Temperature
-- # Write your MySQL query statement below
select w1.id from Weather w1, Weather w2
where w1.temperature > w2.temperature and datediff(w1.recordDate, w2.recordDate) = 1;

-- 607. Sales Person
-- # Write your MySQL query statement below
select s.name from SalesPerson s
where sales_id not in
(  
    select sales_id from orders where com_id in
    (select com_id from company where name = 'RED')
);

-- 1141. User Activity for the Past 30 Days I
-- # Write your MySQL query statement below
select activity_date as day, count(distinct user_id) as active_users
from Activity 
where (activity_date > '2019-06-27' AND activity_date <= '2019-07-27')
group by activity_date;
