import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["291db"]
mycol = mydb["dblp"]

"""Fetching Venue Names"""
VenueName = []
for x in mycol.find({}, {'_id': 0, "venue": 1}):
    if x['venue'] not in VenueName:
        VenueName.append(x['venue'])

"""Fetching the number of articles & the number of articles that reference a paper in that venue"""
NumOfArticles = []
NumOfArticles_Ref = []

for i in VenueName:
    countArt = 0
    countArtRef = 0
    for x in mycol.find({}, {'_id': 0, "venue": 1, 'references': 1}):
        # print(x)

        if i == x['venue']:
            countArt += 1
            if 'references' in x.keys():
                if x['references'] != 0:
                    countArtRef += 1

    NumOfArticles.append(countArt)
    NumOfArticles_Ref.append(countArtRef)

# print(VenueName)
# print(NumOfArticles)
# print(NumOfArticles_Ref)

"""Making a single array of data for sorting"""
Array = []
for i in range(len(VenueName)):
    Array.append([ NumOfArticles_Ref[i], VenueName[i], NumOfArticles[i]])

"""Sort the result based on the number of papers that reference the venue with the top most cited venues shown first. """
Array.sort(reverse=True)

"""Printing first n rows of data"""
n = int(input('Number of top venues you\'d like to see: '))
for i in range(n):
    print(Array[i])


