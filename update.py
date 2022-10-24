from db_create import School, Students, Class_offered, Students_class_enrollment
from db_create import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

# we can do the same with any of the relation from the database
session.query(Students).filter(Students.id==4).update({Students.s_name:"Eminem"})

session.commit()

