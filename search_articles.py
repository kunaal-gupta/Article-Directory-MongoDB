import re
import pymongo
from pymongo.collection import Collection
from pymongo import MongoClient
import json
from pprint import pprint
from datetime import datetime


client = MongoClient("mongodb://localhost:27017")

db = client['291db']
dblp = db["dblp"]


def search_for_articles(dblp:Collection):

    keywords = input("Enter String: ").split()  # Get a list of inputted keywords
    keywords = ['"' + x + '"' for x in keywords]  # Surround each keyword with quotes for the AND semantics
    searchTerms = " ".join(keywords)  # Convert the list into a single string
    execStart = datetime.now()
    cursor = dblp.find({"$text":{"$search" : searchTerms}})
    execTime = datetime.now() - execStart


    # authors_list = set([])
    i = 1  # i = number of search results + 1
    for doc in cursor.clone():  # Print search results
        print('{}.\tID: {}\n\tTitle: {}\n\tYear: {}\n\tVenue: {}\n'.format(
            i, doc.get('id'), doc.get('title'), doc.get('year'), doc.get('venue')))
        i += 1

    if i > 1:  # There are search results
        userSelection = int(input("Please select an article: "))
        while not (1 <= userSelection < i):
            userSelection = int(input("Invalid input. Please select an article: "))
        selectedArticle = dblp.find({"$text":{"$search" : searchTerms}})[userSelection-1]
        print(selectedArticle.get('title'))
        

    else:
        print("No articles found that match the given keyword(s).")


    print("Query took {} seconds".format(execTime.total_seconds()))

def main():
    # title, authors, abstract, venue and year
    # dblp.drop_indexes()
    # dblp.create_index([('title', "text"), ('authors', "text"), ('abstract', "text"), ('venue', "text"), ('year', "text")], default_language="none")
    search_for_articles(dblp)

if __name__ == "__main__":
    main()
