import generator
import random

rand = random.randrange(0,len(generator.seen))
word = generator.seen[rand]

for i in range(len(generator.seen) - 20):
    stuff = generator.after_amount[rand]
    rand = random.randrange(0,len(stuff))
    word = stuff[rand]

    print(word,end=" ")
    rand = generator.seen.index(word)

    pass

