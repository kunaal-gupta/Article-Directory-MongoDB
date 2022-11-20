import re
from pymongo.collection import Collection
from pymongo import MongoClient
import json
from pprint import pprint
from datetime import datetime


client = MongoClient("mongodb://localhost:27017")

db = client['291db']
dblp = db["dblp"]

def search_for_authors(dblp:Collection):

    keyword = input("Enter String: ")
    time_start=datetime.now()
    cursor = dblp.find({"$text":{"$search" : keyword}})


    authors_list = set([])
    for doc in cursor:
        authors_list.update(doc.get('authors'))
    authors_list = list(authors_list)
    
    authors = []
    for author in authors_list:
        if (re.search(r"\b" + keyword + r"\b", author,re.IGNORECASE)):
            authors.append(author)

    if (len(authors) != 0):
        for i in range(len(authors)):
            auth_name = authors[i]
            print(str(i) + " " + auth_name + ": " + str(dblp.count_documents({"authors":auth_name})))

        selection = int(input("Please select a row the number: "))

        while (selection >= len(authors)):
            selection = int(input("Wrong Input. Please select a row the number: "))

        author_name = authors[selection]
        cursor = dblp.find({"authors": author_name}).sort("year",-1)
        print()
        print(author_name)
        for doc in cursor:
            print("Title: " + str(doc.get('title')))
            print("Year: " + str(doc.get('year')))
            print("Venue: " + str(doc.get('venue')))
            print()
    else:
        print("Sorry, no author found with the given keyword: "+keyword)


    time_end=datetime.now()
    e= time_end - time_start
    print("The execution time of python program is : ",e)

def main():
    search_for_authors(dblp)

if __name__ == "__main__":
    main()
