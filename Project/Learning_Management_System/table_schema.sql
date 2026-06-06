CREATE TABLE users(
user_id varchar(10) not null Primary key CHECK (user_id ~ '^USR-[0-9]{4}$'),
user_name varchar(20) not null ,
user_role varchar(10) not null default 'Student',
user_email varchar(30) not null unique,
user_phone_number bigint not null unique
);

CREATE TABLE courses(
course_id varchar(10) not null unique Primary key CHECK (course_id ~'^CORS-[0-9]{4}$'),
course_description varchar(50) not null, 
course_title varchar(30) not null 
);

CREATE TABLE lessons(
lesson_id VARCHAR(10) NOT NULL PRIMARY KEY CHECK(lesson_id ~ '^LES-[0-9]{4}$'),
course_id VARCHAR(10) NOT NULL REFERENCES courses(course_id),
lesson_content TEXT NOT NULL,
lesson_title VARCHAR(100) NOT NULL
);

CREATE TABLE enrollments(
enrollment_id VARCHAR(10) NOT NULL PRIMARY KEY CHECK(enrollment_id ~ '^	ERL-[0-9]{4}$'),
user_id VARCHAR(10) NOT NULL REFERENCES users(user_id),
course_id VARCHAR(10) NOT NULL REFERENCES courses(course_id),
enrollment_date TIMESTAMP NOT NULL default NOW()
);

CREATE TABLE user_activity(
activity_id VARCHAR(10) NOT NULL PRIMARY KEY CHECK(activity_id ~ '^ACT-[0-9]{4}$'),
user_id VARCHAR(10) NOT NULL REFERENCES users(user_id),
lesson_id VARCHAR(10) NOT NULL REFERENCES lessons(lesson_id),
activity_status VARCHAR(20) NOT NULL default 'Not Started'
);

CREATE TABLE assessments(
assessment_id VARCHAR(10) NOT NULL PRIMARY KEY CHECK(assessment_id ~ '^ASS-[0-9]{4}$'),
course_id VARCHAR(10) NOT NULL REFERENCES courses(course_id),
max_score INT NOT NULL default 100
);

CREATE TABLE assessment_submissions(
submission_id VARCHAR(10) NOT NULL PRIMARY KEY CHECK(submission_id ~ '^SUB-[0-9]{4}$'),
assessment_id VARCHAR(10) NOT NULL REFERENCES assessments(assessment_id),
user_id VARCHAR(10) NOT NULL REFERENCES users(user_id),
submission_date DATE NOT NULL,
score_obtained INT not null default 0
);