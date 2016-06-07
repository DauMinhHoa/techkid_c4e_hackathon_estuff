class Post():
    def __init__(self, name, title, overall, catagory, price, catagoryNeed, start_overallNeed, end_overallNeed, start_priceNeed, end_priceNeed):
        self.name = name
        self.title = title
        self.overall = int(overall)
        self.catagory = catagory
        self.price = int(price)

        self.catagoryNeed = catagoryNeed
        self.start_overallNeed = int(start_overallNeed)
        self.end_overallNeed = int(end_overallNeed)
        self.start_priceNeed = int(start_priceNeed)
        self.end_priceNeed = int(end_priceNeed)

    def showPost(self):
        print(self.name, "- has", self.title, self.overall, self.catagory, self.price,
              "\n\t - need",
              self.catagoryNeed, self.start_overallNeed, self.end_overallNeed, self.start_priceNeed, self.end_priceNeed)

    def matchNeed(self, other):
        if self.catagoryNeed == other.catagory:
            if self.start_overallNeed < other.overall < self.end_overallNeed + 1:
                if self.start_priceNeed < other.price < self.end_priceNeed:
                    print("Match")
                else:
                    print("Unmatch price")
            else:
                print("Unmatch overall")
        else:
            print("Unmatch catagory")

huy = Post("Huy","Iphone 5 black 64GB fullbox", 99, "iOS", 5000000, "Android", 90, 100, 4000000, 7000000)
huy.showPost()

hiep = Post("Hiep","Note 4 white 32GB likenew", 95, "Android", 6000000, "iOs", 90, 100, 4000000, 7000000)
hiep.showPost()

hoang = Post("Hoang", "Xperia Z 32GB used", 70, "Android", 3000000, "Android", 70, 90, 2000000, 5000000)
hoang.showPost()

khanh = Post("Khanh", "Moto X 64GB brandnew", 100, "Android", 10000000, "iOS", 99, 100, 4000000, 7000000)
khanh.showPost()

huy.matchNeed(hiep)
huy.matchNeed(hoang)
huy.matchNeed(khanh)
hiep.matchNeed(hoang)


