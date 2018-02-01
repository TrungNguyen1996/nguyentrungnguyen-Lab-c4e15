from pymongo import MongoClient

mongo_uri = "mongodb://amin:amin@ds157873.mlab.com:57873/nguyenkeo"
# 1. Open a connection to mlab
client = MongoClient(mongo_uri)
# 2.Get database
db = client.get_default_database()
# 3. Get collection
games = db['game']  # retri

game_list = game.find()

for game in game_list:
    print(game['description'])

# # 4 creat a new document
# new_game = {
#     'title': 'Crysis 3',
#     'description': 'Deac Space'
# }
#
# # 5.put the creat document into collection
# games.insert_one(new_game)
