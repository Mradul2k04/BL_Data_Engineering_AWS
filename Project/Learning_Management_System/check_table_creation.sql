------------------------------------------------SECTION 1------------------------------------------------------------
--List all users who are enrolled in more than three courses. 
SELECT user_id,user_name from users where user_id IN (SELECT user_id from enrollments 
group by user_id having count(course_id)>3);

--Find courses that currently have no enrollments. 
Select * from enrollments;
Select * from courses;

SELECT course_id,course_title from courses where course_id NOT IN 
(Select Distinct course_id from  enrollments where course_id is not null);

--3. Display each course along with the total number of enrolled users. 