class User:

      def __init__(self, name , id):# Constructor
          self.name = name  #attributes
          self.id = id
          self.followers = 0
          self.following = 0


      def follow(self, user):
          user.followers = +1
          self.following =+1


user1 = User("Rajiv" , "47")
user2 = User("ping" , "04")
# user1.id = 2
# user1.name = "T-Series"

user1.follow(user2)

print(user2.followers)


