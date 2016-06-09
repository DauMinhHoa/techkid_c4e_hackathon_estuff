import pymongo

db_uri = "mongodb://prettygoodvega:Vegawithcheese101@ds015403.mlab.com:15403/vega"
db = pymongo.MongoClient(db_uri).get_default_database()

post_collection = db["post"]

# while True:
print("<Have>")
title = input("Title:")
catagoryHave = input("Catagory:")
overallHave = int(input("Overall:"))
priceHave = int(input("Price:"))

print("<Need>")
catagoryNeed = input("Catagory:")
min_overallNeed = int(input("Overall from:"))
max_overallNeed = int(input("Overall to:"))
min_priceNeed = int(input("Price from:"))
max_priceNeed = int(input("Price to:"))


post_collection.insert_one({"title":title, "catagoryHave": catagoryHave, "overallHave": overallHave, "priceHave":priceHave,
                            "catagoryNeed": catagoryNeed, "min_overallNeed":min_overallNeed, "max_overallNeed":max_overallNeed, "min_priceNeed":min_priceNeed, "max_priceNeed":max_priceNeed})

all_post = post_collection.find()
for x in all_post:
    print(x)
