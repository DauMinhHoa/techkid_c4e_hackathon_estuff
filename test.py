class Post():
    def __init__(self, name, title, catagoryHave, overallHave, priceHave, catagoryNeed, min_overallNeed, max_overallNeed, min_priceNeed, max_priceNeed):
        # Have
        self.name = name
        self.title = title
        self.catagoryHave = catagoryHave
        self.overallHave = int(overallHave)
        self.priceHave = int(priceHave)
        # Need
        self.catagoryNeed = catagoryNeed
        self.min_overallNeed = int(min_overallNeed)
        self.max_overallNeed = int(max_overallNeed)
        self.min_priceNeed = int(min_priceNeed)
        self.max_priceNeed = int(max_priceNeed)

    def showPost(self):
        print(self.name, "- has", self.title, self.catagoryHave, self.overallHave, self.priceHave,
              "\n\t - need",
              self.catagoryNeed, self.min_overallNeed, self.max_overallNeed, self.min_priceNeed, self.max_priceNeed)

    def meetNeed(self, other):
        if self.catagoryHave == other.catagoryNeed and self.catagoryNeed == other.catagoryHave:
            if other.min_overallNeed <= self.overallHave <= other.max_overallNeed and self.min_overallNeed <= other.overallHave <= self.max_overallNeed:
                if other.min_priceNeed <= self.priceHave <= other.max_priceNeed and self.min_priceNeed <= other.priceHave <= self.max_priceNeed:
                    print("Meet")
                else:
                    print("not meet price")
            else:
                print("not meet overall")
        else:
            print("not meet catagory")

huy = Post("Huy","Iphone 5 black 64GB fullbox", "iOS", 100, 6000000, "Android", 95, 100, 4000000, 7000000)
huy.showPost()

hiep = Post("Hiep","Note 4 white 32GB likenew", "Android", 95, 6000000, "Android", 90, 100, 4000000, 7000000)
hiep.showPost()

hoang = Post("Hoang", "Xperia Z 32GB used", "Android", 95, 6000000, "Android", 70, 100, 2000000, 5000000)
hoang.showPost()

khanh = Post("Khanh", "Moto X 64GB brandnew", "Android", 100, 10000000, "iOS", 99, 100, 4000000, 7000000)
khanh.showPost()

nguyen = Post("Nguyen", "OnepPLus One 64GB fullbox", "Android", 96, 6000000, "iOS", 90, 100, 4000000, 7000000)
nguyen.showPost()

huy.meetNeed(hoang)
huy.meetNeed(khanh)
hiep.meetNeed(hoang)
huy.meetNeed(nguyen)


# data = [hiep, huy, hoang, khanh, nguyen]
# for i in data:
#     print(i)

# print("<Have>")
# name = input("Name:")
# title = input("Title:")
# catagoryHave = input("Catagory:")
# overallHave = int(input("Overall:"))
# priceHave = int(input("Price:"))
#
# print("<Need>")
# catagoryNeed = input("Catagory:")
# min_overallNeed = int(input("Min Overall:"))
# max_overallNeed = int(input("Max Overall:"))
# min_priceNeed = int(input("Min Price:"))
# max_priceNeed = int(input("Max Price:"))
#
# hoanh = Post(name, title, catagoryHave, overallHave, priceHave, catagoryNeed, min_overallNeed, max_overallNeed, min_priceNeed, max_priceNeed)
# hoanh.showPost()
