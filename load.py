import sys
from pymongo import MongoClient
from pymongo.collection import Collection
import os


def insert_data(filename, port):
    cmd_str = f"mongoimport --port {port} --db 291db --collection dblp --drop --batchSize 15000 --file {filename}"
    os.system(cmd_str)
    client = MongoClient(f"mongodb://localhost:{port}")
    db = client["291db"]
    dblp = db["dblp"]


def user_input():
    filename = input('Please provided file name (include .json): ')
    port = input('port: ')
    return filename, port

def main():
    filename, port = user_input()
    print(filename)
    print(port)
    insert_data(filename, port)

if __name__ == "__main__":
    main()
