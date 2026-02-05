# Who pay the bill

import random

friends = ['rajiv' , 'ranjan','ping', 'pong']
length = len(friends)#4
print(type(friends))
# print(random.choice(friends))

choice_friends = random.randint(0,(length-1))#0---3--->4
print(friends[choice_friends])