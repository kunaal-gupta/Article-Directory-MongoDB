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


def create_indices():
    dblp.update_many({}, [{'$set': {'year': {'$toString': '$year'}}}])  # Convert year to string
    dblp.drop_indexes()
    dblp.create_index([('title', pymongo.TEXT), ('authors', pymongo.TEXT), ('abstract', pymongo.TEXT), ('venue', pymongo.TEXT)
        , ('year', pymongo.TEXT)], default_language="none")
    dblp.create_index([('references', 1)])


def search_for_articles(dblp:Collection):

    keywords = input("Enter String: ").split()  # Get a list of inputted keywords
    keywords = ['"' + x + '"' for x in keywords]  # Surround each keyword with quotes for the AND semantics
    searchTerms = " ".join(keywords)  # Convert the list into a single string
    cursor = dblp.find({"$text":{"$search" : searchTerms}})

    i = 1  # i = number of search results + 1
    for doc in cursor.clone():  # Print search results
        print('{}.\tID: {}\n\tTitle: {}\n\tYear: {}\n\tVenue: {}\n'.format(
            i, doc.get('id'), doc.get('title'), doc.get('year'), doc.get('venue')))
        i += 1

    if i > 1:  # i > 1 means there was at least 1 matching article
        userSelection = int(input("Please select an article: "))
        while not (1 <= userSelection < i):  # 
            userSelection = int(input("Invalid input. Please select an article: "))
        artcl = dblp.find({"$text":{"$search" : searchTerms}})[userSelection-1]
        print('\n\nID: {}\nTitle: {}\nYear: {}\nVenue: {}\nAbstract: {}\nAuthors: {}\n'.format(
            artcl.get('id'), artcl.get('title'), artcl.get('year'), artcl.get('venue'), artcl.get('abstract'), ", ".join(artcl.get('authors'))))
        # print(dblp.find({"$text":{"$search" : artcl.get('id')}}).explain()['executionStats'])
        refs = dblp.find({"references":artcl.get('id')})
        i = 1  # i = number of references + 1
        for doc in refs.clone():  # Print search results
            i += 1
        if i == 1:
            print('No other articles reference this article.')
        else:
            print('Other articles that reference this article:')
            for doc in refs:
                print('ID: {}\nTitle: {}\nYear: {}\n'.format(doc.get('id'), doc.get('title'), doc.get('year')))
    else:  # No articles that match the user's input
        print("No articles found that match the given keyword(s).")

def main():
    # create_indices()
    search_for_articles(dblp)

if __name__ == "__main__":
    main()
