from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


engine = create_engine('postgresql://postgres:d4t4l4b@dataLab/inegi_dwh', convert_unicode=True)
Base = automap_base()
# # reflect the tables
Base.prepare(engine, reflect=True)
# db_session = Session(engine)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine)) 

Base.query = db_session.query_property()


# ent = Base.classes.fact_entidad

# for entidad_cvegeo, pob01 in session.query(ent.entidad_cvegeo, ent.pob01):
#     print(entidad_cvegeo, pob01)







# def init_db():
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to import them first before calling init_db()
#     from models import Department, Employee, Role
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)

#     # Create the fixtures
#     engineering = Department(name='Engineering')
#     db_session.add(engineering)
#     hr = Department(name='Human Resources')
#     db_session.add(hr)

#     manager = Role(name='manager')
#     db_session.add(manager)
#     engineer = Role(name='engineer')
#     db_session.add(engineer)

#     peter = Employee(name='Peter', department=engineering, role=engineer)
#     db_session.add(peter)
#     roy = Employee(name='Roy', department=engineering, role=engineer)
#     db_session.add(roy)
#     tracy = Employee(name='Tracy', department=hr, role=manager)
#     db_session.add(tracy)
#     db_session.commit()
