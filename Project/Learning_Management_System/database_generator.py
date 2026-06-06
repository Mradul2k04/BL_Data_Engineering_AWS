import csv
from faker import Faker
from datetime import datetime,timedelta
import random

fake=Faker()

#total records
num_records=200

#user file generaton
user_file_path= r"Project\Learning_Management_System\user_data.csv"
headers=["user_id","user_name","user_role","user_email","user_phone_number"]
roles=["Admin","Student"]

with open (user_file_path,"w",newline="",encoding="utf-8") as f:
    write=csv.writer(f)
    write.writerow(headers)
    
    for i in range(1,num_records+1):
        user_id=f"USR-{i:04d}"
        user_name=fake.name()
        user_role=random.choice(roles)
        user_email=fake.email()
        user_phone_number=random.randint(6000000000,9999999999)
        
        write.writerow([
            user_id,
            user_name,
            user_role,
            user_email,
            user_phone_number
        ])
        
#course file generaton
course_file_path=r"Project\Learning_Management_System\course_data.csv"
headers=["course_id","course_description","course_title"]
prefix=["Intoduction to","Advance","Foundation of","Masterclass in","Applied"]
topics=['Data Analytics', 'Full-Stack Development', 'Cloud Architecture', 'Cybersecurity', 'Machine Learning']   

with open(course_file_path,"w",newline="",encoding="utf-8") as f:
    write=csv.writer(f)
    write.writerow(headers)
    
    for i in range (1,num_records+1):
        course_id=f"CORS-{i:04d}"
        course_description=fake.paragraph(nb_sentences=5)
        course_title=f"{random.choice(prefix)} {random.choice(topics)}"
        
        write.writerow([
            course_id,
            course_description,
            course_title
        ])
        
#lessons file generation
lessons_file_path=r"Project\Learning_Management_System\lessons_data.csv"
headers=["lesson_id","course_id","lesson_content","lesson_title"]
verbs=['Getting Started with', 'Understanding', 'Deep Dive into', 'Mastering', 'Debugging']
nouns = ['Arrays & Objects', 'Git Workflows', 'REST APIs', 'SQL Joins', 'State Management']

with open(lessons_file_path,"w",newline="",encoding="utf-8") as f:
       write=csv.writer(f)
       write.writerow(headers)
       
       for i in range(1,num_records+1):
           lesson_id=f"LES-{i:04d}"
           random_num=random.randint(1,200)
           course_id=f"CORS-{random_num:04d}"
           lesson_content=fake.sentence(nb_words=12)
           lesson_title=f"{random.choice(verbs)} {random.choice(nouns)}"
           
           write.writerow([
               lesson_id,
               course_id,
               lesson_content,
               lesson_title
           ])
#enrollments file generation
enrollment_file_path=r"Project\Learning_Management_System\enrollments_data.csv"
headers=["enrollment_id","user_id","course_id","enrollment_date"]

with open(enrollment_file_path,"w",newline="",encoding="utf-8")as f:
    write=csv.writer(f)
    write.writerow(headers)
    
    for i in range(1,num_records+1):
        enrollment_id=f"ERL-{i:04d}"
        user_num=random.randint(1,200)
        user_id=f"USR-{user_num:04d}"
        course_num=random.randint(1,200)
        course_id=f"CORS-{course_num:04d}"
        date_time=fake.date_time_between(start_date='-2y',end_date='now')
        enrollment_date=date_time.strftime('%y-%m-%d %H:%M:%S')
        
        write.writerow([
            enrollment_id,
            user_id,
            course_id,
            enrollment_date
        ])
        
#uer activity file generation
user_activity_file_path=r"Project\Learning_Management_System\user_activity_data.csv"     
headers=["activity_id","user_id","lesson_id","activity_status"]
status=["Not Started","In Progress","Completed"]


with open (user_activity_file_path,"w",newline="",encoding="utf-8") as f:
    write=csv.writer(f)
    write.writerow(headers)
    
    for i in range(1,num_records+1):
        activity_id=f"ACT-{i:04d}"
        user_num=random.randint(1,200)
        user_id = f"USR-{user_num:04d}"
        lesson_num = random.randint(1,200)
        lesson_id = f"LES-{lesson_num:04d}"
        activity_status = random.choice(status)
        
        write.writerow([
            activity_id,
            user_id,
            lesson_id,
            activity_status
        ])
        
# assesment file generation
assessment_file_path = r"Project\Learning_Management_System\assessments_data.csv"
headers = ["assessment_id","course_id","max_score"]

with open(assessment_file_path,"w",newline="", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(headers)

    for i in range(1,num_records+1):
        assessment_id = f"ASS-{i:04d}"
        course_num = random.randint(1,200)
        course_id = f"CORS-{course_num:04d}"
        max_score = 100

        write.writerow([
            assessment_id,
            course_id,
            max_score
        ])
        
# assessment submission file generation
submission_file_path = r"Project\Learning_Management_System\assessments_submission_data.csv"
headers = ["submission_id","assessment_id","user_id","submission_date","score_obtained"]

with open(submission_file_path,"w",newline="", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(headers)

    start_window = datetime.strptime('2024-06-01', '%Y-%m-%d')
    end_window = datetime.strptime('2026-06-30', '%Y-%m-%d')

    for i in range(1,num_records+1):
        submission_id = f"SUB-{i:04d}"
        assessment_num = random.randint(1,200)
        assessment_id = f"ASS-{assessment_num:04d}"
        user_num = random.randint(1,200)
        user_id = f"USR-{user_num:04d}"
        date_obj = fake.date_time_between(start_date=start_window, end_date=end_window)
        submission_date = date_obj.strftime("%Y-%m-%d")
        score_obtained=random.randint(0,100)

        write.writerow([
            submission_id,
            assessment_id,
            user_id,
            submission_date,
            score_obtained
        ])

print("File generated successfully")       
        
        