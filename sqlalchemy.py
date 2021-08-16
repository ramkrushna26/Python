
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql_mysqlconnector://root:pwd@localhost:3306/database, echo=True")

Base = declarative_base()

class Project(Base):
  __tablename__ = 'projects'
  __table_args__ = {'schema' : 'household'}
  
  project_id = Column(Integer, primary_key=True)
  title = Column(String(length=50))
  description = Column(String(length=50))
  
  def __repr__(self):
    return "<Project(title='{0}', description='{1}')>".format(self.title, self.description)
  
  
class Task(Base):
  __tablename__ = 'tasks'
  __table_args__ = {'schema' : 'household'}
  
  task_id = Column(Integer, primary_key=True)
  project_id = Column(Integer, ForeignKey('household.projects.project_id'))
  description = Column(String(length=50))
  
  project = relationship("Project")
  
  def __repr__(self):
    return "<Task(description='{0}')>".format(self.description)
  

Base.metadata.create_all(engine)

# Creating session to play with database
session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

# inserting into table
ram_project = Project(title='Ram', description='The Lord')
session.add(ram_project)
session.commit()
tasks = [Task(project_id=ram_project.project_id, description='ram-seeta tasks'), Task(project_id=ram_project.project_id, description='ram-laxman tasks')]
session.bulk_save_objects(tasks)
session.commit()

# querying database
obj = session.query(Project).filter_by(title='Ram').first()
print(obj)

