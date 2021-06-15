from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    # client = MongoClient('localhost', 32768, username='admin', password='admin', serverSelectionTimeoutMS=1000)
    client = MongoClient('mongodb://localhost:32768')
    db = client['parlebot']
    try: 
        db.command("serverStatus")
    except Exception as e: 
        print(e)
    else: 
        print("You are connected!")
    client.close()
    # info = client.server_info()
except ConnectionFailure:
    print('Something went wrong')

# db = client['parlebot']

# downloadFiles = db.downloadFiles

# document = {
#     'question':'q1',
#     'fileName':'test',
#     'filePath':'file/test',
#     'fileType':'doc',
#     'webLink':'www.test.com',
#     'author_name':'test',
#     'author_ministry':'test'
# }

# result = downloadFiles.insert_one(document)
# print('document id: {0}'.format(result.inserted_id))