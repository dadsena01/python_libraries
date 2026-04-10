class Post:
    def __init__(self, creator, likes):
        self.creator = creator
        self.likes = likes

    def __add__(self, other):
        return f"{self.creator} and {other.creator} have {self.likes + other.likes} likes together."

    def __str__(self):
        return f"Post by {self.creator} with {self.likes} likes"

    def __repr__(self):
        return f"Post(creator='{self.creator}', likes={self.likes})"


creator1 = Post("Antu", 50)
creator2 = Post("Bantu", 30)
creator3 = Post("Chantu", 20)
print(creator1)
print(creator1 + creator2)

p1 = Post("dan", 50)
p2 = Post("eln", 20)
team = [p1, p2]

print(team)
