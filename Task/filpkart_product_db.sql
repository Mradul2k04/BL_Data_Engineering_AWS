CREATE TABLE Products(
Product_ID Serial primary key,
Product_name varchar(100) not null,
sku_code char(8) unique not null,
Product_price  numeric(10,2) check (Product_price >0),
Stock_Quantity int default 0 check (Stock_Quantity>=0),
is_available boolean  default TRUE,
category text not null,
added_on date default current_date,
last_update  Timestamp default now()
);

insert into Products(Product_name,sku_code,Product_price,Stock_Quantity,is_available,category)
values
('Wireless Mouse', 'WM123456', 699.99, 50, TRUE, 'Electronics'),
('Bluetooth Speaker', 'BS234567', 1499.00, 30, TRUE, 'Electronics'),
('Laptop Stand', 'LS345678', 799.50, 20, TRUE, 'Accessories'),
('USB-C Hub', 'UC456789', 1299.99, 15, TRUE, 'Accessories'),
('Notebook', 'NB567890', 99.99, 100, TRUE, 'Stationery'),
('Pen Set', 'PS678901', 199.00, 200, TRUE, 'Stationery'),
('Coffee Mug', 'CM789012', 299.00, 75, TRUE, 'Home & Kitchen'),
('LED Desk Lamp', 'DL890123', 899.00, 40, TRUE, 'Home & Kitchen'),
('Yoga Mat', 'YM901234', 499.00, 25, TRUE, 'Fitness'),
('Water Bottle', 'WB012345', 349.00, 60, TRUE, 'Fitness');

Select * from Products;
