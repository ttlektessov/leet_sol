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
