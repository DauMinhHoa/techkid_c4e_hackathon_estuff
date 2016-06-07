import pymongo

db_uri = "mongodb://prettygoodvega:Vegawithcheese101@ds015403.mlab.com:15403/vega"
db = pymongo.MongoClient(db_uri).get_default_database()

post_collection = db["post"]


# print("<Have>")
# title = input("Title:")
# overall = int(input("Overall:"))
# catagory = input("Catagory:")
# price = int(input("Price:"))
#
# print("<Need>")
# catagoryNeed = input("Catagory:")
# start_overallNeed = int(input("Overall from:"))
# end_overallNeed = int(input("Overall to:"))
# start_priceNeed = int(input("Price from:"))
# end_priceNeed = int(input("Price to:"))
#
#
# post_collection.insert_one({"title":title, "overall": overall, "catagory": catagory, "price":price,
#                             "catagoryNeed": catagoryNeed, "start_overallNeed":start_overallNeed, "end_overallNeed":end_overallNeed, "start_priceNeed":start_priceNeed, "end_priceNeed":end_priceNeed})

all_post = post_collection.find()
for x in all_post:
    print(x["title"])


# class Post():
#     def __init__(self, name, title, overall, catagory, price, catagoryNeed, start_overallNeed, end_overallNeed, start_priceNeed, end_priceNeed):
#         self.name = name
#         self.title = title
#         self.overall = int(overall)
#         self.catagory = catagory
#         self.price = int(price)
#
#         self.catagoryNeed = catagoryNeed
#         self.start_overallNeed = int(start_overallNeed)
#         self.end_overallNeed = int(end_overallNeed)
#         self.start_priceNeed = int(start_priceNeed)
#         self.end_priceNeed = int(end_priceNeed)
#
#     def showPost(self):
#         print(self.name, "- has", self.title, self.overall, self.catagory, self.price,
#               "\n\t - need",
#               self.catagoryNeed, self.start_overallNeed, self.end_overallNeed, self.start_priceNeed, self.end_priceNeed)
#
#     def matchNeed(self, other):
#         if self.catagoryNeed == other.catagory:
#             if self.start_overallNeed < other.overall < self.end_overallNeed + 1:
#                 if self.start_priceNeed < other.price < self.end_priceNeed:
#                     print("Match")
#                 else:
#                     print("Unmatch price")
#             else:
#                 print("Unmatch overall")
#         else:
#             print("Unmatch catagory")