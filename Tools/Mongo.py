from pymongo import MongoClient


class MongoDb(object):
    def __init__(self,host='localhost',port=27017):
        self.client = MongoClient(host=host, port=port)

    @property
    def db(self):
        if hasattr(self,'_db'):
            return self._db
        raise AttributeError("'MongoDb' object has no attribute '_db',please set the db like (MongoDb's instance.db = xxxx<db's name> )")

    @db.setter
    def db(self,db):
        self._db = self.client[db]

    @property
    def collection(self):
        if hasattr(self,'_collection'):
            return self._collection
        raise AttributeError(
            "'MongoDb' object has no attribute '_collection',please set the db like (MongoDb's instance.collection = xxxx<collection's name> )")

    @collection.setter
    def collection(self,collection):
        self._collection = self.db[collection]



    def insert(self,doc,*args,**kwargs):
        if not isinstance(doc,dict):
            raise TypeError("param doc must be a dict's instance")

        return self.collection.insert(doc)



if __name__ == '__main__':
    mongo = MongoDb()
    mongo.db = "test"
    mongo.collection = "redi"
    print(mongo.insert(doc={"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"]}))


# db = client.xyh_api
# collection = db.redi
# post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"]}
# collection.insert(post)

