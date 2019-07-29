from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.automap import automap_base
from geoalchemy2 import *

class MetadataCache(object):
    def __init__(self, engine, schema):
        self.engine = engine
        self.schema = schema
        self.metadata = None

    @property
    def cache_name(self):
        final_name = '{0}.{1}.cache'.format(self.engine.url.database,
                                            self.schema)
        return final_name

    def get_or_create_metadata(self):

        if os.path.exists(self.cache_name):
            with open(self.cache_name, 'r') as cachefile:
                self.metadata = pickle.load(cachefile)
        else:
            self.metadata = MetaData()
            self.metadata.reflect(bind=self.engine, schema=self.schema)
            with open(self.cache_name, 'w') as cachefile:
                pickle.dump(self.metadata, cachefile)

        return self.metadata

engine = create_engine('postgresql://postgres:d4t4l4b@dataLab/inegi_dwh', convert_unicode=True)
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine)) 
Base.query = db_session.query_property()
