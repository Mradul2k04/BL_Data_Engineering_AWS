select product_name, product_price from Products
where product_price=(select min(product_price) from Products);


select round(avg(product_price),2) from Products where category in ('Home & Kitchen','Fitness');


select product_name,stock_quantity from Products
where is_available =TRUE and stock_quantity >50 and product_price !=299;

select category,Max(product_price) as Max_price from Products
group by category;

select Distinct Upper(category) as category_upper
from Products
order by category_upper DESC;

select * from Products;