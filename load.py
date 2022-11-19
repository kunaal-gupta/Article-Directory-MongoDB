import sys
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
    mydb = client["291db"]
    mycol = mydb["dblp"]


def main():
    filename, port = user_input()
    print(filename)
    print(port)
    insert_data(filename, port)
<<<<<<< HEAD

=======
>>>>>>> ec0e77a654cc218d1cc010173cb1810e463e608c

if __name__ == "__main__":
    main()
