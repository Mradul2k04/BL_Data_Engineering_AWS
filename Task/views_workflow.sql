create view  low_stock as
select product_name,category,stock_quantity
from Products
where stock_quantity <30;