
from sqlalchemy import String, Integer, Column
from sqlalchemy import select, create_engine, insert
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class SavedEvent(Base):
    __tablename__ = 'SavedEvents'
    eventbrite_id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    
    # TODO:
    # write the SQLAlchemy class here.
    # (use the same structure as class PopCharts on https://programming-2.vercel.app/lessons/db-and-vis/exploring-data.html)
    # but the class is called "SavedEvent"
    # and the tablename is "SavedEvents"
    # there is a column called eventbrite_id of type Integer, primary_key=True
    # there is a column called title of type String
    # there is a column called url of type String


class EventDBHelper:
    def __init__(self):
        engine = create_engine('sqlite:///event_db.db')
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        
        # TODO:
        # add the SQLAlchemy connection here:
        # (copy the same code as class PopChartsExploration's init method on https://programming-2.vercel.app/lessons/db-and-vis/exploring-data.html)
        # call create_engine with the path 'sqlite:///event_db.db' to get an engine
        # call sessionmaker on the engine to get a Session
        # call Session() to get a session instance and store it in self.session
    
    def add_saved_event(self, eventbrite_id, title, url):
        # sends a sql query to insert a row in the SavedEvents table of the database
        # (you don't need to change this method)
        
        row_contents = {
            'eventbrite_id': eventbrite_id,
            'title': title,
            'url': url
        }
        
        self.session.execute(insert(SavedEvent), row_contents)
        self.session.commit()
            
    def retrieve_saved_events(self):
        # sends a sql query to retrieve all rows in the SavedEvents table of the database
        # (you don't need to change this method)
        
        return self.session.query(SavedEvent).all()
        
