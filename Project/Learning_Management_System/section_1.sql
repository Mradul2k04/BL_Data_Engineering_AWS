-------------------------------------------Section 1--------------------------------------------------------------
select * from users;
select * from courses;
select * from lessons;
select * from enrollments;
select * from user_activity;
select * from assessments;
select * from assessment_submissions;


--List all users who are enrolled in more than three courses.
select u.user_id,u.user_name ,count(e.course_id) as total_enrollments
from users u join enrollments e
on u.user_id=e.user_id
group by u.user_id ,u.user_name
having count(e.course_id)>3 ;


--Find courses that currently have no enrollments.
select c.course_id ,c.course_title
from courses c left join enrollments e
on c.course_id =e.course_id
where e.course_id is null;


--Display each course along with the total number of enrolled users.
select c.course_id,c.course_title ,count(e.user_id) as total_enrolled_users
from courses c left join enrollments e
on c.course_id=e.course_id
group by c.course_id,c.course_title;


--Identify users who enrolled in a course but never accessed any lesson.
select distinct u.user_id, u.user_name
from users u join enrollments e
on u.user_id=e.user_id
left join user_activity ua 
on u.user_id=ua.user_id
where ua.user_id is null; 


--Fetch lessons that have never been accessed by any user.
select l.lesson_id, l.lesson_title
from lessons l left join user_activity ua
on l.lesson_id=ua.lesson_id
where ua.lesson_id is null;


--Show the last activity timestamp for each user.
select u.user_id, u.user_name ,max(sub.submission_date) as last_activity
from users u inner join assessment_submissions sub
on u.user_id =sub.user_id
group by u.user_id,u.user_name;


--List users who submitted an assessment but scored less than 50 percent of the maximum score.
select distinct u.user_id , u.user_name,a.assessment_id,sub.score_obtained,a.max_score
from users u join assessment_submissions sub
on u.user_id =sub.user_id
join assessments a on sub.assessment_id=a.assessment_id
where sub.score_obtained <(a.max_score *0.5 );


--Find assessments that have not received any submissions.
select a.assessment_id,a.course_id 
from assessments a left join assessment_submissions sub
on a.assessment_id =sub.assessment_id
where sub.assessment_id is null;


--Display the highest score achieved for each assessment.
select a.assessment_id,a.course_id,max(sub.score_obtained) as highest_score
from assessments a inner join assessment_submissions sub
on a.assessment_id =sub.assessment_id
group by a.assessment_id ,a.course_id;


--Identify users who are enrolled in a course but have an inactive enrollment status.
select u.user_id, u.user_name ,e.course_id
from users u join enrollments e 
on u.user_id=e.user_id
left join user_activity ua on u.user_id=ua.user_id
where ua.activity_status is null or ua.activity_status='Not Started';

