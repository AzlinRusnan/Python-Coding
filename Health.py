import random

health = 50

difficulty = 1

potion_health = int(random.randint(25,50) / difficulty)

health = health + potion_health

print(health)


#health potion with difficulty level that you can adjusted.
#difficulty level 1-3
#the higher the difficulty level, the lower the health grade
#random.randint gives random number
#int is used to convert float to int

