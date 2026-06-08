Select * from products;

Select * from orders;

--Q1. Show each order along with the product name and price
Select o.order_id,o.customer_name,p.product_name,p.price 
from orders o inner join products p
on o.product_id = p.product_id;

--Q2. Show all products even if they were never ordered
Select p.product_name,o.order_id
from products p left join orders o
on o.product_id = p.product_id;

--Q3. Show orders for only 'Electronics' category
select p.product_id ,p.product_name,p.category 
from 
orders o join products p
on o.product_id =p.product_id
where p.category='Electronics';

--Q4. List all orders sorted by product price (high to low)
select o.order_id,p.product_name,p.price
from 
orders o join products p 
on o.product_id=p.product_id
order by p.price DESC;

--Q5. Show number of orders placed for each product
select p.product_name , count(o.order_id) as total_orders
from 
products p left join orders o 
on p.product_id = o.product_id
group by p.product_name;

--Q6. Show total revenue earned per product
--Q7. Show products where total order revenue > ₹2000
select p.product_name , sum(o.quantity*p.price) as revenue
from 
products p join orders o
on p.product_id = o.product_id
group by p.product_name
having  sum(o.quantity*p.price)>2000;

--Q8. Show unique customers who ordered 'Fitness' products
select distinct o.customer_name
from orders o  join  products p 
on o.product_id =p.product_id
where p.category ='Fitness';



