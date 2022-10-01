import pymongo
client = pymongo.MongoClient("mongodb+srv://Rahul:Rahul12345@fiona.qlcvnoq.mongodb.net/?retryWrites=true&w=majority")
db = client.test


database = client['myinfo']
collection = database["sudh"]


# records = collection.find()
# for i  in records:
#     print(i)
data2 =collection.find({"companyName": "ineuron"})

for i  in data2:
    print(i)