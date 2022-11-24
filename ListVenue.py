import os

from pymongo import MongoClient
from pymongo.collection import Collection
import pymongo


def list_venues(dblp:Collection):
    print('Fetching data. Please wait...')
    a = dblp.aggregate([{
        "$match": {
            "references": {
                "$exists": True
            }
        }
    }, {
        "$group": {
            "_id": "$venue",
            "count": {
                "$sum": 1
            }
        }
    }, {
        "$project": {
            "venue": "$_id",
            "count": 1,
            "_id": 0
        }
    }])

    b = dblp.aggregate([{
        "$match": {
            "venue": {
                "$exists": True
            }
        }
    }, {
        "$group": {
            "_id": "$venue",
            "count": {
                "$sum": 1
            }
        }
    }, {
        "$project": {
            "venue": "$_id",
            "count": 1,
            "_id": 0
        }
    }])

    tempA = {}

    for i in a:
        tempA[i['venue']] = [i['count'], 0]

    for i in b:
        if i['venue'] not in tempA.keys():
            tempA[i['venue']] = [0, 0]

        tempA[i['venue']][1] = i['count']

    Final = sorted(tempA.items(), key=lambda e: e[1][1], reverse=True)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the system terminal to look cleaner

    n = int(input('Enter a number n and see a listing of top n venues: '))
    print()
    print('Venue Name, Number of articles that reference a paper in that venue, Number of articles in that venue')
    print()
    print('-----------------------Showing Results----------------')
    try:
        for i in range(n):
            print(Final[i])
    except IndexError:
        print()
        print('Unfortunately, we only have {} records, but you asked for {}'.format(len(Final), n))
    print()
    print('--------------------End of the result------------------')
    print()


