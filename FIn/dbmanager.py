import operator
from random import randint as r

"""
This class handles the messaging log
"""


class dbmanager():
    def __init__(self):
        self.db_name = 'clueless'
        self.db = []

    def insert_object(self, object_name, content=None):
        if content is None:
            content = dict()
        else:
            self.db.append([object_name, content])

    def setvalue(self, ii, content):
        self.db[ii] = content

    def addvalue(self, content):
        self.db.append(content)

    def getvalue(self, ii):
        return self.db[ii]



