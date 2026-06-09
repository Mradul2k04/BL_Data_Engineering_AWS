------------------------------------------------------------Section-2----------------------------------------------------------------------------
select * from users;
select * from courses;
select * from lessons;
select * from enrollments;
select * from user_activity;
select * from assessments;
select * from assessment_submissions;
--For each course, calculate:Total number of enrolled users,Total number of lessons
select 
c.course_id,
c.course_title,
count(distinct e.user_id) as total_enrolled_users,
count(distinct l.lesson_id) as total_lessons
from courses c left join enrollments e on c.course_id=e.course_id
left join lessons l on c.course_id=l.course_id
group by c.course_id,c.course_title;

--Identify the top three most active users based on total activity count.
select u.user_id , u.user_name , count(ua.activity_id) as total_activity_count
from users u left join user_activity ua
on u.user_id=ua.user_id
group by u.user_id,u.user_name
order by total_activity_count DESC
limit 3;

--Find users whose average assessment score is higher than the course average.



--List courses where lessons are frequently accessed but assessments are never attempted.
select c.course_id,c.course_title 
from courses c join lessons l on c.course_id=l.course_id
join user_activity ua on l.lesson_id =ua.lesson_id
left join assessments a on c.course_id=a.course_id
left join assessment_submissions sub on a.assessment_id=sub.assessment_id
group by c.course_id,c.course_title
having count(sub.submission_id)=0;


--Rank users within each course based on their total assessment score.


--Identify the first lesson accessed by each user for every course.


--Find users with activity recorded on at least five consecutive days.


--Retrieve users who enrolled in a course but never submitted any assessment.


--List courses where every enrolled user has submitted at least one assessment.
