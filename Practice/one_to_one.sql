create table students(
student_id serial Primary key,
name varchar(20) not null
);

insert into students (name)
values ('MRADUL'),
('KARAN'),
('ANUJ');

SELECT * FROM students;

create table student_profiles(
student_id int Primary key,
address text,
age int,
phone varchar(15)
);

insert into student_profiles(student_id,address,age,phone)
values(1,'delhi,India',22,'44544184184'),
(2,'mumbai,India',21,'44544222145421'),
(3,'bangalore,India',32,'445448888888');

alter table student_profiles
add constraint fk_student_id
foreign key (student_id)
references students(student_id);

select * from student_profiles;

select 
s.student_id,
s.name,
sp.address,
sp.age,
sp.phone
from students s
join student_profiles sp
on s.student_id=sp.student_id;



