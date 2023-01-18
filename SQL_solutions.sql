# 595. Big Countries
# Write your MySQL query statement below
select name, population, area from World where area >= 3000000 or population >= 25000000;

# 1757. Recyclable and Low Fat Products
# Write your MySQL query statement below
select product_id from Products where low_fats = 'Y' and recyclable = "Y";

# 584. Find Customer Referee
# Write your MySQL query statement below
select name from Customer where referee_id is null or referee_id <> 2;

# 183. Customers Who Never Order
# Write your MySQL query statement below
select Customers.name as Customers from Customers where Customers.id not in (select Orders.customerId from Orders);
