import re
from pymongo.collection import Collection
from pymongo import MongoClient
import json
from pprint import pprint
from datetime import datetime
import pandas as pd

client = MongoClient("mongodb://localhost:27017")

db = client['291db']
dblp = db["dblp"]

def search_for_authors(dblp:Collection):

    keyword = input("Enter String: ")
    time_start=datetime.now()
    cursor = dblp.find({"$text":{"$search" : keyword}})

    authors_list = []
    for doc in cursor:
        authors_list.extend(doc.get('authors'))
    counts = pd.Series(authors_list).value_counts()
    authors_list = list(set(authors_list))
    
    authors = []
    author_count = 0
    for author in authors_list:
        if (re.search(r"\b" + keyword + r"\b", author,re.IGNORECASE)):
            authors.append(author)
            print(str(author_count) + " " + author + "  "+ str(counts.get(author)))
            author_count = author_count+1

    time_end=datetime.now()
    e= time_end - time_start
    print("The execution time of python program is : ",e)


    if (len(authors) != 0):
        selection = int(input("Please select a row the number: "))

        while (selection >= len(authors)):
            selection = int(input("Wrong Input. Please select a row the number: "))

        author_name = authors[selection]
        cursor = dblp.find({"authors": author_name}).sort("year",-1)
        print()
        print(author_name)
        for doc in cursor:
            print("Title: " + str(doc.get('title')) + '\n' + "Year: " + str(doc.get('year')) + '\n' + "Venue: " + str(doc.get('venue')) + '\n')

    else:
        print("Sorry, no author found with the given keyword: "+keyword)

def main():
    search_for_authors(dblp)

if __name__ == "__main__":
    main()
