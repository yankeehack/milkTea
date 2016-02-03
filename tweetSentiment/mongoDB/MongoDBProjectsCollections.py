__author__ = 'yazhu'
from mongoDBBase import mongoBase
from django.conf import settings


class mongoBaseProjectsCollections(mongoBase):
    collections = None

    def __init__(self):
        super(mongoBaseProjectsCollections, self).__init__()
        self.collections = self.mongo_connection[settings.MONGODB['DB_NAME']][settings.MONGODB['COLLECTION_NAME']]

    def getProjects(self, fields=None):
        if not fields:
            fields = settings.MONGODB['DEFAULT_FIELDS']
        return self.collections.find(projection=fields)

    def closeConnection(self):
        self.mongo_connection.close()