import random

# v1
for n in range(10):
    x = random.randrange(0, 25)
    y = random.random()
    print(x + y)

for n in range(10):
    y = random.random() * 25
    print(y)

for n in range(10):
    y = random.randrange(0, 250) / 10
    print(y)