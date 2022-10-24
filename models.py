#from venv import create

from db_create import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Sequence

class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    school_name = Column(String(50))
    school_address = Column(String(50))
    phone_no =  Column(Integer)

    def __repr__(self):
        return "<School(school_name='%s', school_address='%s, phone_no='%s')>" % (
                            self.school_name, self.school_address, self.phone_no)

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    s_name = Column(String(50))
    s_email= Column(String(50))
    s_phone_no =  Column(Integer)
    s_id = Column(Integer, ForeignKey('school.id'))

    def __repr__(self):
        return "<Students(s_name='%s', s_email='%s', s_phone_no='%s')>" % (
                                self.s_name, self.s_email, self.s_phone_no)


class Class_offered(Base):
    __tablename__ = 'class_offered'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(50))
    subject_id = Column(Integer, ForeignKey('students.id'))

    def __repr__(self):
        return "<class_offered(subject_name='%s', subject_id='%s')>" % (
                                self.subject_name, self.subject_id)
                        
class Students_class_enrollment(Base):
    __tablename__ = 'students_class_enrollment'
    id = Column(Integer, primary_key=True)
    s_name = Column(String(50))
    s_email= Column(String(50))
    subject_name = Column(String(50))
    subject_id = Column(Integer, ForeignKey('class_offered.id'))


    def __repr__(self):
        return "<students_class_enrollment(s_name='%s', s_email='%s', subject_name='%s', subject_id='%s')>" % (
                                self.s_name, self.s_email, self.subject_name, self.subject_id)




                                