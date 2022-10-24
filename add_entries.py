from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import School, Students, Class_offered, Students_class_enrollment

Session = sessionmaker(bind = engine)
session = Session()
if __name__ == "__main__":
    
    # adding a single entry
    # addSchool = School(school_name = "NEIU", school_address ="5700 St. Louis", phone_no = 7734244242)
    # session.add(addSchool)
    # session.commit()
    addSchool = School()
    session.add_all([
        School(school_name = "NEIU", school_address ="5700 St. Louis", phone_no = 773444000),
        School(school_name = "De Paul", school_address ="800 W. Fullerton", phone_no = 312888999),
        School(school_name = "NEIU", school_address ="5700 St. Louis", phone_no = 773444000),
        School(school_name = "Northwestern", school_address ="800 Sheridan Rd.", phone_no = 3120001111),
        School(school_name = "NEIU", school_address ="5700 St. Louis", phone_no = 773444000),
        School(school_name = "De Paul", school_address ="800 W. Fullerton", phone_no = 312888999)

    ])

    addStudents = Students()
    session.add_all([
        Students(s_name = "Anand", s_email = "anand@gmail.com", s_phone_no= 7734441818, s_id = 605123),
        Students(s_name = "Paulina", s_email = "paulina@gmail.com", s_phone_no= 3124441818,s_id = 605124),
        Students(s_name = "Meghan", s_email = "meghan@gmail.com", s_phone_no= 3122821818, s_id = 605125),
        Students(s_name = "Muhammed", s_email = "muhammed@gmail.com", s_phone_no= 7734442222, s_id = 605126),
        Students(s_name = "Morris", s_email = "morris@gmail.com", s_phone_no= 7731019110, s_id = 605127)
    ])


    classOffered = Class_offered()
    session.add_all([
        Class_offered(subject_name = "Discrete Math", subject_id = 201),
        Class_offered(subject_name = "Machine Learning", subject_id = 348),
        Class_offered(subject_name = "Operating Systems", subject_id = 301),
        Class_offered(subject_name = "Algorithm", subject_id = 324),
        Class_offered(subject_name = "Web Development", subject_id = 300),
        Class_offered(subject_name = "Software Engineering", subject_id = 319),
        Class_offered(subject_name = "Mobile App Development", subject_id = 347)

    ])

    studentsClassEnrollment = Students_class_enrollment()
    session.add_all([
        Students_class_enrollment(s_name = "Anand", s_email= "anand@gmail.com", subject_name = "Discrete Math", subject_id = 201),
        Students_class_enrollment(s_name = "Paulina", s_email= "paulina@gmail.com", subject_name = "Operating Systems", subject_id = 301),
        Students_class_enrollment(s_name = "Meghan", s_email= "meghan@gmail.com", subject_name = "Machine Learning", subject_id = 348),
        Students_class_enrollment(s_name = "Muhammed", s_email= "muhammed@gmail.com", subject_name = "Web Development", subject_id = 300),
        Students_class_enrollment(s_name = "Morris", s_email= "morris@gmail.com", subject_name = "Discrete Math", subject_id = 201),
        Students_class_enrollment(s_name = "Anand", s_email= "anand@gmail.com", subject_name = "Algorithm", subject_id = 324),
        Students_class_enrollment(s_name = "Muhammed", s_email= "muhammed@gmail.com", subject_name = "Mobile App Development", subject_id = 347),
        Students_class_enrollment(s_name = "Morris", s_email= "morris@gmail.com", subject_name = "Operating Systems", subject_id = 301),
        Students_class_enrollment(s_name = "Paulia", s_email= "paulina@gmail.com", subject_name = "Discrete Math", subject_id = 201),
        Students_class_enrollment(s_name = "Meghan", s_email= "meghan@gmail.com", subject_name = "Software Engineering", subject_id = 319),
        

    ])
         


session.commit()