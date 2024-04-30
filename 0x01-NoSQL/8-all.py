#!/usr/bin/env python3
'''Lists all documents in a collection
Return an empty list if no document in the collection
'''


import pymongo


def list_all(mongo_collection):
    '''Return a list of documents
    @{param} mongo_collection - pymongo collection object
    '''
    if mongo_collection is None:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
