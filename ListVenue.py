import os

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['291db']
dblp = db["dblp"]


def list_venues():
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
    print('Venue Name, Number of articles in that venue, and the Number of articles that reference a paper in that venue')
    print()
    print('-----------------------Showing Results----------------')

    for i in range(n):
        print(Final[i])
    print()
    print('--------------------End of the result------------------')
    print()


def main():
    list_venues()


if __name__ == '__main__':
    main()
