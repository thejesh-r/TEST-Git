import pymongo

client = pymongo.MongoClient("mongodb+srv://thejesh-mongo-db:mongodb123@mongo-test.no0pz.mongodb.net/?retryWrites"
                             "=true&w=majority")
db = client.test
print(db)

d = {
    "name": "thejeshkumar",
    "email": "thejeshk312@gmail.com",
    "surname": "reddy"
}

db1 = client['mongotest']
coll1 = db1['test']
coll1.insert_one(d)

