CREATE DATABASE person_db

CREATE TABLE person(
id INT,
name VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO person(id, name, city)
VALUES(1, 'Mradul', 'Mathura');


INSERT INTO person
VALUES
(2, 'Anuj', 'Mathura'),
(3, 'Karan', 'Agra');

Select * from person;

SELECT NAME FROM person;

UPDATE person
SET city='Delhi'
WHERE id = 1;

DELETE FROM person
WHERE id = 3

Select * from person;