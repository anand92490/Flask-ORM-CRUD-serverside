from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import School, Students, Class_offered, Students_class_enrollment

Session = sessionmaker(bind = engine)
session = Session()

if __name__ == "__main__":

# delete students by id

    delById = session.query(Students).get(3)
    session.delete(delById)

    session.commit()


# delete students by name
    # deleteByName = session.query(Students_class_enrollment).filter(Students_class_enrollment.s_name == "Anand").first()
    # session.delete(deleteByName)
    # session.commit()


