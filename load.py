import sys

import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
import os


def user_input():
    filename = input('Please provided file name (include .json): ')
    port = input('port: ')  # 271
    return filename, port


def insert_data(filename, port):
    cmd_str = f"mongoimport --port {port} --db 291db --collection dblp --drop --batchSize 15000 --file {filename}"
    os.system(cmd_str)
    client = MongoClient(f"mongodb://localhost:{port}")
    db = client["291db"]

    collist = db.list_collection_names()
    if 'dblp' in collist:
        dblp.drop()

    dblp = db["dblp"]

    # Indices
    dblp.update_many({}, [{'$set': {'year': {'$toString': '$year'}}}])  # Convert year to string
    dblp.drop_indexes()
    dblp.create_index([('title', pymongo.TEXT), ('authors', pymongo.TEXT), ('abstract', pymongo.TEXT), ('venue', pymongo.TEXT)
        , ('year', pymongo.TEXT)], default_language="none")
    dblp.create_index([('references', 1)])


def main():
    filename, port = user_input()
    print(filename)
    print(port)
    insert_data(filename, port)


if __name__ == "__main__":
    main()
