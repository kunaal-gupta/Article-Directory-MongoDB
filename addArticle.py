import pymongo
from pymongo.collection import Collection


def add_an_article(dblp:Collection):
    print('We are now going to ask you a few details to add an article.')
    """Collecting all Ids"""
    Ids = []
    for x in dblp.find({}, {'id': 1}):
        Ids.append(x['id'])

    print('So let\'s begin..')
    print()

    print('------------------------------')

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
    print()
    """Inserting document in the collection"""
    try:
        mydict = {'abstract': Abstract, 'authors': Authors, 'n_citation': n_citation, 'references': References, 'title': Title, 'venue': Venue, 'year': Year, 'id': UniqueId}
        dblp.insert_one(mydict)
    except:
        pass
    else:
        print('Successfully inserted a new article in the collection')
    print('------------------------------')
    print()


