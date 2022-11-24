import pymongo
from pymongo.collection import Collection


def add_article(dblp:Collection):
    """Collecting all Ids"""
    Ids = []
    for x in dblp.find({}, {'id': 1}):
        Ids.append(x['id'])


    """Getting Unique Ids from user"""
    UniqueId = input('UniqueId: ')

    while True:
        if UniqueId in Ids:
            print('Id is not unique. Enter again')
            UniqueId = input('UniqueId: ')
        else:
            break

    """Input required fields from user """

    Title = input('Title: ')
    NumofAuthors = int(input('Number of Authors: '))
    Authors = []
    for i in range(NumofAuthors):
        AuthName = input('Authors Name: ')
        Authors.append(AuthName)
    Year = int(input('Year: '))

    Venue = None
    Abstract = None
    References = []
    n_citation = 0

    """Inserting document in the collection"""
    try:
        mydict = {'abstract': Abstract, 'authors': Authors, 'n_citation': n_citation, 'references': References, 'title': Title, 'venue': Venue, 'year': Year, 'id': UniqueId}
        dblp.insert_one(mydict)
    except:
        pass
    else:
        print('Successfully inserted document in the collection')