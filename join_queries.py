from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *
Session = sessionmaker(bind = engine)
session = Session()

viewStudentEnrollment = session.query(Students, Students_class_enrollment)

for school, student in session.query(School, Students).filter(School.id == Students.id).all():
    print("--------------------------------------------------------------------------------------------------------")
    print ("School: {} , Student Name: {} , Student Email {} , Phone no: {} ".format(school.school_name,student.s_name, student.s_email, student.s_phone_no))
    print("--------------------------------------------------------------------------------------------------------")




for s, c in session.query(Students, Students_class_enrollment).filter(Students.id == Students_class_enrollment.id).all():
    print("------------------------------------------------------------------------------------------------")
    print ("Student Id: {} , Student Name: {} , Course Name: {} , Course no: {} ".format(s.s_id,s.s_name, c.subject_name, c.subject_id))
    print("------------------------------------------------------------------------------------------------")




# SELECT Students.id 
# AS Students.id, Students.s_name 
# AS customers_name, customers.address 
# AS customers_address, customers.email 
# AS customers_email, invoices.id 
# AS invoices_id, invoices.custid 
# AS invoices_custid, invoices.invno 
# AS invoices_invno, invoices.amount 
# AS invoices_amount
# FROM customers, invoices
# WHERE customers.id = invoices.custid