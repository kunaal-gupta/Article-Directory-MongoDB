import sys

import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
import os
import multiprocessing
from datetime import datetime

def user_input():
    filename = input('Please provided file name (include .json): ')
    port = input('port: ')  
    return filename, port


def insert_data(json_filename, port):
    time_start=datetime.now()
    mongoprint_cmd = f"mongoimport --port {port} --db 291db --collection dblp --drop --batchSize 15000 --file {json_filename} --numInsertionWorkers {multiprocessing.cpu_count()}"
    os.system(mongoprint_cmd)
    client = MongoClient(f"mongodb://localhost:{port}")
    db = client["291db"]
    dblp = db["dblp"]
    dblp.drop_indexes()
    dblp.create_index([('references', 1)])

    # Indices
    dblp.update_many({}, [{'$set': {'year': {'$toString': '$year'}}}])  # Convert year to string
    dblp.create_index([('title', pymongo.TEXT), ('authors', pymongo.TEXT), ('abstract', pymongo.TEXT), ('venue', pymongo.TEXT), ('year', pymongo.TEXT)], default_language="none")

    time_end=datetime.now()
    e= time_end - time_start
    print("The execution time of python program is : ",e)

    print("Collection is Created!")


def main():
    json_filename, port = user_input()
    insert_data(json_filename, port)


if __name__ == "__main__":
    main()
